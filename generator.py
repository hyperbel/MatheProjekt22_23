import sqlite3
import random

con = sqlite3.connect('mathe.db')
cur = con.cursor()

def expo_generator():
    a = random.randint(0, 20)
    b = random.randint(0, 9)

    if b == 0:
        return a 
    else:
        f = str(a) + "." + str(b)
        return f

def trigo_generator():
    amplitude = random.randint(1, 30)
    frequenz = random.randint(1, 30)
    phase = random.randint(1, 30)
    felder = []
    felder.append(str(amplitude))
    felder.append(str(frequenz))
    felder.append(str(phase))
    return felder

def integral_generator():
    a = random.randint(0, 30)
    funktion = "x**" + str(a)
    return funktion

def terme_generator():
    function = ""
    a = random.randint(-10, 10)
    b = random.randint(-10, 10)
    c = random.randint(-10, 10)
    d = random.randint(-10, 10)
    hoch = random.randint(1, 7)
    if hoch > 1:
        # der 2. exponent ist 1 kleiner als der erste. wird nur bei hoch > 3 gebraucht
        hoch2 = random.randint(2,hoch-1) if hoch > 3 else 0
        funktion = ""
        # die funktion wird von hinten aufgebaut
        # wenn eine variable nicht 0 ist, wird am ende der funktion das dran gehängt.
        if d != 0:
            funktion = f"+{d}" if d > 0 else f"{d}"
        if c != 0:
            funktion = f"+{c}x{funktion}" if c > 0 else f"{c}x{funktion}"
        if b != 0:
            funktion = f"+{b}x^{hoch2}{funktion}" if b > 0 else f"{b}x^{hoch2}{funktion}"
        if a != 0:
            funktion = f"{a}x^{hoch}{funktion}" if a > 0 else f"{a}x^{hoch}{funktion}"
        function = funktion
        return function
    else:
        function = f"{a}x + {b}"
        return function
    
