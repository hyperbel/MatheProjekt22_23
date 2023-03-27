from tkinter import Frame, Listbox, Scrollbar, END, BOTH, LEFT, RIGHT
import sqlite3

class Verlauf(Frame):
    def __init__(self, master):
        super().__init__(master, bg="green", width=30)
        self.verlauf = self.get_verlauf(1)
        self.listbox = Listbox(self, width=20, height=100)
        for i in self.verlauf:
            self.listbox.insert(END, i[0])
        self.listbox.pack(side=LEFT, fill=BOTH, expand=False)

        self.scrollbar_init()

    def get_verlauf(self, userid: int):
        con = sqlite3.connect("mathe.db")
        cur = con.cursor()
        userid=1
        sql = f"SELECT funktion from funktionen WHERE userid=\'{userid}\';"
        ergebnis = cur.execute(sql).fetchall()
        print(ergebnis)
        return ergebnis

    def scrollbar_init(self):
        self.scrollbar = Scrollbar(self, width=10)

        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)

        self.scrollbar.pack(side=RIGHT, fill=BOTH)

