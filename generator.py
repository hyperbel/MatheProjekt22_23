import sqlite3
import random

con = sqlite3.connect('mathe.db')
cur = con.cursor()

def expo_generator():
    a = random.randint(0, 100)
    b = random.randint(0, 9)

    if b == 0:
        return a 
    else:
        return a + "." + b

def insert_functions(num_functions):
    userid = 1
    
    for _ in range(num_functions):
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
        else:
            function = f"{a}x + {b}"

        cur.execute("INSERT INTO funktionen VALUES (?, ?)", (function, userid))
        yield function
    
    con.commit()

for function in insert_functions(1500000):
    print(function)
