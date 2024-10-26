# IMPORTS
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter.font import Font
from tkinter.font import Font


from rps_backend import WebcamAI

# MAIN MENU AND TITLE INITIALIZATION
# Create the main menu and initialize the title
root = Tk()
root.title("Rock, Paper, AI Sensors")

# COLOR PALETTE
beige = "#e2d5d5"
blue = "#5582c4"
red = "#c05953"
green = "#72c68a"
black = "#393845"
gray = "#9d8c89"
orange = "#c58955"
yellow = "#f7d559"
black = "#393845"
gray = "#9d8c89"
orange = "#c58955"
yellow = "#f7d559"

# CONFIGURATION OF MAIN WINDOW 
# Configure the main window's grid and its border
root.grid_rowconfigure(0, weight=0)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
#if the border doesn't work, we can just use this and it should be fine
root.config(bg=beige, highlightthickness=13, highlightbackground=blue, highlightcolor=blue)

#root.config(bg=beige) # uncomment this when you want to try the border :3


""" note for Kai: I think it can work hyptothetically with this code but the spacing throws off everything. Maybe you can try to
figure out how to make the border work? I'll leave this here for you, just uncomment when you're ready to try it out!"""
# good luck...
""" ATTEMPTING to make a border with rectangles! """
# # Create canvas widget for border with dynamic size
# canvasBorder = Canvas(root, width=root.winfo_width(), height=root.winfo_height(), bg=beige, highlightthickness=0, bd=0)
# canvasBorder.grid(row=0, column=0, rowspan=3, columnspan=3, sticky='nsew')

# # Update the border dimensions based on the root size
# def draw_borders():
#     window_width = root.winfo_width()
#     window_height = root.winfo_height()

#     borderThickness = 13

#     canvasBorder.delete("all")  # Clear previous rectangles
#     canvasBorder.create_rectangle(0, 0, window_width, borderThickness, fill=gray, outline=beige) # top-border
#     canvasBorder.create_rectangle(0, 0, borderThickness, window_height, fill=blue, outline=beige) # left-border 
#     canvasBorder.create_rectangle(window_width - borderThickness, 0, window_width, window_height, fill=red, outline=beige) # right-border
#     canvasBorder.create_rectangle(0, window_height - borderThickness, window_width, window_height, fill=yellow, outline=beige) # bottom-border

# # Call the function to draw borders initially
# draw_borders()

# # Bind to the configure event to redraw borders on resize
# root.bind("<Configure>", lambda event: draw_borders())

""" ATTEMPTING to make a border with rectangles! """

# FULLSCREEN FUNCTIONS 
# Automatically fullscreens the screen
root.attributes("-fullscreen", True)

# Function to exit fullscreen mode
def exit_fullscreen(event=None):
    root.attributes("-fullscreen", False)
    root.overrideredirect(False)

# Function to toggle fullscreen mode
def toggle_fullscreen(event=None):
    is_fullscreen = root.attributes("-fullscreen")
    root.attributes("-fullscreen", not is_fullscreen)
    root.overrideredirect(not is_fullscreen)

# Bind the Escape key to exit fullscreen mode
root.bind("<Escape>", exit_fullscreen)

# Bind the F11 key to toggle fullscreen mode
root.bind("<F11>", toggle_fullscreen)

# TITLE
# Title on the top of the screen configuration
label = Label(
    root,
    text="ROCK, PAPER, AI SENSORS",
    font=("Kalam", 60, "bold"),
    foreground=black,
    bg=beige
)
label.grid(column=0, row=0, pady=(40, 10))

# CONTENT (ENCAPSULATES AI AND PLAYER FRAMES)
content = Frame(root, bg=beige)
content.grid(row=1, column=0, sticky='nsew')

# DOTTED LINE
# Create a Canvas widget
canvas = Canvas(content, width=5, bg=beige, highlightthickness=0)
canvas.grid(row=0, column=1, sticky='ns')

# Function to print coordinates on click
def print_coords(event):
    print(f"Clicked at: ({event.x}, {event.y})")

