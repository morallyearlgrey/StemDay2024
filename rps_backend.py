import cv2  # Accesses and manipulates webcam images
import mediapipe as mp  # Performs AI analysis on images and outputs object identifiers (landmarks) and visuals
import random  # Selects random rock-paper-scissors gesture for computer (CPU) player
from collections import deque  # Holds list (deque) of last five gesture image detections made by backend
import statistics as st  # Determines most common gesture in deque as player's selected gesture
import tkinter as tk #
from PIL import Image, ImageTk # Holds webcam video frames to cycle through

# Determines message displayed at end-of-game
# Input: CPU's selected gesture (str) and player's selected gesture (str)
# Output: Game end phrase (str)
def calculate_winner(cpu_choice, player_choice):

    # Determines the winner of each round when passed the computer's and player's moves

    if player_choice == "Invalid":
        return "Invalid!"

    if player_choice == cpu_choice:
        return "Tie!"

    elif player_choice == "Rock" and cpu_choice == "Scissors":
        return "You win!"

    elif player_choice == "Rock" and cpu_choice == "Paper":
        return "CPU wins!"

    elif player_choice == "Scissors" and cpu_choice == "Rock":
        return "CPU wins!"

    elif player_choice == "Scissors" and cpu_choice == "Paper":
        return "You win!"

    elif player_choice == "Paper" and cpu_choice == "Rock":
        return "You win!"

    elif player_choice == "Paper" and cpu_choice == "Scissors":
        return "CPU wins!"

# Counts the number of fingers held up on the webcam
# Inputs: List of hand-joint landmarks (lists containing each joint's x-coord [1], y-coord [2], and hand type [3]) and int of held-up fingers counted so far (defaults to 0)
# Output: Integer count of held-up fingers
def compute_fingers(hand_landmarks, finger_count):

    # Coordinates are used to determine whether a finger is being held up or not
    # This is done by determining whether the tip of the finger is above or below the base of the finger
    # For the thumb it determines whether the tip is to the left or right (depending on whether it's their right or left hand)

    # Index Finger (if lower joint is below tip, count finger as held-up)
    if hand_landmarks[8][2] < hand_landmarks[6][2]:
        finger_count += 1

    # Middle Finger
    if hand_landmarks[12][2] < hand_landmarks[10][2]:
        finger_count += 1

    # Ring Finger
    if hand_landmarks[16][2] < hand_landmarks[14][2]:
        finger_count += 1

    # Pinky Finger
    if hand_landmarks[20][2] < hand_landmarks[18][2]:
        finger_count += 1

    # Thumb (If tip is farther to the right than joint on left-hand, count it)
    if hand_landmarks[4][3] == "Left" and hand_landmarks[4][1] > hand_landmarks[3][1]:
        finger_count += 1
    elif hand_landmarks[4][3] == "Right" and hand_landmarks[4][1] < hand_landmarks[3][1]:
        finger_count += 1
    return finger_count

