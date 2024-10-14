# Imports
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

# Create the main menu and initialize the very cool name
root = Tk()
root.title("Rock, Paper, AI Sensors")

# Color Palette (based off the illustration)
beige = "#e3d4d7"
blue = "#5483c3"
red = "#c05851"
green = "#72c68a"
black = "#403139"
gray = "#9f8b8a"

# Configure the main window's grid and its border
root.grid_rowconfigure(0, weight=0)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
root.config(bg=beige, highlightthickness=10, highlightbackground=blue, highlightcolor=blue)

# Title on the top of the screen configuration
label = Label(
    root,
    text="ROCK, PAPER, AI SENSORS",
    font=("Kalam", 100),
    foreground=black,
    bg=beige

)
label.grid(column=0, row=0, pady=(40, 10))

content = Frame(root, bg=beige)
content.grid(row=1, column=0, sticky='nsew')

# i wanted to add the solid line here
solid_line = Frame(content, width=5, bg=black)
solid_line.grid(row=0, column=1, sticky='ns')

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

backgroundImagePath = "./StemDay2024/images/test-image.png"
backgroundImage = Image.open(backgroundImagePath)
backgroundImage = backgroundImage.resize((200, 200), Image.LANCZOS)
backgroundImageTked = ImageTk.PhotoImage(backgroundImage)

backgroundLabel=Label(backgroundFrame, image=backgroundImageTked)
backgroundLabel.pack(expand=True, fill='both') 

# Number Label
numberLabel = Label(
    content, 
    text="0",
    font=("Kalam", 30), 
    bg=beige,
    foreground=black
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
    font=("Kalam", 50),
    padx=100,
    bg=gray
)

aiScore = StringVar()
aiLabel = Label(
    AIInfoFrame, 
    textvariable=aiScore,
    font=("Kalam", 50),
    padx=40,
    bg=red
)

aiLabel['textvariable'] = aiScore
aiScore.set("0")

# Player title and score 
playerTitle = Label(
    playerInfoFrame, 
    text="PLAYER", 
    font=("Kalam", 50),
    padx=37,
    bg=gray
)

playerScore = StringVar()

playerLabel = Label(
    playerInfoFrame, 
    textvariable=playerScore,
    font=("Kalam", 50),
    padx=40,
    bg=green
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