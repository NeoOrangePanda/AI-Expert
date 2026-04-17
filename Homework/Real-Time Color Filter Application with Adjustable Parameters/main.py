from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import *
from PIL import Image, ImageTk
import tkinter.ttk as ttk
import numpy as np
import time
import cv2

class ColorFilterApp(Tk):
    def __init__(self):
        super().__init__()

        width, height = 300, 550
        x, y = (self.winfo_screenwidth() // 2) - (width // 2), (self.winfo_screenheight() // 2) - (height // 2)

        self.font_name = "Segoe UI Variable Display"

        self.style = ttk.Style()
        self.style.configure("MyAppButton.TButton", font=(self.font_name, 11), padding=(20, 7, 20, 7))

        self.image = None
        self.copy_image = None
        self.preview_running = True

        self.title("Filter App")
        self.geometry(f"{width}x{height}+{x}+{y}")
        self.resizable(False, False)
        self.add_widgets()

    def reset_image_status(self):
        self.copy_image = self.image.copy()

    def red_tint(self): 
        self.reset_image_status()
        self.copy_image[:, :, 0] = 0
        self.copy_image[:, :, 1] = 0
    def blue_tint(self): 
        self.reset_image_status()
        self.copy_image[:, :, 1] = 0
        self.copy_image[:, :, 2] = 0
    def green_tint(self): 
        self.reset_image_status()
        self.copy_image[:, :, 0] = 0
        self.copy_image[:, :, 2] = 0

    def upload_image(self):
        upload_path = filedialog.askopenfilename(title="Select an image", filetypes=[
            ('Image Files', '*.png *.jpg *.jpeg')
        ])

        if not upload_path: return

        self.image = cv2.imread(upload_path)
        self.copy_image = self.image.copy()
        while True: self.start_preview()

    def save_image(self):
        save_path = filedialog.asksaveasfile(title="Save image", filetypes=[('Image Files', '*.png *.jpg *.jpeg')])
        if not save_path: return
        cv2.imwrite(save_path, self.copy_image)
        showinfo("File Saved!", f"Saved File at {save_path}")

    def start_preview(self):
        if self.image is None:
            return
        
        if not self.preview_running:
            self.preview_running = True
            self.update_preview()
    
    def update_preview(self):
        if self.copy_image is not None:
            cv2.imshow("LIVE PREVIEW - Color Filter App", self.copy_image)

        if self.preview_running:
            while True: 
                time.sleep(0.3)
                self.update_preview()

    def key(self, event):
        if event.char == "p":
            cv2.imshow("IMAGE PREVIEW - Color Filter App", self.copy_image)

    def add_widgets(self):
        self.app_title = ttk.Label(self, text="Color Filter App", font=[self.font_name, 20, "bold"])
        self.app_title.pack(pady=14)

        self.red_tint_button = ttk.Button(self, text="Red Tint", style="MyAppButton.TButton", width=23, command=lambda: self.red_tint()) 
        self.red_tint_button.pack()
        self.blue_tint_button = ttk.Button(self, text="Blue Tint", style="MyAppButton.TButton", width=23, command=lambda: self.blue_tint()) 
        self.blue_tint_button.pack(pady=10)
        self.green_tint_button = ttk.Button(self, text="Green Tint", style="MyAppButton.TButton", width=23, command=lambda: self.green_tint()) 
        self.green_tint_button.pack()

        self.sep_1 = ttk.Separator(self, orient='horizontal')
        self.sep_1.pack(fill='x', padx=25, pady=15)

        self.increase_red_button = ttk.Button(self, text="Increase Red", style="MyAppButton.TButton", width=23) 
        self.increase_red_button.pack()
        self.increase_blue_button = ttk.Button(self, text="Increase Blue", style="MyAppButton.TButton", width=23) 
        self.increase_blue_button.pack(pady=10)
        self.increase_green_button = ttk.Button(self, text="Increase Green", style="MyAppButton.TButton", width=23) 
        self.increase_green_button.pack()

        self.sep_2 = ttk.Separator(self, orient='horizontal')
        self.sep_2.pack(fill='x', padx=25, pady=15)
        
        self.upload_file_button = ttk.Button(self, text="Upload Image", style="MyAppButton.TButton", width=23, command=lambda: self.upload_image()) 
        self.upload_file_button.pack()
        self.save_file_button = ttk.Button(self, text="Save Image", style="MyAppButton.TButton", width=23, command=lambda: self.save_image()) 
        self.save_file_button.pack(pady=10)

        self.bind('<Key>', self.key)

if __name__ == "__main__":
    app = ColorFilterApp()
    app.mainloop()