# Bind left mouse click to print_coords function
canvas.bind("<Button-1>", print_coords)

# Draw the dashed line on the Canvas
canvas.create_line(2, -10, 2, 670, fill=orange, width=10, dash=(50, 7))

# SETS WHAT WILL BE IN THE CONTENT 
# AI
# Outer frame to create that polaroid-esque border outside
outerAIFrame = Frame(
    content, 
    borderwidth=5, 
    bg=gray
)  
outerAIFrame.grid(column=0, row=0, padx=(20, 20), pady=(0, 0))

# Actual AI frame
aiFrame = Frame(
    outerAIFrame, 
    borderwidth=0, 
    relief="ridge", 
    width=550, 
    height=525,
    bg=beige
)

# Connecting the AI's images and configuring it 
aiImagePath = "images/ai_background.png"
aiImage = Image.open(aiImagePath)
aiImage = aiImage.resize((300, 300), Image.LANCZOS)
aiImageTked = ImageTk.PhotoImage(aiImage)

# Creates a frame to hold the AI image
aiImageFrame = Frame(
    content,
    width=300,
    height=300,
    bg=beige,
)

# Creates a label containing the tked image to go inside of the frame
aiImageLabel = Label(aiImageFrame, image=aiImageTked)
aiImageLabel.pack(expand=True, fill='both', pady=(0, 0))
aiImageFrame.pack_propagate(False)
aiImageLabel.config(bg=beige, highlightthickness=0)

# Center the aiImageFrame within aiFrame
aiImageFrame.place(relx=0.5, rely=0.9, anchor='center')

# For configuration of the AI frame itself
aiFrame['borderwidth'] = 0
aiFrame['relief'] = 'solid'
aiFrame.grid_propagate(False)

# Frame holding AI Title and AI Label
AIInfoFrame = Frame(aiFrame, bg=gray)
AIInfoFrame.grid(row=0, column=0, sticky='nsew')

# PLAYER
# Outer frame to create that polaroid-esque border outside
outerPlayerFrame = Frame(
    content, 
    borderwidth=5, 
    bg=gray
)  
outerPlayerFrame.grid(column=2, row=0, padx=(20, 20), pady=(0, 0))

# Actual player frame
playerFrame = Frame(
    outerPlayerFrame,
    borderwidth=5, 
    relief="ridge", 
    width=525, 
    height=550,
    bg=beige,
)
playerFrame['borderwidth'] = 0
playerFrame['relief'] = 'solid'
playerFrame.grid_propagate(False)

# Connecting the player's webcam and configuring it 

# Winner Label
winnerLabel = Label(
    content,
    text="Winner: ",
    font=("Kalam", 40, "bold"),
    bg=beige,
    fg=black
)

winnerText = StringVar()
winnerLabel['textvariable'] = winnerText
winnerText.set("...")  

# Place the winner label below the number graphic
winnerLabel.grid(column=1, row=1, pady=(10, 20))

playerImageFrame = Frame(playerFrame, borderwidth=0, relief="ridge", highlightthickness=0, bg=beige)
playerImageFrame.pack(expand=True, fill='none') 



# Frame holding Player Title and Player Label
playerInfoFrame = Frame(playerFrame, bg=gray)
playerInfoFrame.grid(row=0, column=0, sticky='nsew')

# CENTRAL CIRCULAR FRAME
# Number Label Background Image
backgroundFrame = Frame(content, bg=beige, width=200, height=200)
backgroundFrame.grid(column=1, row=0, sticky='ew')

# Bring in the number's circular frame graphic
backgroundImagePath = "images/NumberGraphic.png"
backgroundImage = Image.open(backgroundImagePath)
backgroundImage = backgroundImage.resize((135, 135), Image.LANCZOS)
backgroundImageTked = ImageTk.PhotoImage(backgroundImage)

# Pack it into a label and then into the frame supposed to hold the number and it
backgroundLabel=Label(backgroundFrame, image=backgroundImageTked)
backgroundLabel.pack(expand=True, fill='both') 
backgroundLabel.config(bg=beige)

