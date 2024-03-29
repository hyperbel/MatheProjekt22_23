""" Verlauf Logik """
import sqlite3
import time
import re
from tkinter import Frame, Listbox, Scrollbar, END, BOTH, LEFT, RIGHT, ttk, BOTTOM, messagebox
from mainwindowbase import BaseWindow 


class Verlauf(Frame):
    """ Verlauf Klasse """
    def __init__(self, master, parent: BaseWindow):
        super().__init__(master, width=30)

        self.parent = parent

        self.con = sqlite3.connect("mathe.db")
        self.cur = self.con.cursor()

        self.verlauf = self.get_verlauf(1)
        self.listbox = Listbox(self, width=20)
        for i in self.verlauf:
            self.listbox.insert(END, i[0])

        self.listbox.bind('<Double-Button-1>', self.on_double_click)

        self.scrollbar_init()
        self.delete_frame_init()
        self.listbox.pack(side=LEFT, fill=BOTH, expand=True)
        self.userid=1

    def on_double_click(self, event):
        """ Öffnet die Funktion aus dem Verlauf
        :param event: Eventdaten
        """

        widget = event.widget
        selection = widget.curselection()
        if selection:
            index = selection[0]
            item = widget.get(index)
            if item:
                self.open_funktion_aus_verlauf(item)

    def open_funktion_aus_verlauf(self, _):
        """ Öffnet die Funktion aus dem Verlauf
        :param _: Eventdaten, brauchen wir hier nicht
        """
        selection = self.listbox.curselection()
        if selection:
            index = selection[0]
            funktion = self.listbox.get(index)
            if re.search("x", funktion):
                if re.search("\*", funktion):
                    self.parent.select_by_name("integralrechnung", funktion=funktion)
                    #print("integralrechnung")
                else:
                    self.parent.select_by_name("term_eingeben", funktion=funktion)
                    #print("term_eingeben")
            else:
                num_commas = funktion.count(",")
                if num_commas == 2:
                    self.parent.select_by_name("trigonometrische", funktion=funktion)
                    #print("trigonometrische")
                else:
                    self.parent.select_by_name("exponential", funktion=funktion)
                    #print("exponential")


    def get_verlauf(self, userid: int) -> list:
        """ Holt den Verlauf aus der Datenbank
        :param userid: User ID, immer 1 loool
        :return: Verlauf
        :rtype: list
        """
        sql = f"SELECT funktion from funktionen WHERE userid=\'{userid}\';"
        ergebnis = self.cur.execute(sql).fetchall()
        #print(ergebnis)
        return ergebnis

    
    def remove_verlauf(self, userid: int, minu: str, std: str):
        """ Löscht den Verlauf aus der Datenbank
        :param userid: User ID, immer 1 loool
        :return: Verlauf
        :rtype: list
        """
        try:
            aktuelle_zeit = time.strftime("%H:%M:%S")
            zeit = time.strftime("%H:%M:%S", time.strptime(f"{std}:{minu}:00", "%H:%M:%S"))
            aktuelle_zeit_in_sec = sum(x * int(t) for x, t in zip([3600, 60, 1], aktuelle_zeit.split(":")))
            zeit_in_sec = sum(x * int(t) for x, t in zip([3600, 60, 1], zeit.split(":")))
            alte_zeit_in_sec = aktuelle_zeit_in_sec - zeit_in_sec
            alte_zeit = time.strftime("%H:%M:%S", time.gmtime(alte_zeit_in_sec))
            sql = f"DELETE FROM funktionen WHERE zeit BETWEEN '{alte_zeit}' AND '{aktuelle_zeit}' AND userid = '1';"
        except:
            _ = messagebox.showwarning(title="Fehler", message="Fehler beim Löschen")

    def scrollbar_init(self):
        """ Scrollbar wird erstellt"""
        self.scrollbar = Scrollbar(self, width=10)

        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)

        self.scrollbar.pack(side=RIGHT, fill=BOTH)

    def combobox_init(self, parent):
        """ Lösch Auswahl wird erstellt
        :param parent: Parent Widget
        """
        self.combobox_values = ['5 min', '10 min', '15 min', '30 min', '1 std', '2 std', '8 std', '24 std', 'alles löschen']
        self.combobox = ttk.Combobox(parent, values=self.combobox_values)
        self.combobox.current(0)
        self.combobox.pack(side=LEFT, padx=5, pady=5)

    def button_init(self, parent):
        """ Löschen Button wird erstellt
        :param parent: Parent Widget
        """
        self.button = ttk.Button(parent, text='Löschen', command=self.delete_selection)
        self.button.pack(side=LEFT, padx=5, pady=5)

    def delete_selection(self):
        """ Löscht die Auswahl aus dem Verlauf
        """
        selection = self.combobox.get()
        if selection == 'alles löschen':
            self.listbox.delete(0, END)
            self.cur.execute("DELETE FROM funktionen;")
            self.con.commit()
        elif selection == '5 min':
            self.remove_verlauf(1,'05',0)
        elif selection == '10 min':
           self.remove_verlauf(1,10,0)
        elif selection == '15 min':
           self.remove_verlauf(1,15,0)
        elif selection == '30 min':
            self.remove_verlauf(1,30,0)
        elif selection == '1 std':
            self.remove_verlauf(1,0,1)
        elif selection == '2 std':
            self.remove_verlauf(1,0,2)
        elif selection == '8 std':
            self.remove_verlauf(1,0,8)
        elif selection == '24 std':
            self.remove_verlauf(1,0,24)
        else:
           _ = messagebox.showinfo(title="Auswahl ungültig", message="Sie müssen in der Combobox etwas auswählen")

    def delete_frame_init(self):
        """ Löschen Frame wird erstellt
        """
        self.delete_frame = Frame(self)
        self.combobox_init(self.delete_frame)
        self.button_init(self.delete_frame)
        self.delete_frame.pack(side=BOTTOM, fill=BOTH)

    def appendieren(self, funktion):
        """ Fügt die Funktion in den Verlauf ein
        :param funktion: Funktion die hinzugefügt werden soll
        :type funktion: str
        """
        self.listbox.insert(END, funktion)
        sql = "INSERT INTO funktionen (userid, funktion) VALUES (?, ?);"
        self.cur.execute(sql, (self.userid, funktion))
        self.con.commit()
