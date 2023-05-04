# Joshua Erickson | CPSC 491 | Dupligone GUI Homescreen Test using CustomTkinter

import customtkinter as ctk
import os
from PIL import Image # for use with displaying images

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Dupligone")
        self.geometry("1280x720")

        # Set Dark Mode Default Appearance
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        # Get Started Function - Progress to File Upload Page. Text placeholder
        def getStarted():
            print("Get Started Now == Pressed")

        # set grid layout 1x1
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # load images
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "Assets")
        self.logo_image = ctk.CTkImage(Image.open(os.path.join(image_path, "magnifyicon.png")), size=(26, 26))
        self.instructions_image = ctk.CTkImage(Image.open(os.path.join(image_path, "testall.png")), size=(600, 200))

        # Set up home frame
        self.home_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)

        # Dupligone logo label
        dup_label = ctk.CTkLabel(self, text="Dupligone!", font=("Roboto", 36))
        dup_label.pack(pady=12, padx=10)

        # Home Screen Description 1
        description_1 = ctk.CTkLabel(self, text="Dupligone! automagically searches folders for copies or duplicates of photos.", font=("Roboto", 24))
        description_1.pack(pady=12, padx=10)
        # Home Screen Description 2
        description_2 = ctk.CTkLabel(self, text="Using Dupligone! is as simple as...", font=("Roboto", 24))
        description_2.pack(pady=12, padx=10)

        # Import instructional image placeholder
        instr_image = ctk.CTkImage(Image.open(r"C:\Users\theun\OneDrive\Documents\Dupligone\Assets\testall.png"), size=(600,200))
        # Home Screen Instructionbox Button
        instr_button = ctk.CTkButton(self, image=instr_image, width=600, height=200, text='', fg_color="transparent", hover=False)
        instr_button.pack(pady=12, padx=10)

        # Get Started Now Button
        button = ctk.CTkButton(self, text="Get Started Now!", font=("Roboto", 24), command=getStarted)
        button.pack(pady=12, padx=10)

if __name__ == "__main__":
    app = App()
    app.mainloop()