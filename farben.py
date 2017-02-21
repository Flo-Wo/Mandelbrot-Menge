#farbenZuordnung.py
"""!/usr/bin/python
-*- coding: UTF-8 -*-
Date: 21.02.2017
"""

#Der Wert n (Anzahl der Iterationsschritte) wird übergeben, Farbe soll Ausgabe sein


def farbwahl(n):
    #-----------------
    #1er-Schritte
    #-----------------
    if n <= 1:
        color = "white"
        #Weiß
    elif 1 < n <= 2:
        color = "#ffffb3"
        #sehr sehr helles Gelb
    elif 2 < n <= 3:
        color = "#ffff99"
        #sehr helles Gelb
    elif 3 < n <= 4:
        color = "#ffff80"
        #helles Gelb
    elif 4 < n <= 5:
        color = "#ffff66"
        #leicht helles Gelb
    elif 5 < n <= 6:
        color = "#ffff33"
        #Gelb
    elif 6 < n <= 7:
        color = "#e6e600"
        #dunkles Gelb
    elif 7 < n <= 8:
        color = "#ffc266"
        #helles Orange
    elif 8 < n <= 9:
        color = "#ffb84d"
        #Orange
    elif 9 < n <= 10:
        color = "#ffad33"
        #dunkles Orange
    #-----------------
    #2er-Schritte
    #-----------------
    elif 10 < n <= 12:
        color = "#ff99ff"
        #helles Rosa
    elif 12 < n <= 14:
        color = "#ff33ff"
        #Rosa
    elif 14 < n <= 16:
        color = "#ff4d4d"
        #helles Rot
    elif 16 < n <= 18:
        color = "#cc0000"
        #Rot
    elif 18 < n <= 20:
        color = "#990000"
        #dunkles Rot
    #-----------------
    #5er-Schritte
    #-----------------
    elif 20 < n <= 25:
        color = "#800080"
        #Violet
    elif 25 < n <= 30:
        color = "#660066"
        #dunkles Violet
    elif 30 < n <= 35:
        color = "#4700b3"
        #gemäßigtes Blau
    elif 35 < n <= 40:
        color = "#3d0099"
        #Blau
    #-----------------
    #10er-Schritte
    #-----------------
    elif 40 < n <= 50:
        color = "#330080"
        #dunkles Blau
    elif 50 < n <= 60:
        color = "#009900"
        #gemäßigtes Grün
    elif 60 < n <= 70:
        color = "#39ac39"
        #Grün
    elif 70 < n <= 80:
        color = "#1f601f"
        #dunkles Grün
    elif 80 < n <= 90:
        color = "#996633"
        #Braun
    elif 90 < n <= 99:
        color = "#60401f"
        #dunkles Braun
    else:
        #bei 100 Iterationsschritten keine Divergenz --> Konvergenz, in der Mandelbrot-Menge
        color = "black"
        #Schwarz
    return(color)
