from tkinter import *
import random


class Converter:
    def __init__(self, parent):

        bkg_colour = "#9fe5d9"

        self.converter_frame = Frame(width=400, height=300, bg=bkg_colour)
        self.converter_frame.grid()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter(root)
    root.mainloop()
