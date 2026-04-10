from tkinter import *
from tkinter.messagebox import *
from PIL import Image, ImageTk
import tkinter.ttk as ttk
import numpy as np
import cv2

class ColorFilterApp(Tk):
    def __init__(self):
        super().__init__()

        width, height = 700, 467
        x, y = (self.winfo_screenwidth() // 2) - (width // 2), (self.winfo_screenheight() // 2) - (height // 2)

        self.title("Filter App")
        self.geometry(f"{width}x{height}+{x}+{y}")
        self.resizable(False, False)
        self.add_widgets()

    def add_widgets(self):
        self.app_title = ttk.Label(self, text="Color Filter App", font=["Segoe UI Variable Display", 20, "bold"])
        self.app_title.pack(pady=14)

if __name__ == "__main__":
    app = ColorFilterApp()
    app.mainloop()