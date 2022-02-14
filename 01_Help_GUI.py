from tkinter import *
import random


class Converter:
    def __init__(self, parent):

        # Bkg Variable
        bkg_colour = "#9fe5d9"

        # Main Window
        self.converter_frame = Frame(width=400, height=300, bg=bkg_colour, padx=10, pady=10)
        
        self.converter_frame.grid()
        
        # Temp Conv. Heading
        self.temp_converter_label = Label(self.converter_frame, text="Temperature Converter", font=("Gill Sans Nova", "18", "bold"), bg=bkg_colour, padx=10, pady=10)
       
        self.temp_converter_label.grid(row=0)

        #Help button
        self.help_button = Button(self.converter_frame, text="Help", padx=10, pady=10, command=self.help)
        self.help_button.grid(row=1)
        
        #what that button do
    def help(self):  
        print("Ayo")
        get_help = Help(self)
        get_help.help_text.configure(text="Help text")

class Help: 
    def __init__(self, partner): 

        #background colour
        bkg_colour= "#9fe5d9"

        #Button off
        partner.help_button.config(state=DISABLED)

        #GUI Frame
        self.help_frame = Frame(width=400, height=300, bg=bkg_colour, padx=10, pady=10)
        
        self.help_frame.grid()

        #Help Heading 0
        self.help_converter_label = Label(self.help_frame, text="Information", font=("Gill Sans Nova", "13", "bold"), bg=bkg_colour, padx=10, pady=10)
       
        self.help_converter_label.grid(row=0)

        #Help Text 1 
        self.help_text = Label(self.help_frame, text="", justify=LEFT, width=40. bg=background, wrap=250)
        self.help_text.grid(column=0, row=1)

        #Dismiss button 2 




# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter(root)
    root.mainloop()
