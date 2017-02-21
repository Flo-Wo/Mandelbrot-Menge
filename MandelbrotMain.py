"""!/usr/bin/python
-*- coding: UTF-8 -*-
Date: 21.02.2017
"""

#Modul für die graphische Darstellung
import tkinter
#Mathematikmodul
import math
#eigenes Modul für die Farbwahl
import farben


#Falls Änderung der Größe des Fensters, alle weiteren Angaben sind relativ
xwidth = 500
yheight = 500


#Initialisierung Variablen
deltax = None
deltay = None


#Erzeugung des Fensters aus dem tkinter-Modul
#Fenster bleibt, Canvas immer überschrieben
fenster = tkinter.Tk()
#Titel des erzeugten Fensters
fenster.title("Die Mandelbrot-Menge.")

#Erzeugen der Zeichenoberfläche aus dem tkinter-Modul
w = tkinter.Canvas(fenster, width=xwidth, height=yheight)
#Ohne .pack() wird diese nicht korrekt dargestellt
w.pack()


#Endlosschleife
while True:
    #Eingaben der Breite und Höhe des anzuzeigenden Bereichs
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
            #Position des Pixels ist jetzt bekannt (cr/ci))
            #-------------
            #Iterationschritte für jeden Pixel --> rekursive Folge durchlaufen
            #-------------
            #Wert des Realteils
            zi = 0
            #Wert des Imaginärteils
            zr = 0
            #Entweder Abstand zum Ursprung größer als 2 --> divergiert mit Sicherheit
            #oder maximal 100 Iterationsschritte, bis dahin keine Divergenz --> innerhalb der Menge
            #je schneller der Wert konvergiert, desto dunkler die Farbe des Pixels --> Verweis Farbmodul

            #Zähler Iterationsschritte initialisiert
            n = 0
            while ((zr**2 + zi**2)<=2) and n <= 100:
                #-------------
                #Rekursive Folge lautet: z_(n+1) = z_(n)^2 + c
                #Komplexe Multiplikation durchführen
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
            #Modul gibt über return(color) die Farbe zurück
            #-------------
            color = farben.farbwahl(n)
            #Erzeugung des Pixels einzelnen Pixels an der Position (cr/ci)
            #Paramter der reactangle-Funktion:
                #Wert 1 und 2: Koordinaten der "Starposition"
                #Wert 2 und 3: Koordinaten der "Endposition"
                #die beiden Punkte spannen die Ecken des Rechtecks auf
                #fill: Füllfarbe, die das Modul übergibt
                #width: Dicke des Randes, der standardmäßig schwarz ist --> kein Rand
            #w. bezieht sich auf die Zeichenfläche (Canvas, oben erstellt)
            w.create_rectangle(xpixel, ypixel, xpixel, ypixel , fill=color, width=0)
