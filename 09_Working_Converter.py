from tkinter import * 
from functools import partial #for removing window
import random
import re

class Converter:
    def __init__(self, calc_history):

        #light cyan
        bkg_colour = "#9fe5d9"

        #set up for calc history
        self.all_calc_list = []

        # frame
        self.converter_frame = Frame(width=400, height=300, bg=bkg_colour, padx=10, pady=10)
        self.converter_frame.grid()
        
        # Heading
        self.converter_label = Label(self.converter_frame, text="Temperature Converter", font=("Arial 18 bold"), bg=bkg_colour, padx=10, pady=30)
        self.converter_label.grid(row=1)
        
        # User information/Instructions
        self.user_i = Label(self.converter_frame, text="Enter the temperature you would like to convert and click the button with the unit sytem you want to convert it to.", font="arial 10 italic", wrap=250, justify=LEFT, bg=bkg_colour, pady=10)
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
        self.calch_button = Button(self.hc_button_frame, text="Calculation History", width=15, command=lambda: self.history(self.all_calc_list))
        self.calch_button.grid(row=0, column=0, padx=5)

        # help Button
        self.help_button = Button(self.hc_button_frame, text="Help", width=5, command=self.help)
        self.help_button.grid(row=0, column=1, padx=5) 

        #disables history button before conversions have been made
        if len(self.all_calc_list) == 0:
            self.calch_button.config(state=DISABLED)


        # help command
    def help(self):  
        print("help")
        get_help = Help(self)
        get_help.help_text.configure(text="Enter the Temperature you would like to convert then click the button labelled with the unit system you want to convert to", bg="white")
        
        #history command
    def history(self, calc_history):
        print("history")
        History(self,calc_history)
       
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

            if has_errors != "yes":
                self.all_calc_list.append(answer)
                self.calch_button.config(state=NORMAL)

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
        bkg_colour= "#c6e2ff" #light blue

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
        self.help_text = Label(self.help_frame, text="help", justify=LEFT, width=40, bg=bkg_colour , wrap=250)
        self.help_text.grid(row=1)

        #Dismiss button 2 
        self.dismiss_button = Button(self.help_frame, text="Exit", width=10, command=partial(self.close_button, partner))
        self.dismiss_button.grid(row=2,pady=10)
    
    #close help function
    def close_button(self, partner):
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()

class History:
    def __init__(self, partner, calc_history):

        #background colour
        bkg_colour= "#b9cfad" #light green

        #Button off
        partner.calch_button.config(state=DISABLED)

        #opens a new window
        self.history_box = Toplevel()
        
        self.history_box.protocol('WM_DELETE_WINDOW', partial(self.close_history, partner))

        #GUI Frame
        self.history_frame = Frame(self.history_box, width=400, height=300, bg=bkg_colour, padx=10, pady=10)
        
        self.history_frame.grid()

        #History Heading 0
        self.history_converter_label = Label(self.history_frame, text="Conversion History", font=("Arial 16 bold"), bg=bkg_colour, padx=10, pady=10)
       
        self.history_converter_label.grid(row=0)

        #History Text 1 
        self.history_text = Label(self.history_frame, text="These are your most recent conversions, you can view full conversion history in a text file with the button labelled Export.", justify=CENTER, width=40, bg=bkg_colour , wrap=250)
        self.history_text.grid(row=1)
        

        history_string = ""
      
            
       
    
        if len(calc_history) > 7:
            for item in range(0,7):
                history_string += calc_history[len(calc_history) - item - 1]+"\n"

        else:
            for item in calc_history:
                history_string += calc_history[len(calc_history) - calc_history.index(item) - 1]+"\n"

                self.history_text.config(text="Here are your conversions, you can save these to a text file with the Export button.")
                   
        #display recent history 

        self.history_string_label = Label(self.history_frame, text=history_string , font=("Arial 12"), bg=bkg_colour, justify=LEFT, padx=10, pady=10)
       
        self.history_string_label.grid(row=3, pady=5)

        #button frame
        self.button_frame_history = Frame(self.history_frame, bg= bkg_colour)
        self.button_frame_history.grid(row=5)

        #Dismiss button 2 
        self.dismiss_button = Button(self.button_frame_history, text="Exit", width=10, command=partial(self.close_history, partner))
        self.dismiss_button.grid(row=0, column=1, padx=5)

        #retrieve full history button
        self.full_history = Button(self.button_frame_history, text="Export", width=10, command=lambda: self.export_button(calc_history))
        self.full_history.grid(row=0, column=0, padx=5)

    def export_button(self, calc_history):
        get_export= Export(self, calc_history)
        
 #close history function
    
    def close_history(self, partner):
        partner.calch_button.config(state=NORMAL)
        self.history_box.destroy()

