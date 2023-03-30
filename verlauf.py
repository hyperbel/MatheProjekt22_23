from tkinter import Frame, Listbox, Scrollbar, END, BOTH, LEFT, RIGHT, ttk

import sqlite3

class Verlauf(Frame):
    def __init__(self, master):
        super().__init__(master, width=30)
        self.verlauf = self.get_verlauf(1)
        self.listbox = Listbox(self, width=20, height=100)
        for i in self.verlauf:
            self.listbox.insert(END, i[0])
        self.listbox.pack(side=LEFT, fill=BOTH, expand=True)

        self.scrollbar_init()
        self.combobox_init()
        self.button_init()

    def get_verlauf(self, userid: int):
        con = sqlite3.connect("mathe.db")
        cur = con.cursor()
        userid=1
        sql = f"SELECT funktion from funktionen WHERE userid=\'{userid}\';"
        ergebnis = cur.execute(sql).fetchall()
        print(ergebnis)
        return ergebnis

    def remove_verlauf (self, userid: int, zeit: str):
        print("lol")

    def scrollbar_init(self):
        self.scrollbar = Scrollbar(self, width=10)

        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)

        self.scrollbar.pack(side=RIGHT, fill=BOTH)

    def combobox_init(self):
        self.combobox_values = ['5 min', '10 min', '15 min', '1 std', '24 std', 'alles löschen']
        self.combobox = ttk.Combobox(self, values=self.combobox_values)
        self.combobox.pack(side=LEFT, padx=5, pady=5)

    def button_init(self):
        self.button = ttk.Button(self, text='Löschen', command=self.delete_selection)
        self.button.pack(side=LEFT, padx=5, pady=5)

    def delete_selection(self):
        selection = self.combobox.get()
        if selection == 'alles löschen':
            self.listbox.delete(0, END)
        else:
              # MM-DD-YYYY HH:MM
            self.remove_verlauf(1, "03.30.2023 09:30")
