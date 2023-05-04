# Joshua Erickson | CPSC 491 | Dupligone GUI Homescreen Test using CustomTkinter

import customtkinter as ctk
from base2test import interfaceSearch, uploadedFiles
import os
from PIL import Image # for use with displaying images

# Initialize Desktop Application
class InitApp(ctk.CTk):

    def __init__(self, *args, **kwargs):
        ctk.CTk.__init__(self, *args, **kwargs)

        # Initialize title and size of start-up window
        self.title("Dupligone Init") #theoretically shouldn't ever see this : if frame missing title
        self.geometry("1280x720")

        # Set Dark Mode Default Appearance
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")
        
        # Set up container to store frames/pages
        container = ctk.CTkFrame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (HomePage, UploadPage, SearchPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # top one in stacking order will be visible
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("HomePage") # call function to raise a chosen frame so it is visible

    # Function that raises frame for inputed page_name
    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

# Home Page: will show instructions and button to proceed to file upload
class HomePage(ctk.CTkFrame):

    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent) 
        self.controller = controller

        # Set title and state of Window
        self.controller.title('Dupligone!')
        self.controller.state('zoomed')

        heading_label = ctk.CTkLabel(self,
                                                     text='Dupligone!',
                                                     font=('Roboto',45,'bold'),
                                                     )
        heading_label.pack(pady=25)

        # Home Screen Description 1
        description_1 = ctk.CTkLabel(self, text="Dupligone! automagically searches folders for copies or duplicates of photos.", font=("Roboto", 24))
        description_1.pack(pady=25)
        # Home Screen Description 2
        description_2 = ctk.CTkLabel(self, text="Using Dupligone! is as simple as...", font=("Roboto", 24))
        description_2.pack(pady=25)
        
        # Import instructional image placeholder
        instr_image = ctk.CTkImage(Image.open(r"C:\Users\theun\OneDrive\Documents\Dupligone\Assets\testall.png"), size=(657,213))
        # Home Screen Instructionbox Button
        instr_button = ctk.CTkButton(self, image=instr_image, width=657, height=213, text='', fg_color="transparent", hover=False)
        instr_button.pack(pady=25)
        
        # Get Started Function - Progress to File Upload Page.
        def getStarted():
            print("Get Started Now == Pressed")
            controller.show_frame('UploadPage')     

        # edit start button and overhaul page
        start_button = ctk.CTkButton(self,
                                     text='Get Started Now!',
                                     font=("Roboto", 24,'bold'),
                                     command=getStarted,
                                     )
        start_button.pack(pady=10)


# Page for browsing folders and uploading files to workspace        
class UploadPage(ctk.CTkFrame):
    # end goal: page split into two sections (boxes). Left box contains browse folder button, right box contains preview of uploaded filepaths
        # may need to implement function that shows browse folders

    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller

        # Header Label for Dupligone Logo
        heading_label = ctk.CTkLabel(self,
                                     text='Dupligone!',
                                     font=('Roboto',45,'bold'))
        heading_label.pack(pady=25)
        # Sub Header Label for page description
        main_menu_label = ctk.CTkLabel(self,
                                       text='Upload Content to Workspace',
                                       font=('Roboto',20))
        main_menu_label.pack()


        # Frame for left box
        left_frame = ctk.CTkFrame(self,border_width=3)
        left_frame.pack(fill="both", side='left', expand=True, padx=70, pady=140)

        # Function for Browse button to prompt user to upload files
        def pressedBrowse():
            print("pressedBrowse == pressed")
            upload_test = []
            upload_test = uploadedFiles(upload_test)
            right_frame.configure(state="normal") # enable editing state of text box
            for element in upload_test:
                right_frame.insert("end", element)
                right_frame.insert("end", "\n")
            right_frame.configure(state="disabled") # enable editing state of text box

        search_button = ctk.CTkButton(left_frame,
                                      text='Browse',
                                      font=('Roboto',20),
                                      command=pressedBrowse)
        search_button.pack(side='bottom', pady=25)

        # Textbox Frame for right box
        right_frame = ctk.CTkTextbox(self,border_width=3, state="disabled", font=('Roboto',16))
        right_frame.pack(fill="both", side='right', expand=True, padx=70, pady=140)

        # Function for Exit button to return to homepage
        def exit():
            controller.show_frame('HomePage')
            print("Exit button pressed, returning to homepage")
        # Create Exit button    
        exit_button = ctk.CTkButton(self,
                                    text='Exit',
                                    font=('Roboto',15),
                                    command=exit)
        exit_button.pack(side='bottom', pady=10)
        
        # Function for Search button to progress to search results page
        def gotoSearch():
            controller.show_frame('SearchPage')
            print("Search button pressed, moving to SearchPage")
        # Create search page button
        goto_search_button = ctk.CTkButton(self,
                                    text='Begin Search',
                                    font=('Roboto',30),
                                    command=gotoSearch
                                    )
        goto_search_button.pack(side='bottom', pady=10, ipadx=2, ipady=2)

        
