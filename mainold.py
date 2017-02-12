"""!/usr/bin/python
-*- coding: UTF-8 -*-
Date: 02.02.2017
"""

import tkinter
import math

xwidth = 200
yheight = 200


fenster = tkinter.Tk()
fenster.title("Die Mandelbrot-Menge")
w = tkinter.Canvas(fenster, width=xwidth, height=yheight)
w.pack()
w.create_rectangle(100, 100, 101, 101, fill="blue")
w.create_rectangle(100, 100, 120, 120, fill="orange")

#Zahl 1 und 2 geben x- und y-Werte des Startpunkts (oben links) an
#die Zahlen 3 und 4 die Koordinaten des Endpunkts (unten rechts) an

#Fenster bleibt geöffnet
tkinter.mainloop()


#Initialisierung Abstand zur 0
betrag = 0

#Iterationsschritte
n = 0

# while betrag < 0 and n < 1001:
#     #Iteration
#     n += 1
#
# if n = 1001:
#     #Setze Pixel(x;y) -> schwarz
# elif n < 1001:
#     #Setze Pixel(x;y) -> blau
# elif n < 100:
#     #Setze Pixel(x;y) -> rot
# elif n < 10:
#     #Setze Pixel(x;y) -> gelb
# elif n < 2:
#     #Setze Pixel(x;y) -> weiß