# GAME NUMBER IN THE CENTER
# Number Label
numberLabel = Label(
    content, 
    text="0",
    font=("Kalam", 30, "bold"), 
    bg=beige,
    foreground=orange
)

# Set the positions of the elements in the content area
aiImageFrame.grid(column=0, row=0, padx=(10, 10), pady=(90, 10))

aiFrame.grid(column=0, row=0, padx=(10, 10), pady=(10, 10))
numberLabel.grid(column=1, row=0, padx=0)
playerFrame.grid(column=0, row=0, padx=(10, 10), pady=(10, 10))

# Configure the grid weights for content
content.grid_columnconfigure(0, weight=1)
content.grid_columnconfigure(1, weight=1)
content.grid_columnconfigure(2, weight=1)
content.grid_rowconfigure(0, weight=1)
content.grid_rowconfigure(2, weight=1) 

# sets content in aiFrame and playerFrame
# AI title and score
aiTitle = Label(
    AIInfoFrame, 
    text="AI", 
    font=("Kalam", 50, "bold"),
    padx=100,
    bg=gray,
    fg=black
)

aiScore = StringVar()
aiLabel = Label(
    AIInfoFrame, 
    textvariable=aiScore,
    font=("Kalam", 50, "bold"),
    padx=40,
    bg=red,
    fg=beige
)

aiLabel['textvariable'] = aiScore
aiScore.set("0")

# Player title and score 
playerTitle = Label(
    playerInfoFrame, 
    text="PLAYER", 
    font=("Kalam", 50, "bold"),
    padx=0,
    bg=gray,
    fg=black
)

playerScore = StringVar()

playerLabel = Label(
    playerInfoFrame, 
    textvariable=playerScore,
    font=("Kalam", 50, "bold"),
    padx=40,
    bg=green,
    fg=beige
)

playerLabel['textvariable'] = playerScore
playerScore.set("0")

playerTitle.grid(row=0, column=0, sticky='w', padx=50, pady=10)
playerLabel.grid(row=0, column=1, sticky='e', padx=30, pady=10)

# Set the positions of the ai and player content in their respective frames
aiTitle.grid(row=0, column=0, sticky='w', padx=50, pady=10)
aiLabel.grid(row=0, column=1, sticky='e', padx=30, pady=10)

# Grid layout for the player's title and score
playerTitle.grid(
    column=0, 
    row=0, 
    sticky='nsew', 
    padx=50,
    pady=10
)

playerLabel.grid(
    column=1, 
    row=0, 
    sticky='e', 
    padx=30,
    pady=10,
)


aiFrame.grid_columnconfigure(0, weight=1)
playerFrame.grid_columnconfigure(0, weight=1)

webcam = WebcamAI(playerImageFrame, winnerText, aiImageLabel, aiScore, playerScore)

# countdown
numberCount = StringVar()
numberLabel['textvariable'] = numberCount
numberCount.set(f"{webcam.countdown_display}")  # Sets the countdown of the "rock paper scissor" beat
numberLabel.place(relx=0.5, rely=0.42, anchor='center')

#button for starting the game
startButton = ttk.Button(content, text='START', style='TButton', command=webcam.button_press)
startButton.grid(row=1, column=2, pady=(10, 20))

#makes the button unclickable after being clicked
def disable_button():
    startButton.state(['disabled'])
    startButton.configure(style='Disabled.TButton')

startButton.config(command=lambda: [disable_button(), webcam.button_press()])

buttonStyle = ttk.Style()
buttonStyle.configure('TButton', background=blue, foreground=blue, font=("Kalam", 20, "bold"), highlightbackground=blue, activebackground = blue)
buttonStyle.map('TButton', background=[('disabled', gray)], foreground=[('disabled', gray)])
buttonStyle.configure('Disabled.TButton', background=gray, foreground=gray, font=("Kalam", 20, "bold"))

root.mainloop()
