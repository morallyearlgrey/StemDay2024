# for the cool camera stuff
import cv2
import os
from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()

# camera stuff
class webcam:
    def __init__(self, window):
        self.window = window
        self.window.title("Player")
        self.video_capture = cv2.VideoCapture(1)
        self.current_image = None
        self.canvas = tk.Canvas(window, width=640, height=640)
        self.canvas.pack()
        self.update_webcam()

    def update_webcam(self):
        ret, frame = self.video_capture.read()

        if ret:
            self.current_image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            self.photo = ImageTk.PhotoImage(image=self.current_image)
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)
            self.window.after(15, self.update_webcam)


app = webcam(root)

root.mainloop()