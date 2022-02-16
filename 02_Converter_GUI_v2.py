from tkinter import * 
from functools import partial #for removing window
import random

class Converter:
    def __init__(self, parent):

        #light cyan
        bkg_colour = "#9fe5d9"

        # frame
        self.converter_frame = Frame(width=400, height=300, bg=bkg_colour, padx=10, pady=10)
        self.converter_frame.grid()
        
        # Heading
        self.converter_label = Label(self.converter_frame, text="Temperature Converter", font=("Arial 18 bold"), bg=bkg_colour, padx=10, pady=30)
        self.converter_label.grid(row=1)
        
        # User information/Instructions
        self.user_i = Label(self.converter_frame, text="User Information", wrap=250, justify=LEFT, bg=bkg_colour, padx=10, pady=10)
        self.user_i.grid(row=2)

        # Temper input box
        self.input_box = Entry(self.converter_frame, width=20, font="Arial 14 bold")
        self.input_box.grid(row=4)
       
        #button frame
        self.conv_button_frame = Frame(self.converter_frame, bg=bkg_colour)
        self.conv_button_frame.grid(row=5, pady=10)

        #Centigrade button
        self.conv_c_button = Button(self.conv_button_frame, text="Centigrade", command=lambda: self.temp_convert(-459))
        self.conv_c_button.grid(row=0, column=0, padx=5)

        #F Button
        self.conv_f_button = Button(self.conv_button_frame, text="Fahrenheit", command=lambda: self.temp_convert(-273))
        self.conv_f_button.grid(row=0, column=1, padx=5)

        #Conv label
        self.conversion_outcome = Label(self.converter_frame, text="Conversion", font="Arial 14", wrap=250, justify=LEFT, bg=bkg_colour, padx=30, pady=30)
        self.conversion_outcome.grid(row=7)

        #help and calc his buttons
        self.hc_button_frame = Frame(self.converter_frame, bg=bkg_colour)
        self.hc_button_frame.grid(row=10, pady=10)

        #calc historuy button
        self.calch_button = Button(self.hc_button_frame, text="Calculation History", width=15)
        self.calch_button.grid(row=0, column=0, padx=5)

        # help Button
        self.help_button = Button(self.hc_button_frame, text="Help", width=5, command=self.help)
        self.help_button.grid(row=0, column=1, padx=5)

    def help(self):  
        print("help")
        get_help = Help(self)
        get_help.help_text.configure(text="Help text")

    def temp_convert(self,to): 
        print(to)

        error= "#F3B6B6"

        to_convert = self.input_box.get()
        
        try:
            to_convert = float(to_convert)
            print("your brain is large")

        except ValueError: 
            self.conversion_outcome.configure(text="Please enter a number", font="Arial 14", fg="#CE1B1B")
            self.input_box.configure(bg=error)


class Help: 
    def __init__(self, partner): 

        #background colour
        bkg_colour= "#4cb4e0"

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