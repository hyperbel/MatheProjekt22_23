import sqlite3
from tkinter import Frame, Listbox, Scrollbar, END, BOTH, LEFT, RIGHT, ttk, BOTTOM


class Verlauf(Frame):
    def __init__(self, master):
        super().__init__(master, width=30)

        self.con = sqlite3.connect("mathe.db")
        self.cur = self.con.cursor()

        self.verlauf = self.get_verlauf(1)
        self.listbox = Listbox(self, width=20)
        for i in self.verlauf:
            self.listbox.insert(END, i[0])

        self.scrollbar_init()
        self.delete_frame_init()
        self.listbox.pack(side=LEFT, fill=BOTH, expand=True)
        self.userid=1

    def get_verlauf(self, userid: int):
        sql = f"SELECT funktion from funktionen WHERE userid=\'{userid}\';"
        ergebnis = self.cur.execute(sql).fetchall()
        #print(ergebnis)
        return ergebnis

    def remove_verlauf (self, userid: int, zeit: str):
        pass

    def scrollbar_init(self):
        self.scrollbar = Scrollbar(self, width=10)

        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)

        self.scrollbar.pack(side=RIGHT, fill=BOTH)

    def combobox_init(self, parent):
        self.combobox_values = ['5 min', '10 min', '15 min', '30 min', '1 std', '2 std', '8 std', '24 std', 'alles löschen']
        self.combobox = ttk.Combobox(parent, values=self.combobox_values)
        self.combobox.pack(side=LEFT, padx=5, pady=5)

    def button_init(self, parent):
        self.button = ttk.Button(parent, text='Löschen', command=self.delete_selection)
        self.button.pack(side=LEFT, padx=5, pady=5)

    def delete_selection(self):
        selection = self.combobox.get()
        if selection == 'alles löschen':
            self.listbox.delete(0, END)
            self.cur.execute("DELETE FROM funktionen;")
            self.con.commit()
        else:
            # MM-DD-YYYY HH:MM
            self.remove_verlauf(1, "03.30.2023 09:30")

    def delete_frame_init(self):
        self.delete_frame = Frame(self)
        self.combobox_init(self.delete_frame)
        self.button_init(self.delete_frame)
        self.delete_frame.pack(side=BOTTOM, fill=BOTH)

    def appendieren(self, funktion):
        self.listbox.insert(END, funktion)
        sql = "INSERT INTO funktionen (userid, funktion) VALUES (?, ?);"
        self.cur.execute(sql, (self.userid, funktion))
        self.con.commit()
