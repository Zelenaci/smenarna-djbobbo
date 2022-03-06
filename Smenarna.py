#!/usr/bin/env python3

from os.path import basename, splitext
import tkinter as tk
import random
from tkinter import  CENTER, E, END, LEFT, TOP,  N, UNDERLINE, BOTTOM, HORIZONTAL, Label, Button, Scale,  StringVar, Frame, Entry , Listbox,Radiobutton,LabelFrame
from tkinter.ttk import Labelframe
   

# from tkinter import ttk


class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "Smenarna (rubly nevedeme)"

    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        self.bind("<Escape>", self.quit)
         
        
        self.lblNazev = tk.Label(self, text="Směnárna")
        self.lblNazev.grid(row=0, column=1, columnspan=3)

        self.labelframe = tk.LabelFrame(self , text="Transakce")
        self.labelframe.grid(row=1,column=1)

        self.radiobutton0 =tk.Radiobutton(self.labelframe, text="Nákup",value=1)
        self.radiobutton0.grid()

        self.radiobutton1 =tk.Radiobutton(self.labelframe, text="Prodej",value=2)
        self.radiobutton1.grid()

        self.labelframe1 = tk.LabelFrame(self , text="Měna")
        self.labelframe1.grid(row=2,column=1)
       
        self.radiobutton2 =tk.Radiobutton(self.labelframe1, text="EUR", value=3)
        self.radiobutton2.grid()

        self.radiobutton3 =tk.Radiobutton(self.labelframe1, text="GBP", value=4)
        self.radiobutton3.grid()
   
        self.radiobutton4 =tk.Radiobutton(self.labelframe1, text="USD", value=5)
        self.radiobutton4.grid()

        self.radiobutton5 =tk.Radiobutton(self.labelframe1, text="JPY", value=6)
        self.radiobutton5.grid()

        self.radiobutton6 =tk.Radiobutton(self.labelframe1, text="IDR", value=7)
        self.radiobutton6.grid()
       
        self.labelframe2 = tk.LabelFrame(self , text="Kurz")
        self.labelframe2.grid(row=3,column=1)

        self.entry0 = tk.Entry (self.labelframe2)
        self.entry0.grid()

        self.entry1 = tk.Entry (self.labelframe2)
        self.entry1.grid()


        self.labelframe3 = tk.LabelFrame(self , text="Výpočet")
        self.labelframe3.grid(row=4,column=1)
        
        self.entry2 = tk.Entry (self.labelframe3)
        self.entry2.grid()

        self.btn1 = tk.Button (self.labelframe3, text= "Výpočet")
        self.btn1.grid()
        
        
        
        #self.listbox = tk.Listbox(self)
        #self.listbox.grid(row=5 ,column=1 )
        #for item in [u"", u""]:
        #    self.listbox.insert(END, item)
   
   
    def vyplneni_listboxu(self):
        f = open("listek.txt","r")
        slovnik = {}
        for line in f:
            self.listbox.insert(tk.END,line.split()[0])
            slovnik[line.split()[0]] = (line.split()[1:])



    def quit(self, event=None):
        super().quit()


app = Application()
app.mainloop()
