from tkinter import *
from functools import partial #for removing window
import random


class Converter:
    def __init__(self, parent):

        # Bkg Variable
        bkg_colour = "#9fe5d9"

        # Main Window
        self.converter_frame = Frame(width=400, height=300, bg=bkg_colour, padx=10, pady=30)
        
        self.converter_frame.grid()
        
        # Temp Conv. Heading
        self.temp_converter_label = Label(self.converter_frame, text="Temperature Converter", font=("Arial 18 bold"), bg=bkg_colour, padx=10, pady=10)
       
        self.temp_converter_label.grid(row=0)

        #Help button
        self.help_button = Button(self.converter_frame, text="Help", padx=10, pady=10, command=self.help)
        self.help_button.grid(row=1)
        
        #what that button do
    def help(self):  
        print("help")
        get_help = Help(self)
        get_help.help_text.configure(text="Help text")

class Help: 
    def __init__(self, partner): 

        #background colour
        bkg_colour= "#9fe5d9"

        #Button off
        partner.help_button.config(state=DISABLED)

        #opens a new window
        self.help_box = Toplevel()

        #GUI Frame
        self.help_frame = Frame(self.help_box, width=400, height=300, bg=bkg_colour, padx=10, pady=10)
        
        self.help_frame.grid()

        #Help Heading 0
        self.help_converter_label = Label(self.help_frame, text="How to Use", font=("Arial 13 bold"), bg=bkg_colour, padx=10, pady=10)
       
        self.help_converter_label.grid(row=0)

        #Help Text 1 
        self.help_text = Label(self.help_frame, text="", justify=LEFT, width=40, bg=bkg_colour , wrap=250)
        self.help_text.grid(row=1)

        #Dismiss button 2 
        self.dismiss_button = Button(self.help_frame, text="Exit", width=10, command=partial(self.close_button, partner))
        self.dismiss_button.grid(row=2,pady=10)
    
    #close help function
    def close_button(self, partner):
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()



# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter(root)
    root.mainloop()
