import sqlite3
import random

con = sqlite3.connect('mathe.db')
cur = con.cursor()

def insert_functions(num_functions):
    userid = 1
    
    for _ in range(num_functions):
        function = ""
        a = random.randint(0, 10)
        b = random.randint(0, 10)
        c = random.randint(0, 10)
        d = random.randint(0, 10)
        hoch = random.randint(1, 7)
        if hoch > 1:
            hoch2 = random.randint(2,hoch-1) if hoch > 3 else 0
            funktion = ""
            if d != 0:
                funktion = f"+{d}" if d > 0 else f"-{d}"
            if c != 0:
                funktion = f"+{c}x{funktion}" if c > 0 else f"-{c}x{funktion}"
            if b != 0:
                funktion = f"+{b}x^{hoch2}{funktion}" if b > 0 else f"-{b}x^{hoch2}{funktion}"
            if a != 0:
                funktion = f"{a}x^{hoch}{funktion}" if a > 0 else f"-{a}x^{hoch}{funktion}"
            function = funktion
        else:
            function = f"{a}x + {b}"

        cur.execute("INSERT INTO funktionen VALUES (?, ?)", (function, userid))
        yield function
    
    con.commit()

for function in insert_functions(10):
    print(function)
