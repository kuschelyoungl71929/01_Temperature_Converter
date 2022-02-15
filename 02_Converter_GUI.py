from tkinter import *
from functools import partial #for removing window
import random

class Converter:
    def __init__(self, parent):

        bkg_colour = "#9fe5d9"

        self.converter_frame = Frame(width=400, height=300, bg=bkg_colour, padx=10, pady=10)
        self.converter_frame.grid()

        self.converter_label = Label(self.converter_frame, text="Temperature Converter", font=("Arial 18 bold"), bg=bkg_colour, padx=10, pady=30)
        self.converter_label.grid(row=1)

        self.user_i = Label(self.converter_frame, text="User Information")
        self.user_i.grid(row=2)
        # main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter(root)
    root.mainloop()