# Opening AI analysis with low (0) complexity and confidence levels for hand detection and tracking (default = 0.5)
class WebcamAI:
    def __init__(self, window):
        self.window = window
        self.window.title("Webcam")

        self.webcam = cv2.VideoCapture(0) # Using OpenCV to capture from the webcam

        self.current_image = None

        self.canvas = tk.Canvas(window, width=640,height=480)
        self.canvas.pack()

        self.update_webcam()

    def update_webcam(self):
        # Loading in mediapipe drawing tools
        mp_drawing = mp.solutions.drawing_utils
        mp_drawing_styles = mp.solutions.drawing_styles
        # Loading mediapipe hand-specific analysis tools
        mp_hands = mp.solutions.hands
        # List of possible gestures CPU can choose from
        cpu_choices = ["Rock", "Paper", "Scissors"]
        # Default CPU and player's chosen gestures to nothing first
        cpu_choice, player_choice = "Nothing", "Nothing"
        # Set scores for CPU and player to zero
        cpu_score, player_score = 0, 0
        # Set color of winner to green by default
        winner_colour = (0, 255, 0)
        # Determines whether hand is detected and should be analyzed for finger count
        hand_valid = False
        # List of possible gestures in image, using number of fingers as index
        display_values = ["Rock", "Invalid", "Scissors", "Invalid", "Invalid", "Paper"]
        # Text displayed for winner at end-of-game
        winner = "None"
        # Queue list containing five "nothing" elements
        de = deque(['Nothing'] * 5, maxlen=5)
        with mp_hands.Hands(
                model_complexity=0,
                min_detection_confidence=0.5,
                min_tracking_confidence=0.5) as hands:
            success, frame = self.webcam.read()
            # Running program if webcam found
            if success:
                # Formatting image color type, orientation, and more before analysis
                frame = cv2.flip(frame, 1)
                frame.flags.writeable = False
                results = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
                frame.flags.writeable = True
                # Type (left or right) of hand on screen (0 or 1)
                handNumber = 0
                # List of hand joints, including their coordinates and which hand they are on
                hand_landmarks = []
                # Condition checking whether finger counting should be happening
                isCounting = False
                # Int count of held-up fingers
                count = 0

                # If at least one hand is detected counting will happen
                if results.multi_hand_landmarks:
                    isCounting = True

                    # hand_valid acts as a flag for when hand is first detected so the CPU does not "play" a move multiple times
                    if player_choice != "Nothing" and not hand_valid:

                        hand_valid = True
                        # Select random gesture for CPU to play
                        cpu_choice = random.choice(cpu_choices)
                        # Choose winner from CPU and player choices
                        winner = calculate_winner(cpu_choice, player_choice)

                        # Incrementing scores of player or CPU and choosing end-game win message color
                        if winner == "You win!":
                            player_score += 1
                            winner_colour = (255, 0, 0)
                        elif winner == "CPU wins!":
                            cpu_score += 1
                            winner_colour = (0, 0, 255)
                        elif winner == "Invalid!" or winner == "Tie!":
                            winner_colour = (0, 255, 0)

                    # Drawing the hand skeletons
                    for hand in results.multi_hand_landmarks:
                        # Identifying joints and drawing on screen
                        mp_drawing.draw_landmarks(
                            frame,
                            hand,
                            mp_hands.HAND_CONNECTIONS,
                            mp_drawing_styles.get_default_hand_landmarks_style(),
                            mp_drawing_styles.get_default_hand_connections_style())

                        # Figures out whether it's a left hand or right hand in frame
                        label = results.multi_handedness[handNumber].classification[0].label

                        # Converts unit-less hand landmarks into pixel counts
                        for id, landmark in enumerate(hand.landmark):
                            imgH, imgW, imgC = frame.shape
                            xPos, yPos = int(landmark.x *
                                             imgW), int(landmark.y * imgH)

                            hand_landmarks.append([id, xPos, yPos, label])

                        # Number of fingers held up are counted
                        count = compute_fingers(hand_landmarks, count)

                        # Switch to next hand (if available) to analyze
                        handNumber += 1
                # If there is no hand detected, there is no valid hand for the game to happen
                else:
                    hand_valid = False

                # The number of fingers being held up is used to determine which move is made by the player
                if isCounting and count <= 5:
                    player_choice = display_values[count]
                    # Counting errors accounted for as invalid
                elif isCounting:
                    player_choice = "Invalid"
                    # Player cannot have gesture inputted if fingers have not been counted
                else:
                    player_choice = "Nothing"

                # Adding the detected move to the left of the double-ended queue
                de.appendleft(player_choice)

                # Instead of using the first move detected, the mode (most often observed gesture) is taken for more accurate detection
                try:
                    player_choice = st.mode(de)
                except st.StatisticsError:
                    print("Stats Error")

                self.current_image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
                self.photo = ImageTk.PhotoImage(image=self.current_image)
                self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)
                self.window.after(15, self.update_webcam)
            else:
                print("Error: Video capture failed")

root = tk.Tk()
app = WebcamAI(root)
root.mainloop()