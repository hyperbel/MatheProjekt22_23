import sqlite3
import random

con = sqlite3.connect('mathe.db')
cur = con.cursor()

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
            if hoch == 2:
                if b > 0:
                    if c > 0:
                        function = f"{a}x^{hoch}+{b}x+{c}"
                    else:
                        function = f"{a}x^{hoch}+{b}x{c}"
                else:
                    if c > 0:
                        function = f"{a}x^{hoch}{b}x+{c}"
                    else:
                        function = f"{a}x^{hoch}{b}x{c}"
            elif hoch == 3:
                if b > 0:
                    if c > 0:
                        if d > 0:
                            function = f"{a}x^{hoch}+{b}x^2+{c}x+{d}"
                        else:
                            function = f"{a}x^{hoch}+{b}x^2+{c}x{d}"
                    else:
                        function = f"{a}x^{hoch}+{b}x^2{c}x+{d}"
                else:
                    if c > 0:
                        if d > 0:
                            function = f"{a}x^{hoch}{b}x^2+{c}x+{d}"
                        else:
                            function = f"{a}x^{hoch}+{b}x^2+{c}x{d}"
                    else:
                        function = f"{a}x^{hoch}{b}x^2{c}x+{d}"
            elif hoch == 4:
                 hoch2 = random.randint(2, 3)
                 if b > 0:
                    if c > 0:
                        if d > 0:
                                function = f"{a}x^{hoch}+{b}x^{hoch2}+{c}x+{d}"
                        else:
                                function = f"{a}x^{hoch}+{b}x^{hoch2}+{c}x{d}"
                    else:
                            function = f"{a}x^{hoch}+{b}x^{hoch2}{c}x+{d}"
                 else:
                        if c > 0:
                            if d > 0:
                                function = f"{a}x^{hoch}{b}x^{hoch2}+{c}x+{d}"
                            else:
                                function = f"{a}x^{hoch}+{b}x^{hoch2}+{c}x{d}"
                        else:
                            function = f"{a}x^{hoch}{b}x^{hoch2}{c}x+{d}"
            elif hoch == 5:
                 hoch2 = random.randint(2, 4)
                 if b > 0:
                    if c > 0:
                        if d > 0:
                                function = f"{a}x^{hoch}+{b}x^{hoch2}+{c}x+{d}"
                        else:
                                function = f"{a}x^{hoch}+{b}x^{hoch2}+{c}x{d}"
                    else:
                            function = f"{a}x^{hoch}+{b}x^{hoch2}{c}x+{d}"
                 else:
                        if c > 0:
                            if d > 0:
                                function = f"{a}x^{hoch}{b}x^{hoch2}+{c}x+{d}"
                            else:
                                function = f"{a}x^{hoch}+{b}x^{hoch2}+{c}x{d}"
                        else:
                            function = f"{a}x^{hoch}{b}x^{hoch2}{c}x+{d}"
            elif hoch == 6:
                 hoch2 = random.randint(2, 5)
                 if b > 0:
                    if c > 0:
                        if d > 0:
                                function = f"{a}x^{hoch}+{b}x^{hoch2}+{c}x+{d}"
                        else:
                                function = f"{a}x^{hoch}+{b}x^{hoch2}+{c}x{d}"
                    else:
                            function = f"{a}x^{hoch}+{b}x^{hoch2}{c}x+{d}"
                 else:
                        if c > 0:
                            if d > 0:
                                function = f"{a}x^{hoch}{b}x^{hoch2}+{c}x+{d}"
                            else:
                                function = f"{a}x^{hoch}+{b}x^{hoch2}+{c}x{d}"
                        else:
                            function = f"{a}x^{hoch}{b}x^{hoch2}{c}x+{d}"
            elif hoch == 7:
                 hoch2 = random.randint(2, 6)
                 if b > 0:
                    if c > 0:
                        if d > 0:
                                function = f"{a}x^{hoch}+{b}x^{hoch2}+{c}x+{d}"
                        else:
                                function = f"{a}x^{hoch}+{b}x^{hoch2}+{c}x{d}"
                    else:
                            function = f"{a}x^{hoch}+{b}x^{hoch2}{c}x+{d}"
                 else:
                        if c > 0:
                            if d > 0:
                                function = f"{a}x^{hoch}{b}x^{hoch2}+{c}x+{d}"
                            else:
                                function = f"{a}x^{hoch}+{b}x^{hoch2}+{c}x{d}"
                        else:
                            function = f"{a}x^{hoch}{b}x^{hoch2}{c}x+{d}"
                
           
        else:
            function = f"{a}x + {b}"

        cur.execute("INSERT INTO funktionen VALUES (?, ?)", (function, userid))
        yield function
    
    con.commit()

for function in insert_functions(10):
    print(function)
