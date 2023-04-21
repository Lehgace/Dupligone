# Joshua Erickson | CPSC 491 | Dupligone GUI Homescreen Test using CustomTkinter

import customtkinter as ctk
from base2test import interfaceSearch, uploadedFiles
#import os
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
        left_frame = ctk.CTkScrollableFrame(self, border_width=1)
        left_frame.pack(fill='both',side='left', expand=True, padx=10, pady=10)

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
        test_output.rowconfigure(0, weight=3)
        test_output.grid(row=0,column=0,pady=5,padx=5)

        # Frame for right box (Image Preview Window)
        right_frame = ctk.CTkFrame(self,border_width=1)
        right_frame.pack(fill="both", side='left', expand=True, padx=10, pady=10)

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
        #exit_button.pack(side='bottom')
        exit_button.grid(row=0,column=1,pady=5,padx=5)

if __name__ == "__main__":
    app = InitApp()
    app.mainloop()
