from tkinter import Tk, Frame, Label, Entry, Button, TOP, LEFT, BOTH, NW, NE, Menu, Listbox, Scrollbar, RIGHT, END
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import re
import numpy as np
import sqlite3

# basic window config
def base_tk(size="900x600", name="") -> Tk:
    """basis window config
    :param size: Größe des Fensters
    :type size: str
    :param name: Name des Fensters
    :type name: str

    :return: das Fenster
    :rtype: Tk
    """
    win = Tk()
    win.geometry(size)
    win.title(name)
    return win

class MainWindow(Tk):
    def __init__(self):
        super().__init__()
        self.title("Mathe Projekt 22/23")
        self.geometry("900x600")

        self.create_menu()
        self.config(menu=self.menu, bg="red")

        self.verlauf = Verlauf(self)
        self.verlauf.pack(side=LEFT, fill=BOTH, expand=False)

    def select_ganzrational(self):
        self.selected_frame = Ganzrational(self)
        self.selected_frame.pack(side=RIGHT, fill=BOTH, expand=True)
        pass

    # generiert main menu fuer das root win
    def create_menu(self) -> None:
        """ generiert main menu für das root win """
        self.menu = Menu(self, tearoff=0)
        funktionen_menu = Menu(self.menu, tearoff=0)
        # account_menu = Menu(_menu, tearoff=0)
        # hilfe_menu = Menu(_menu, tearoff=0)

        funktionen_menu.add_command(label="Ganzrational", command=self.select_ganzrational)

        self.menu.add_cascade(label="Funktionen", menu=funktionen_menu)

        # funktionen_menu.add_command(label="Trigonometrische", command=open_trigonometrische_window)
        # funktionen_menu.add_command(label="Exponential", command=open_exponential_window)
        # # Differenzial Rechnen = Ableitungen, deshalb wir dies in dem anderen Fenster sein
        # funktionen_menu.add_command(label="Integralrechnung", command=open_integralrechnung_window)
        # _menu.add_cascade(label="Funktionen", menu=funktionen_menu)

        # account_menu.add_command(label="Logout", command=self.destroy)
        # _menu.add_cascade(label="Account", menu=account_menu)

        # hilfe_menu.add_command(label="hilfe", command=open_hilfe_window)
        #_menu.add_cascade(label="Hilfe", menu=hilfe_menu)
        # hilfe_menu.add_command(label="über", command=open_ueber_window)