# Page for searching folders uploaded to workspace        
class SearchPage(ctk.CTkFrame):
    # Overhaul Layout to Look closer to design concept 

    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller

        # Header Label for Dupligone Logo
        heading_label = ctk.CTkLabel(self,
                                     text='Dupligone!',
                                     font=('Roboto',45,'bold'))
        heading_label.pack(pady=25)

        # header frame for top labels
        header_frame = ctk.CTkFrame(self,fg_color="transparent")
        header_frame.pack(fill="x", side='top', padx=5, pady=5)

        duplicates_label = ctk.CTkLabel(header_frame,
                                       text='Duplicates',
                                       font=('Roboto',22, 'bold'))
        duplicates_label.pack(fill="x",side='left',padx=200)
        image_preview_label = ctk.CTkLabel(header_frame,
                                       text='Image Preview',
                                       font=('Roboto',22, 'bold'))
        image_preview_label.pack(fill="x",side='right',padx=200)
        
        # Frame for bottom buttons box
        bottom_frame = ctk.CTkFrame(self,border_width=2)
        bottom_frame.pack(fill="x", side='bottom', padx=5, pady=5)

        # Frame for Left Side (Duplicate Viewer Window)
        left_frame = ctk.CTkScrollableFrame(self, border_width=1, width=600, height=500)
        left_frame.pack(fill='both',side='left', padx=10, pady=10)

        # Debugging function that prints the duplicates found to textbox (filepath, filename)
        def testSearch():
            print("Test Search == pressed")
            found_images_dict, found_filepaths_dict = interfaceSearch()
            
            #print(found_images_dict)
            for key, value in found_images_dict.items():
                print(key, " : ", value)

            test_output.configure(state="normal") # enable editing state of text box
            for value in found_filepaths_dict:
                # Test Skeletal Code for displaying the images
                # current_image = ctk.CTkImage(Image.open(r"[filepath]"), size=(100,100))
                print(found_filepaths_dict[value])
                test_output.insert("end", found_filepaths_dict[value])
                test_output.insert("end", "\n\n")
            test_output.configure(state="disabled") # disable editing state after finished writing results
            # to-fix note: if user exits page after text insertion, text remains when visiting the page again

        # Textbox for debugging display purposes
        test_output = ctk.CTkTextbox(left_frame, state="disabled")
        test_output.grid(row=0,column=0,columnspan=4,pady=5,padx=5)

        # Function to call for image preview
        def show_in_preview(image, text):
            print("Image has been clicked")
            preview_image_button.configure(image=image, text=text)


        # Declarations for image previews
        preview_image = ctk.CTkImage(Image.open(r"C:\Users\theun\OneDrive\Documents\Dupligone\TestImages\AC2.jpg"), size=(500,350))
        preview_image2 = ctk.CTkImage(Image.open(r"C:\Users\theun\OneDrive\Documents\Dupligone\TestImages\K3P.png"), size=(500,350))
        preview_image3 = ctk.CTkImage(Image.open(r"C:\Users\theun\OneDrive\Documents\Dupligone\TestImages\R2.png"), size=(500,350))
        preview_image4 = ctk.CTkImage(Image.open(r"C:\Users\theun\OneDrive\Documents\Dupligone\TestImages\Subfolder1\B2.jpg"), size=(500,350))
        preview_image5 = ctk.CTkImage(Image.open(r"C:\Users\theun\OneDrive\Documents\Dupligone\TestImages\Subfolder2\D2.jpg"), size=(500,350))

        # Prototype loading images    
        test_image = ctk.CTkImage(Image.open(r"C:\Users\theun\OneDrive\Documents\Dupligone\TestImages\AC2.jpg"), size=(100,100))
        test_image_button = ctk.CTkButton(left_frame, image=test_image, width=100, height=100, text='AC2.jpg', font=('Roboto',15), compound="top", fg_color="transparent", hover=True)
        test_image_button.configure(command=lambda: show_in_preview(preview_image, test_image_button.cget("text")))
        test_image_button.grid(row=1,column=0,pady=5,padx=5)
        test_image2 = ctk.CTkImage(Image.open(r"C:\Users\theun\OneDrive\Documents\Dupligone\TestImages\K3P.png"), size=(100,100))
        test_image2_button = ctk.CTkButton(left_frame, image=test_image2, width=100, height=100, text='K3P.png', font=('Roboto',15), compound="top", fg_color="transparent", hover=True)
        test_image2_button.configure(command=lambda: show_in_preview(preview_image2, test_image2_button.cget("text")))
        test_image2_button.grid(row=1,column=1,pady=5,padx=5)
        test_image3 = ctk.CTkImage(Image.open(r"C:\Users\theun\OneDrive\Documents\Dupligone\TestImages\R2.png"), size=(100,100))
        test_image3_button = ctk.CTkButton(left_frame, image=test_image3, width=100, height=100, text='R2.png', font=('Roboto',15), compound="top", fg_color="transparent", hover=True)
        test_image3_button.configure(command=lambda: show_in_preview(preview_image3, test_image3_button.cget("text")))
        test_image3_button.grid(row=1,column=2,pady=5,padx=5)
        test_image4 = ctk.CTkImage(Image.open(r"C:\Users\theun\OneDrive\Documents\Dupligone\TestImages\Subfolder1\B2.jpg"), size=(100,100))
        test_image4_button = ctk.CTkButton(left_frame, image=test_image4, width=100, height=100, text='B2.jpg', font=('Roboto',15), compound="top", fg_color="transparent", hover=True)
        test_image4_button.configure(command=lambda: show_in_preview(preview_image4, test_image4_button.cget("text")))
        test_image4_button.grid(row=1,column=3,pady=5,padx=5)
        test_image5 = ctk.CTkImage(Image.open(r"C:\Users\theun\OneDrive\Documents\Dupligone\TestImages\Subfolder2\D2.jpg"), size=(100,100))
        test_image5_button = ctk.CTkButton(left_frame, image=test_image5, width=100, height=100, text='D2.jpg', font=('Roboto',15), compound="top", fg_color="transparent", hover=True)
        test_image5_button.configure(command=lambda: show_in_preview(preview_image5, test_image5_button.cget("text")))
        test_image5_button.grid(row=2,column=0,pady=5,padx=5)

        # Frame for right box (Image Preview Window)
        right_frame = ctk.CTkFrame(self,border_width=1, width=600, height=500)
        right_frame.pack(fill="both", side='left',  expand=True, padx=10, pady=10)

        # Function to call for image preview
        preview_image = ctk.CTkImage(Image.open(r"C:\Users\theun\OneDrive\Documents\Dupligone\TestImages\AC2.jpg"), size=(500,350))
        preview_image_button = ctk.CTkButton(right_frame, image=preview_image, width=500, height=350, text='AC2.jpg', font=('Roboto',15), compound="top", fg_color="transparent", hover=True)
        preview_image_button.grid(row=0,column=0,columnspan=4,pady=5,padx=5)
        
        # Function to delete image; tested with Image 5 D2.png
        def delete_image(file_path):
            #os.remove(file_path)
            print(file_path)
            print(f"{file_path} has been deleted")
            test_image5_button.grid_forget()


        #Top Level rename prototype; tested with K3P.png
        class RenameWindow(ctk.CTkToplevel):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.geometry("400x300")

                def submit_name():
                    new_name = self.entry.get()
                    print(new_name)
                    test_image2_button.configure(text=new_name)
                    self.deiconify()
                    
                self.entry = ctk.CTkEntry(self, placeholder_text="Enter new name")
                self.entry.pack(padx=20)
                self.submit_button = ctk.CTkButton(self, text="Submit", command=submit_name)
                self.submit_button.pack(padx=20)

         
        
        # Function to open top level window for rename
        def open_renamelevel(self):
            if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
                self.toplevel_window = RenameWindow(self)  # create window if its None or destroyed
            else:
                self.toplevel_window.focus()  # if window exists focus it

        #Top Level Compare Related prototype; tested with D1.png and D2.png
        class CompareWindow(ctk.CTkToplevel):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.geometry("1280x720")

                # Header Label for Dupligone Logo
                compare_head_label = ctk.CTkLabel(self,
                                     text='Preview',
                                     font=('Roboto',20,'bold'))
                compare_head_label.pack(pady=25)

                # Frame for Left Side (Duplicate Viewer Window)
                left_compare_frame = ctk.CTkFrame(self, border_width=1, width=600, height=500)
                left_compare_frame.pack(fill='both',side='left', expand=True, padx=10, pady=10)

                left_image = ctk.CTkImage(Image.open(r"C:\Users\theun\OneDrive\Documents\Dupligone\TestImages\AC1.jpg"), size=(500,350))
                left_image_button = ctk.CTkButton(left_compare_frame, image=left_image, width=500, height=350, text='AC1.jpg', font=('Roboto',15), compound="top", fg_color="transparent", hover=True)
                left_image_button.grid(row=0,column=0,columnspan=4,pady=5,padx=5)

                # Frame for right box (Image Preview Window)
                right_compare_frame = ctk.CTkFrame(self,border_width=1, width=600, height=500)
                right_compare_frame.pack(fill="both", side='left',  expand=True, padx=10, pady=10) 

                right_image = ctk.CTkImage(Image.open(r"C:\Users\theun\OneDrive\Documents\Dupligone\TestImages\AC2.jpg"), size=(500,350))
                right_image_button = ctk.CTkButton(right_compare_frame, image=right_image, width=500, height=350, text='AC2.jpg', font=('Roboto',15), compound="top", fg_color="transparent", hover=True)
                right_image_button.grid(row=0,column=0,columnspan=4,pady=5,padx=5)
                #self.entry = ctk.CTkEntry(self, placeholder_text="Enter new name")
                #self.entry.pack(padx=20)

        # Function to open top level window for compare related
        def open_comparelevel(self):
            if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
                self.toplevel_window = CompareWindow(self)  # create window if its None or destroyed
            else:
                self.toplevel_window.focus()  # if window exists focus it

        # Set no top level window active
        self.toplevel_window = None

        # delete, rename, move, compare related
        delete_button = ctk.CTkButton(right_frame, text='Delete', font=('Roboto',15), fg_color="#7E191B")
        delete_button.configure(command=lambda: delete_image(r"C:\Users\theun\OneDrive\Documents\Dupligone\TestImages\Subfolder2\D2.jpg")) # test to delete last image D2.png
        delete_button.grid(row=1,column=0,pady=5,padx=5)
        rename_button = ctk.CTkButton(right_frame, text='Rename', font=('Roboto',15))
        rename_button.configure(command=lambda: open_renamelevel(self))
        rename_button.grid(row=1,column=1,pady=5,padx=5)
        move_button = ctk.CTkButton(right_frame, text='Move', font=('Roboto',15))
        move_button.grid(row=1,column=2,pady=5,padx=5)
        compare_button = ctk.CTkButton(right_frame, text='Compare Related', font=('Roboto',15), fg_color="#1338BE")
        compare_button.configure(command=lambda: open_comparelevel(self))
        compare_button.grid(row=1,column=3,pady=5,padx=5)

        # Text button for search algo debugging
        search_button = ctk.CTkButton(bottom_frame,
                                      text='TestSearch',
                                      font=('Roboto', 15),
                                      command=testSearch)
        #search_button.pack(side='bottom')
        search_button.grid(row=0,column=0,pady=5,padx=5)

        # Exit function to return to homepage
        def exit():
            controller.show_frame('HomePage')
            print("Exit button pressed, returning to homepage")
            # to-do: prompt user if they are sure they wish to go to homepage, wipe any texts, images displayed from the page
            
        # Exit button 
        exit_button = ctk.CTkButton(bottom_frame,
                                    text='Exit',
                                    font=('Roboto', 15),
                                    command=exit)
        exit_button.grid(row=0,column=1,pady=5,padx=5)

if __name__ == "__main__":
    app = InitApp()
    app.mainloop()
