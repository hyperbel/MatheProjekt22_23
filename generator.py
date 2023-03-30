import sqlite3
import random

con = sqlite3.connect('mathe.db')
cur = con.cursor()

def insert_functions(num_functions):
    userid = 1
    
    for i in range(num_functions):
        a = random.randint(-10, 10)
        b = random.randint(-10, 10)
        c = random.randint(-10, 10)
        function = f"{a}x^2 + {b}x + {c}"
        cur.execute("INSERT INTO funktionen VALUES (?, ?)", (function, userid))
        yield function
    
    con.commit()

for function in insert_functions(10):
    print(function)
