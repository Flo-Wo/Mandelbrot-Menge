"""!/usr/bin/python
-*- coding: UTF-8 -*-
Date: 07.02.2017
"""

import math
import tkinter

#Fensterbreite
xwidth = 500
yheigt = 500

#Iterationsschritte, initialisierung
n = 0

#Betrag, Abstand zur 0
betrag = 0


fenster = tkinter.Tk()
fenster.title("Die Mandelbrot-Menge.")
w = tkinter.Canvas(fenster, width=xwidth, height=yheight)
w.pack()
#tk.mainloop()

#Rückgabe der Eingabewerte
def callback():
    w.get()
    return()

#Schritte werden berechnet
def deltacalc(xmin, xmax, ymin, ymax):
    deltax = (xmax - xmin)/500
    deltay = (ymax - ymin)/500



while True:
    w.focus_set()
    xmin = tkinter.Button(fenster, text = "xMin eingeben", width = 10, command = callback)
    xmax = tkinter.Button(fenster, text = "xMax eingeben", width = 10, command = callback)
    ymin = tkinter.Button(fenster, text = "yMin eingeben", width = 10, command = callback)
    #Berechung ymax --> Fenstergröße
    ymax = xmax - xmin + ymin
    deltacalc()
    #Durchgehen aller x-Werte
    for xpixel in range(0, 500):
        #Berechnung cr
        cr = xmin + xpixel * deltax
        #Durchgehen aller y-Werte
        for ypixel in range(0, 500):
            #Berechnung ci
            ci = ymax - ypixel * deltay
            #farbe wählen
            #Rechteck: 1. 2 Koord. Startpunkt, 2. 2 Koord. Endpunkt, von --> zu
            w.create_rectangle(100, 100, 101, 101, fill=farbe)

    w.pack()