class Export:
    def __init__(self, partner, calc_history):

        #light cyan
        bkg_colour = "#9fe5d9"
        
        partner.full_history.config(state=DISABLED)
        #export box
        self.export_box = Toplevel()
        
        # frame
        self.export_frame = Frame(self.export_box, width=400, height=300, bg=bkg_colour, padx=10, pady=10)
        self.export_frame.grid()
        
        # Heading
        self.export_label = Label(self.export_frame, text="Export", font=("Arial 16 bold"), bg=bkg_colour, padx=5, pady=10)
        self.export_label.grid(row=1)
        
        # User information/Instructions
        self.instructions = Label(self.export_frame, text="Enter a filename, no spaces or special characters", wrap=250, justify=LEFT, bg=bkg_colour, font="arial 11", padx=10, pady=10)
        self.instructions.grid(row=2)

        self.instructions = Label(self.export_frame, text="Warning: If the filename you choose already exists, your calculation history will overwrite that file", wrap=250, justify=LEFT, bg="#F3B6B6", font="arial 11 italic", padx=10, pady=10)
        self.instructions.grid(row=3, pady=5)
        # Temper input box
        self.filename_box = Entry(self.export_frame, width=15, font="Arial 12 bold")
        self.filename_box.grid(row=4)

        self.error_filename = Label(self.export_frame, text="", wrap=250, justify=LEFT, bg=bkg_colour, font="arial 11", padx=10, pady=10)
        self.error_filename.grid(row=5)
       
        #button frame
        self.save_exit_button_frame = Frame(self.export_frame, bg=bkg_colour)
        self.save_exit_button_frame.grid(row=6, pady=10)

        #exit
        self.dismiss_button_export = Button(self.save_exit_button_frame, text="Exit", width=7, command=partial(self.close_export, partner))
        self.dismiss_button_export.grid(row=0, column=1, padx=5)

        #save Button
        self.save_button = Button(self.save_exit_button_frame, width=7, text="Save", command=partial(lambda: self.save_as_file(partner, calc_history)))
        self.save_button.grid(row=0, column=0, padx=5)

    def save_as_file(self, partner, calc_history):

        valid_char = "[A-za-z0-9_]"
        has_error= "no"

        filename=  self.filename_box.get()
      
        
        for letter in filename:
            if re.match(valid_char, letter):
                continue
        
            elif letter == " ":
                problem = ("No spaces allowed.")
       
            else:
                problem = ("No {}'s allowed.".format(letter))

            has_error = "yes"
            break

        if filename == "":
            problem= "Please enter a filename."
            has_error = "yes"

        if has_error == "yes":
            self.error_filename.config(text="Invalid filename - {}".format(problem))
        else:
            filename = filename + ".txt"

            f = open(filename, "w+")

            for item in calc_history:
                f.write(item + "\n")

        f.close

        self.close_export(partner)

    def close_export(self, partner):
        partner.full_history.config(state=NORMAL)
        self.export_box.destroy()

        

       
 # main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter(root)
    root.mainloop()