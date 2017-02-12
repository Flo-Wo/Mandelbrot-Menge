"""!/usr/bin/python
-*- coding: UTF-8 -*-
Date: 07.02.2017
"""

import math
import tkinter

#Fensterbreite
xwidth = 500
yheight = 500

#Iterationsschritte, initialisierung
n = 0

#Betrag, Abstand zur 0
betrag = 0


fenster = tkinter.Tk()
fenster.title("Die Mandelbrot-Menge.")
w = tkinter.Canvas(fenster, width=xwidth, height=yheight)
w.pack()


#Schritte werden berechnet
def deltacalc(xmin, xmax, ymin, ymax):
    deltax = (xmax - xmin)/500
    deltay = (ymax - ymin)/500


w.focus_set()

#Eingabe von xMax
e1 = tkinter.Entry(fenster)
e1.pack()
e1.focus_set()

xmin = tkinter.IntVar()
xmax = tkinter.IntVar()
ymin = tkinter.IntVar()

def callbackxMax():
    #print(e1.get())
    xmin = e1.get()
    #print("xMin: " + xmin)

b = tkinter.Button(fenster, text="xmin eingeben:", width=10, command=callbackxMax)
b.pack()


#Eingabe xMin
e2 = tkinter.Entry(fenster)
e2.pack()
e2.focus_set()

xmin = tkinter.IntVar()

def callbackxMin():
    #print(e1.get())
    xmax = e2.get()
    #print("xMax: " + xmax)

b = tkinter.Button(fenster, text="xmax eingeben:", width=10, command=callbackxMin)
b.pack()


#Eingabe yMin
e3 = tkinter.Entry(fenster)
e3.pack()
e3.focus_set()

xmin = tkinter.IntVar()

def callbackyMin():
    #print(e1.get())
    ymin = e3.get()
    #print("yMin: " + ymin)

b = tkinter.Button(fenster, text="ymin eingeben:", width=10, command=callbackyMin)
b.pack()


#Berechung ymax --> Fenstergröße

# ymax = xmax - xmin + ymin
# print(xmin)
# print(xmax)
# print(ymin)
# print(ymax)
#deltacalc()
#Durchgehen aller x-Werte
# for xpixel in range(0, 500):
#     #Berechnung cr
#     cr = xmin + xpixel * deltax
#     #Durchgehen aller y-Werte
#     for ypixel in range(0, 500):
#         #Berechnung ci
#         ci = ymax - ypixel * deltay
#         #farbe wählen
#         #Rechteck: 1. 2 Koord. Startpunkt, 2. 2 Koord. Endpunkt, von --> zu
#         w.create_rectangle(100, 100, 101, 101, fill=farbe)
#
# w.pack()
tkinter.mainloop()
