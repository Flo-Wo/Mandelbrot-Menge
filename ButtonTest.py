"""!/usr/bin/python
-*- coding: UTF-8 -*-
Date: 07.02.2017
"""

import tkinter

fenster = tkinter.Tk()
fenster.title("Die Mandelbrot-Menge.")


#Eingabe von xMax
e1 = tkinter.Entry(fenster)
e1.pack()
e1.focus_set()

xmin = tkinter.IntVar()
xmax = tkinter.IntVar()
ymin = tkinter.IntVar()

def callback():
    #print(e1.get())
    xmin = e1.get()
    #print("xMin: " + xmin)

b = tkinter.Button(fenster, text="xmin eingeben:", width=10, command=callback)
b.pack()

#Eingabe xMin
e2 = tkinter.Entry(fenster)
e2.pack()
e2.focus_set()

xmin = tkinter.IntVar()

def callback():
    #print(e1.get())
    xmax = e2.get()
    #print("xMax: " + xmax)

b = tkinter.Button(fenster, text="xmax eingeben:", width=10, command=callback)
b.pack()

#Eingabe yMin

e3 = tkinter.Entry(fenster)
e3.pack()
e3.focus_set()

xmin = tkinter.IntVar()

def callback():
    #print(e1.get())
    ymin = e3.get()
    #print("yMin: " + ymin)

b = tkinter.Button(fenster, text="ymin eingeben:", width=10, command=callback)
b.pack()

tkinter.mainloop()
