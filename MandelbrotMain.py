"""!/usr/bin/python
-*- coding: UTF-8 -*-
Date: 21.02.2017
"""

import tkinter
import math
#eigenes Modul für die Farbwahl
import farben


#Falls Änderung der Größe des Fensters
xwidth = 500
yheight = 500


#Initialisierung Variablen
deltax = None
deltay = None


#Erzeugung des Fensters
#Fenster bleibt, Canvas immer überschrieben
fenster = tkinter.Tk()
fenster.title("Die Mandelbrot-Menge.")

#Erzeugen der Zeichenoberfläche
w = tkinter.Canvas(fenster, width=xwidth, height=yheight)
w.pack()



while True:
    #Eingabe
    xmin = int(input("xMin eingeben: "))
    xmax = int(input("xMax eingeben: "))
    ymin = int(input("yMin eingeben: "))
    
    #Löschen aller Objekte auf der Zeichenoberfläche --> Überschreibung beim Zoom nötig
    w.delete("all")
    #Berechnung ymax --> eine Eingabe weniger
    ymax = (xmax - xmin) + ymin
    #Berechnung der beiden Deltas --> Schritte
    deltax = (xmax - xmin)/xwidth
    deltay = (ymax - ymin)/yheight

    #Durchgehen der einzelnen Pixel in Form einer 2-dimensionalen Liste
    for xpixel in range(0, xwidth):
        #Berechnung des Realteils des Parameters c
        cr = xmin + (xpixel * deltax)
        for ypixel in range(0, xwidth):
            #Berechnung Imaginärteil des Parameters c
            ci = ymin + (ypixel * deltay)
            #-------------
            #Pixel ist jetzt bekannt (cr/ci))
            #-------------
            #Iterationschritte für jeden Pixel --> rekursive Folge durchlaufen
            #-------------
            #Wert des Realteils
            zi = 0
            #Wert des
            zr = 0
            #Entweder Abstand zum Ursprung größer als 2 --> divergiert mit Sicherheit
            #oder maximal 100 Iterationsschritte, bis dahin keine Divergenz --> innerhalb der Menge
            #je schneller etwas konvergiert, desto dunkler

            #Zähler Iterationsschritte
            n = 0
            while ((zr**2 + zi**2)<=2) and n <= 100:
                #-------------
                #Komplexe Multiplikation laut: z_(n+1) = z_(n)^2 + c
                #-------------

                #Neuer Realteil
                zrneu = zr * zr - zi * zi + cr
                #Neuer Imaginärteil
                zineu = 2 * zr * zi + ci

                #Übergeben der Werte für die nächste Iteration
                zr = zrneu
                zi = zineu
                #Erhöhung Iterationschritt
                n += 1
            #-------------
            #Vergeben Farbe Pixel, wenn die Schleife abbricht --> Wert divergiert, geht -> infty
            #Farbüberprüfung über Farbmodul
            #-------------
            color = farben.farbwahl(n)
            w.create_rectangle(xpixel, ypixel, xpixel, ypixel , fill=color, width=0)
