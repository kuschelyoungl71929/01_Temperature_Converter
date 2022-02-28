from tkinter import * 
from functools import partial #for removing window
import random
import re

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
        self.conversion_outcome = Label(self.converter_frame, text="Conversion goes here", font="Arial 14", wrap=250, justify=LEFT, bg=bkg_colour, padx=30, pady=30)
        self.conversion_outcome.grid(row=7)

        #help and calc his buttons
        self.hc_button_frame = Frame(self.converter_frame, bg=bkg_colour)
        self.hc_button_frame.grid(row=10, pady=10)

        #calc history button
        self.calch_button = Button(self.hc_button_frame, text="Calculation History", width=15, command=self.history)
        self.calch_button.grid(row=0, column=0, padx=5)

        # help Button
        self.help_button = Button(self.hc_button_frame, text="Help", width=5, command=self.help)
        self.help_button.grid(row=0, column=1, padx=5) 

        # help command
    def help(self):  
        print("help")
        get_help = Help(self)
        get_help.help_text.configure(text="Help text")

    def history(self):
        print("history request")
        retrieve_history= history(self)
        retrieve_history.history_text.configure(text="History")
       
        #temp converter
    def temp_convert(self, low): 
        
        error= "#F3B6B6"

        to_convert = self.input_box.get()
        
        
        try:
            to_convert = float(to_convert)
            has_errors = "no"

            #fahrenheit
            if low == -273 and to_convert >= low:
                fahr = (to_convert * 9/5) + 32
                to_convert = self.rounding(to_convert)
                fahr = self.rounding(fahr)
                answer = "{} C° is {} F°".format(to_convert, fahr)
            #celsius
            elif low == -459 and to_convert >= low:
                cels = (to_convert - 32) * 5/9
                to_convert = self.rounding(to_convert)
                cels = self.rounding(cels)
                answer = "{} F° is {} C°".format(to_convert, cels)
            #too cold
            else :
                answer = "Too Cold"
                has_errors = "yes"

            if has_errors == "no":
                self.conversion_outcome.configure(text=answer, font="Arial 14", fg="black")
                self.input_box.configure(bg="white")
            else:
                self.conversion_outcome.configure(text=answer, font="Arial 14", fg="red")
                self.input_box.configure(bg=error)

        except ValueError: 
            self.conversion_outcome.configure(text="Please enter a number", font="Arial 14", fg="#CE1B1B")
            self.input_box.configure(bg=error)

    def rounding(self, to_round):
        if to_round%1 == 0:
            rounded = int(to_round)
        else:
            rounded = round(to_round, 1)

        return rounded

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

class history:
    def __init__(self, partner):

        #light cyan
        bkg_colour = "#9fe5d9"

        #opens a new window
        self.history_box = Toplevel()

        # frame
        self.history_frame = Frame(self.history_box, width=400, height=300, bg=bkg_colour, padx=10, pady=20)
        
        self.history_frame.grid()

        #history Heading 0
        self.history_converter_label = Label(self.history_frame, text="History", font=("Arial 13 bold"), bg="#9fe5d9", padx=10, pady=10)
       
        self.history_converter_label.grid(row=0)

     #retrieve full history button
        self.full_history = Button(self.history_frame, text="Retrieve Full History", command=(self.write_to_file))
        self.full_history.grid(row=4, pady=10)
        

        #History Text 1 
        self.history_text = Label(self.history_frame, text="", justify=LEFT, width=40, bg=bkg_colour , wrap=250)
        self.history_text.grid(row=1)
        
        #disable history button
        partner.calch_button.config(state=DISABLED)

        #Dismiss button 2 
        self.history_dismiss_button = Button(self.history_frame, text="Exit", width=5, command=partial(self.close_button, partner))
        self.history_dismiss_button.grid(row=5,pady=10)

        
    
    def write_to_file(self):
        #opens a new window
        self.input_filename = Toplevel()
        
        self.input_frame = Frame(self.input_filename, width=400, height=300, bg="#9fe5d9", padx=10, pady=20)
        self.input_frame.grid()
        
        self.input_text = Label(self.input_frame, text="Input Filename:")
        self.input_text.grid(row=1)
        #input box filename
        self.filename_input = Entry(self.input_frame, width=20, font="Arial 14 bold")
        self.filename_input.grid(row=2)

        #History data
        data = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh']
            #assumed valid data input for file name
        has_error = "yes"
        while has_error == "yes":
        
            filename = self.filename_input.get()
        has_error = "no"


        valid = "[A-za-z0-9_]"
        for letter in filename:
            if re.match(valid, letter):
            
                continue
        
            elif letter == " ":
                problem = ("No spaces allowed.")
       
            else:
                problem = ("No {}'s allowed.".format(letter))

                has_error = "yes"

        if filename == "":
            problem= "Please enter a filename."
            has_error = "yes"

        if has_error == "yes":
           return  ("Invalid filename - {}".format(problem))
            #("Invalid filename - {}".format(problem))
        else:
            #("Done.")

     #text file
         filename = filename + ".txt"
#make the file
        f = open(filename, "w+")
#add new line for each item
        for item in data:
            f.write(item + "\n")
#close the file
        f.close


    
    

 #close help function
    
    def close_button(self, partner):
        partner.calch_button.config(state=NORMAL)
        self.history_box.destroy()
        

       
 # main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter(root)
    root.mainloop()