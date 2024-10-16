# im so sorry i just forgot this needed to professional and sweared in the commit so committing again
# LMFAO
# Imports
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter.font import Font

# Create the main menu and initialize the very cool name
root = Tk()
root.title("Rock, Paper, AI Sensors")

# Color Palette (based off the illustration)
beige = "#e2d5d5"
blue = "#5582c4"
red = "#c05953"
green = "#72c68a"
black = "#393845"
gray = "#9d8c89"
orange = "#c58955"
yellow = "#f7d559"

# Configure the main window's grid and its border
root.grid_rowconfigure(0, weight=0)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
root.config(bg=beige, highlightthickness=13, highlightbackground=blue, highlightcolor=blue)

# automatically fullscreens it
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

# Title on the top of the screen configuration
label = Label(
    root,
    text="ROCK, PAPER, AI SENSORS",
    font=("Kalam", 60, "bold"),
    foreground=black,
    bg=beige
)
label.grid(column=0, row=0, pady=(40, 10))

content = Frame(root, bg=beige)
content.grid(row=1, column=0, sticky='nsew')

#below is used to get specific coords of the mouse click so I know where to place things!
# Create a Canvas widget
canvas = Canvas(content, width=5, bg=beige, highlightthickness=0)
canvas.grid(row=0, column=1, sticky='ns')
# Function to print coordinates on click
def print_coords(event):
    print(f"Clicked at: ({event.x}, {event.y})")
# Bind left mouse click to print_coords function
canvas.bind("<Button-1>", print_coords)

# Draw a dashed line on the Canvas
canvas.create_line(2, -10, 2, 670, fill=orange, width=10, dash=(50, 1))

# Set the content of what's going to be in the grid
# AI Frame
outerAIFrame = Frame(
    content, 
    borderwidth=5, 
    bg=gray
)  
outerAIFrame.grid(column=0, row=0, padx=(20, 20), pady=20)

aiFrame = Frame(
    outerAIFrame, 
    borderwidth=1, 
    relief="ridge", 
    width=550, 
    height=600,
    bg=beige
)

aiFrame['borderwidth'] = 0
aiFrame['relief'] = 'solid'
aiFrame.grid_propagate(False)

# Frame holding AI Title and AI Label
AIInfoFrame = Frame(aiFrame, bg=gray)
AIInfoFrame.grid(row=0, column=0, sticky='nsew')

# Player Frame
outerPlayerFrame = Frame(
    content, 
    borderwidth=5, 
    bg=gray
)  
outerPlayerFrame.grid(column=2, row=0, padx=(20, 20), pady=20)

playerFrame = Frame(
    outerPlayerFrame,
    borderwidth=5, 
    relief="ridge", 
    width=550, 
    height=600,
    bg=beige,
)
playerFrame['borderwidth'] = 0
playerFrame['relief'] = 'solid'
playerFrame.grid_propagate(False)

# Frame holding Player Title and Player Label
playerInfoFrame = Frame(playerFrame, bg=gray)
playerInfoFrame.grid(row=0, column=0, sticky='nsew')

# Number Label Background Image
# ignore the test image for now,,,,
backgroundFrame = Frame(content, bg=beige, width=200, height=200)
backgroundFrame.grid(column=1, row=0, sticky='ew')

backgroundImagePath = "images/NumberGraphic.png"
backgroundImage = Image.open(backgroundImagePath)
backgroundImage = backgroundImage.resize((135, 135), Image.LANCZOS)
backgroundImageTked = ImageTk.PhotoImage(backgroundImage)

backgroundLabel=Label(backgroundFrame, image=backgroundImageTked)
backgroundLabel.pack(expand=True, fill='both') 
backgroundLabel.config(bg=beige)

# Number Label
numberLabel = Label(
    content, 
    text="0",
    font=("Kalam", 30, "bold"), 
    bg=beige,
    foreground=orange
)
numberCount = StringVar()
numberLabel['textvariable'] = numberCount
numberCount.set("2")  # Sets the count of the "rock paper scissor" beat
numberLabel.place(relx=0.5, rely=0.5, anchor='center')

# Set the positions of the elements in the content area
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


root.mainloop()