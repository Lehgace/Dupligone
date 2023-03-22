# Joshua Erickson | CPSC 491 | Dupligone GUI Homescreen Test using CustomTkinter

import customtkinter as ctk
#import os
#from PIL import Image # for use with displaying images

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
        for F in (HomePage, UploadPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("HomePage") # call function to raise a chosen frame so it is visible

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

class HomePage(ctk.CTkFrame):

    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent) 
        self.controller = controller

        self.controller.title('Dupligone Home')
        self.controller.state('zoomed') # purpose unclear atm?

        heading_label = ctk.CTkLabel(self,
                                                     text='Dupligone!',
                                                     font=('Roboto',45,'bold'),
                                                     )
        heading_label.pack(pady=25)

        # Get Started Function - Progress to File Upload Page. Text placeholder
        def getStarted():
            print("Get Started Now == Pressed")
            controller.show_frame('UploadPage')     

        # edit start button and overhaul page
        start_button = ctk.CTkButton(self,
                                                     text='Get Started Now!',
                                                     command=getStarted,
                                                     border_width = 3,
                                                     width=40,
                                                     height=3)
        start_button.pack(pady=10)

        incorrect_password_label = ctk.CTkLabel(self,
                                                                        text='',
                                                                        font=('orbitron',13),
                                                                        anchor='n')
        incorrect_password_label.pack(fill='both',expand=True)

        bottom_frame = ctk.CTkFrame(self,border_width=3)
        bottom_frame.pack(fill='x',side='bottom')
        
class UploadPage(ctk.CTkFrame):

    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller
   
        heading_label = ctk.CTkLabel(self,
                                                     text='SECURITEX ATM',
                                                     font=('orbitron',45,'bold'))
        heading_label.pack(pady=25)

        main_menu_label = ctk.CTkLabel(self,
                                                           text='Main Menu',
                                                           font=('orbitron',13))
        main_menu_label.pack()

        selection_label = ctk.CTkLabel(self,
                                                           text='Please make a selection',
                                                           font=('orbitron',13),
                                                           anchor='w')
        selection_label.pack(fill='x')

        button_frame = ctk.CTkFrame(self)
        button_frame.pack(fill='both',expand=True)

        def withdraw():
            controller.show_frame('WithdrawPage')
            
        withdraw_button = ctk.CTkButton(button_frame,
                                                            text='Withdraw',
                                                            command=withdraw,
                                                            border_width=3,
                                                            width=50,
                                                            height=5)
        withdraw_button.grid(row=0,column=0,pady=5)

        def deposit():
            controller.show_frame('DepositPage')
            
        deposit_button = ctk.CTkButton(button_frame,
                                                            text='Deposit',
                                                            command=deposit,
                                                            border_width=3,
                                                            width=50,
                                                            height=5)
        deposit_button.grid(row=1,column=0,pady=5)

        def balance():
            controller.show_frame('BalancePage')
            
        balance_button = ctk.CTkButton(button_frame,
                                                            text='Balance',
                                                            command=balance,
                                                            border_width=3,
                                                            width=50,
                                                            height=5)
        balance_button.grid(row=2,column=0,pady=5)

        def exit():
            controller.show_frame('HomePage')
            
        exit_button = ctk.CTkButton(button_frame,
                                                            text='Exit',
                                                            command=exit,
                                                            border_width=3,
                                                            width=50,
                                                            height=5)
        exit_button.grid(row=3,column=0,pady=5)


        bottom_frame = ctk.CTkFrame(self,border_width=3)
        bottom_frame.pack(fill='x',side='bottom')


if __name__ == "__main__":
    app = InitApp()
    app.mainloop()