class Ganzrational(Frame):
    def __init__(self, master):
        super().__init__(master, bg="blue")
        Label(self, text="hier Funktionsterm eingeben: ").pack(side=TOP, anchor=NW)

        self.f_entry = Entry(self)
        self.f_entry.pack(side=TOP, anchor=NW)
        # labels & entries for bounds of x and y axis
        Label(self, text="x von, bis: ").pack(side=TOP, anchor=NW)
        self.x_von_bis_entry = Entry(self)
        self.x_von_bis_entry.pack(side=TOP, anchor=NW)
        Label(self, text="y von, bis: ").pack(side=TOP, anchor=NW)
        self.y_von_bis_entry = Entry(self)
        self.y_von_bis_entry.pack(side=TOP, anchor=NW)

        _b = Button(self, text="Los gehts!", command=self.funktion_berechnen)
        Button(self, text="?", command=self._get_help).pack(side=TOP, anchor=NE)

        _b.pack(side=TOP, anchor=NW)

        self.pack(side=LEFT, fill=BOTH, expand=True)

    def _get_help(self) -> None:
        """ ruft das hilfefenster auf """
        _help = base_tk(size="800x500", name="Hilfe - Funktionen")
        Label(_help,
        text="In das Input feld die Funktion eingeben, die exponenten werden mit einem ^ notiert.\n\
                Also z.B.: 1x^3 + 2x^2 + 1x + 0\n\
                Wenn der erste term ein x vorne hat, muss eine 1 davor geschrieben werden!").pack()
        Button(_help, text="Ok", command=_help.destroy).pack()

    # berechnet das richtig dismal lol. ich bin so dumm
    def funktion(self, x_wert: float) -> float:
        """ berechnet die funktion """
        y_wert = 0
        for basis, exponent in self.basis_exponent_paare:
            y_wert += basis * (x_wert ** exponent)
        return y_wert


    def funktion_berechnen(self) -> None:
        """ holt werte und berechnet die funktion """

        # holt input und bereinigt ihn
        self.basis_exponent_paare = self.basis_exponent_paare_holen(self.f_entry.get())

        # erstellt plot
        fig = plt.Figure(figsize=(10, 20), dpi=100)
        x_werte = np.arange(-100, 200, 0.2)
        self.ax = fig.add_subplot()
        self.ax.set_xlabel("x")
        self.ax.set_ylabel("y")
        self.ax.set_title("Funktionsgraph")
        x_von, x_bis = self.von_bis(self.x_von_bis_entry.get())
        self.ax.set_xlim(x_von, x_bis)
        y_von, y_bis = self.von_bis(self.y_von_bis_entry.get())
        self.ax.set_ylim(y_von, y_bis)
        self.ax.grid()
        self.ax.spines.left.set_position('zero')
        self.ax.spines.right.set_color('none')
        self.ax.spines.bottom.set_position('zero')
        self.ax.spines.top.set_color('none')
        self.ax.yaxis.set_ticks_position('left')
        self.ax.xaxis.set_ticks_position('bottom')

        self.ax.scatter(0, 0, color="purple", label="Nullpunkt")



        self.ax.plot(x_werte, self.funktion(x_werte), label="linie")
        # setzt eine Legende in die obere rechte Ecke
        self.ax.legend(loc="upper right")

        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()


        kurvendiskussion_button = Button(self,
                                         text="Kurvendiskussion",
                                         command=self.kurvendiskussion)
        kurvendiskussion_button.pack(side=TOP, anchor=NW)
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True)

    def basis_exponent_paare_holen(self, inp: str) -> list[tuple[float, float]]:
        input_str = self.array_von_leeren_strings_befreien(inp)
        terme = self.get_zahlen(input_str)
        return [self.get_term(t) for t in terme]

    def get_zahlen(self, inp: str) -> list:
        """ holt wichtige zahlen aus dem string
        :param inp: string mit allen zahlen
        :type inp: str
        :return: liste mit allen zahlen
        :rtype: list
        """
        # regex magie um alle zahlen zu finden
        dirty_terme = re.findall(r"[+-]?\d*x?\^?\d*", inp)

        # entfernt alle leeren strings
        terme = [t for t in dirty_terme if t != '']
        return terme

    def get_term(self, term: str) -> tuple:
        """ gibt einen term als tuple zurück (koeffizient, exponent)
        :param term: term als string
        :type term: str
        :return: tuple mit koeffizient und exponent
        :rtype: tuple
        """

        # wenn kein x vorhanden ist, dann ist es ein konstanter term
        if 'x' not in term:
            return int(term), 0
        # wenn kein exponent vorhanden ist, dann ist es ein linearer term
        if '^' not in term:
            return int(term[:-1]), 1
        # sonst ist es ein term mit exponent
        return int(term[:term.index('x')]), int(term[term.index('^')+1:])

    def array_von_leeren_strings_befreien(self, arr: str) -> str:
        """entfernt alle leeren strings aus einem array """
        output_string = ""
        # schaut durch alle items im array und filtert alle leeren strings raus
        for a in arr:
            if a != '':
                output_string += a
        return output_string

    def leerzeichen_raus_machen(self, inp: str) -> str:
        """ entfernt alle leerzeichen aus einem string """
        outp = ""
        # enumeriert über input mit (index, wert)
        for _, character in enumerate(inp):
            if character != " ":
                outp += character
        return outp

    def von_bis(self, get_from: str) -> tuple[float, float]:
        """
        Holt von und bis werde aus einem string (von, bis)
        :param get_from: der string, aus dem die limits geholt werden sollen
        :type get_from: str
        :return: die Werte aus dem String
        :rtype: tuple[float, float]
        """
        input_bereinigt = self.leerzeichen_raus_machen(get_from)
        von, bis = input_bereinigt.split(",")
        return float(von), float(bis)


    def kurvendiskussion(self):
        pass

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

if __name__ == "__main__":
    MainWindow().mainloop()
