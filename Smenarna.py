#!/usr/bin/env python3

from os.path import basename, splitext
import tkinter as tk
import random
from tkinter import  CENTER, E, END, LEFT, TOP,  N, W, UNDERLINE, BOTTOM, HORIZONTAL, Label, Button, Scale,  StringVar, Frame, Entry , Listbox,Radiobutton,LabelFrame
from tkinter.ttk import Labelframe
   

# from tkinter import ttk


class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "Smenarna (rubly nevedeme)"

    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        self.bind("<Escape>", self.quit)
         
                #Nadpisek
        self.lblNazev = tk.Label(self, text="Směnárna")
        self.lblNazev.grid(row=0, column=1, columnspan=3)
                #Transakce
        self.TransakciVariable = tk.IntVar()
        self.TransakciVariable.set(0)
        
        self.labelframe = tk.LabelFrame(self , text="Transakce")
        self.labelframe.grid(row=1,column=1, sticky = W)
                #Nakup a prodej 
        self.varTransakce = tk.IntVar()
        self.varTransakce.set(0)
       
        self.radiobutton0 =tk.Radiobutton(self.labelframe,variable =self.varTransakce,  text="Nákup", value=0)
        self.radiobutton0.grid()

        self.radiobutton1 =tk.Radiobutton(self.labelframe, variable =self.varTransakce, text="Prodej", value=1)
        self.radiobutton1.grid()

        self.varTransakce.set("Nákup")

                #Mena
        mena = self.nacteni_listku()  

        self.MenaVar = tk.IntVar()
        self.MenaVar.set(0)

        self.labelframeMen = tk.LabelFrame(self , text="Měna")
        self.labelframeMen.grid(row=2,column=1,sticky = W)
        for n,item in enumerate(mena):
            Radiobutton(self.labelframeMen, text=item[0], variable = self.MenaVar, value = n).grid()
        
            #Kurz 
        self.kurzVariable =tk.StringVar()
        self.kurzVariable.set("")

        self.mnozstviVariable = tk.StringVar()
        self.mnozstviVariable.set("")
        
        self.labelframe2 = tk.LabelFrame(self , text="Kurz")
        self.labelframe2.grid(row=3,column=1)

        self.Editmnozstvi0 = tk.Entry (self.labelframe2,state = "readonly" ,textvariable= self.mnozstviVariable )
        self.Editmnozstvi0.grid()

        self.EditKurz1 = tk.Entry (self.labelframe2,state = "readonly", textvariable= self.kurzVariable)
        self.EditKurz1.grid()
            

            #Vypocet
        
        self.VstupniVariable = tk.StringVar()
        self.VstupniVariable.set("")
        
        self.VystupniVariable = tk.StringVar()
        self.VystupniVariable.set("")

        self.labelframe3 = tk.LabelFrame(self , text="Výpočet")
        self.labelframe3.grid(row=4,column=1)
        
        self.EditVstupu2 = tk.Entry (self.labelframe3, textvariable= self.VstupniVariable)
        self.EditVstupu2.grid()

        self.btn1 = tk.Button (self.labelframe3, text= "Výpočet", command = self.No_sam_bych_to_nevymyslel  ) 
        self.btn1.grid()
        
        self.EditVystupu2 = tk.Entry (self.labelframe3,state = "readonly", textvariable= self.VystupniVariable )
        self.EditVystupu2.grid()
        
        
        #self.listbox = tk.Listbox(self)
        #self.listbox.grid(row=5 ,column=1 )
        #for item in [u"", u""]:
        #    self.listbox.insert(END, item)
   
   
        


    
    def nacteni_listku (self):                            #nacitani textu
        f = open("listek.txt","r")
        mena = []
        while 1:
            radek = f.readline()
            if radek == "":
                break 

            if radek.strip()[0] == "#":
                continue 
            mena += [radek.replace(",",".").split()]
        f.close()
        for radek in mena:
                radek[1] = float(radek[1])
                radek[2] = float(radek[2])
                radek[1] = float(radek[3])
        return mena 

    
    mnozstvi = 1
    kurz = 1 

    def No_sam_bych_to_nevymyslel (self):
        global mnozstvi
        global kurz 
        Vstupu = float(self.VstupniVariable.get())
        Vystupu = kurz/mnozstvi * Vstupu
        self.VystupniVariable.set(str(Vystupu))
        

    def Updatekurzu(self, *Args):
        global mnozstvi
        global kurz 
        self.mnozstviVariable.set(str(mena[self.MenaVar.get()][1]))
        count = mena [self.MenaVar.get()][1]
        if self.varTransakce.get()==0:
            self.kurzVariable.set(str(mena[self.MenaVar.get()][2]))
            kurz = mena [self.MenaVar.get()][2]
        else:
            self.kurzVariable.set(str(mena[self.MenaVar.get()][3]))
            kurz = mena[self.MenaVar.get()][3]


    
            
        

        self.TransakciVariable.trace("w",self.Updatekurzu)
        self.MenaVar.trace("w",self.Updatekurzu)
        app.bind("<Map>",self.Updatekurzu)

    
    
    
    
    
    def quit(self, event=None):
        super().quit()

   
    





app = Application()
app.mainloop()
