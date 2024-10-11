from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Rock, Paper, AI Sensors")

# Configure the main window's grid
root.grid_rowconfigure(0, weight=0)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

# Title on the top of the screen
label = ttk.Label(root, text="Rock, Paper, AI Sensors", font=("Arial", 50))
label.grid(column=0, row=0, pady=(40, 10))

content = ttk.Frame(root)
content.grid(row=1, column=0, sticky='nsew')

# Set the content of what's going to be in the grid
aiFrame = ttk.Frame(content, borderwidth=5, relief="ridge", width=600, height=600)
aiFrame['borderwidth'] = 7
aiFrame['relief'] = 'solid'
aiFrame.grid_propagate(False)

playerFrame = ttk.Frame(content, borderwidth=5, relief="ridge", width=600, height=600)
playerFrame['borderwidth'] = 7
playerFrame['relief'] = 'solid'
playerFrame.grid_propagate(False)

numberLabel = ttk.Label(content, text="0",font=("Arial", 30))
numberCount = StringVar()
numberLabel['textvariable'] = numberCount
numberCount.set("2")  # Sets the count of the "rock paper scissor" beat

# Set the positions of the elements in the content area
aiFrame.grid(column=0, row=0, padx=(20, 0), pady=20)
numberLabel.grid(column=1, row=0, padx=0)
playerFrame.grid(column=2, row=0, padx=(0, 20), pady=20)

# Configure the grid weights for content
content.grid_columnconfigure(0, weight=1)
content.grid_columnconfigure(1, weight=1)
content.grid_columnconfigure(2, weight=1)
content.grid_rowconfigure(0, weight=1)

# sets content in aiFrame and playerFrame
aiTitle = ttk.Label(aiFrame, text="AI", font=("Arial", 30))

aiScore = StringVar()
aiLabel = ttk.Label(aiFrame, textvariable=aiScore,font=("Arial", 30))
aiLabel['textvariable'] = aiScore
aiScore.set("0")

playerTitle = ttk.Label(playerFrame, text="PLAYER", font=("Arial", 30))

playerScore = StringVar()
playerLabel = ttk.Label(playerFrame, textvariable=playerScore,font=("Arial", 30))
playerLabel['textvariable'] = playerScore
playerScore.set("0")

# Set the positions of the ai and player content in their respective frames
aiTitle.grid(column=0, row=0, columnspan=1, sticky='nsew', padx=50)
aiLabel.grid(column=1, row=0, columnspan=1, sticky='e', padx=30)
aiFrame.grid_columnconfigure(0, weight=1)

playerTitle.grid(column=0, row=0, sticky='nsew', padx=50)
playerLabel.grid(column=1, row=0, sticky='e', padx=30)
playerFrame.grid_columnconfigure(0, weight=1)

root.mainloop()
