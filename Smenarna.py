#!/usr/bin/env python3

from os.path import basename, splitext
import tkinter as tk
import random
from tkinter import  CENTER, E, LEFT, TOP,  N, UNDERLINE, BOTTOM, HORIZONTAL, Label, Button, Scale,  StringVar, Frame, Entry , Listbox

# from tkinter import ttk


class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "Smenarna (rubly nevedeme)"

    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        self.bind("<Escape>", self.quit)
         
        self.listbox = tk.Listbox(self, text="mrsina")
        self.listbox.grid( row=1, colum=1)

        
        


    def quit(self, event=None):
        super().quit()


app = Application()
app.mainloop()
