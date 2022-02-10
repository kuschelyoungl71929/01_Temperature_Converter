from tkinter import *
import random


class Converter:
    def __init__(self, parent):

        bkg_colour = "#9fe5d9"

 
        self.converter_frame = Frame(width=400, height=300, bg=bkg_colour)
        self.converter_frame.grid()

    self.temp_converter_label = Label(text="Temperature Converter" font=("Arial", "18", "bold"), bg=bkg_colour padx=10, pady=10)
    self.temp_converter_label.grid(row=0)

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter(root)
    root.mainloop()
