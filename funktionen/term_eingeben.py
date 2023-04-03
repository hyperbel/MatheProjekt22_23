from math import sqrt
import re
import utils
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from functionframe import FunktionFrame
from tkinter import Label, NW, TOP, Entry, Button, NE, LEFT, BOTH
from verlauf import Verlauf
from oop import MainWindow

class TermEingeben(FunktionFrame):
    def __init__(self, master, parent: MainWindow):
        super().__init__(master)
        self.parent = parent

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
        Button(self, text="?", command=self.get_help).pack(side=TOP, anchor=NE)

        _b.pack(side=TOP, anchor=NW)

        self.fig = plt.Figure(figsize=(10, 10), dpi=125)

        self.pack(side=LEFT, fill=BOTH, expand=False)

    def basis_funktion(self) -> str:
        return self.f_entry.get()

    def get_help(self) -> None:
        """ ruft das hilfefenster auf """
        _help = utils.base_tk(size="800x500", name="Hilfe - Funktionen")
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

        self.verlauf_appendieren(self.parent.get_verlauf())

        # holt input und bereinigt ihn
        self.basis_exponent_paare = self.basis_exponent_paare_holen(self.f_entry.get())

        # erstellt plot

        self.fig.clear()

        x_werte = np.arange(-100, 200, 0.1)
        self.ax = self.fig.add_subplot()
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

        self.canvas.get_tk_widget().destroy() if hasattr(self, "canvas") else None
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.draw()

        kurvendiskussion_button = Button(self,
                                         text="Kurvendiskussion",
                                         command=self.kurvendiskussion)
        kurvendiskussion_button.pack(side=TOP, anchor=NW)
        self.canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True)

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

    def get_term(self, term: str) -> tuple[int,int]:
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


    def ableitung_ersteller(self, inp: str) -> str:
        """ berechnet die ableitung einer funktion """
        basis_exponent_paare = self.basis_exponent_paare_holen(inp)
        ableitung = ""
        for basis, exponent in basis_exponent_paare:
            if exponent == 0:
                continue
            term = f"{basis * exponent}x^{exponent - 1}"
            if term[-1] == '0':
                term = term[:-3]
            if term[0] == '-':
                ableitung += f"-{term[1:]}"
            else:
                ableitung += f"+{term}"
            
        return ableitung

    def verlauf_appendieren(self, verlauf: Verlauf) -> None:
        verlauf.appendieren(self.basis_funktion())

    def funktionsgrad_bestimmen(self, funktion) -> int:
        """ gibt den funktionsgrad einer funktion zurück """
        basis_exponent_paare = self.basis_exponent_paare_holen(funktion)
        return max([int(x[1]) for x in basis_exponent_paare])


    # TODO: implementieren
    def nullstellen(self, funktion) -> list[float]:

        funktionsgrad = self.funktionsgrad_bestimmen(funktion)

        basis_exponent_paare = self.basis_exponent_paare_holen(funktion)

        # pq Formel
        if funktionsgrad == 2:
            normiert_p = basis_exponent_paare[1][0] / basis_exponent_paare[0][0]
            normiert_q = basis_exponent_paare[2][0] / basis_exponent_paare[0][0]
            x1, x2 = self.pq_formel(normiert_p, normiert_q)
            return [x1, x2]

        return []

    def pq_formel(self, p: float, q: float) -> tuple[float, float]:
        """ berechnet die nullstellen einer quadratischen funktion """
        # -p/2 +- sqrt((p/2)^2 - q)
        x1 = (-(p/2)) + sqrt((p/2)**2 - q)
        x2 = (-(p/2)) - sqrt((p/2)**2 - q)

        return x1, x2


    def kurvendiskussion(self) -> None:
        # funktionsgrad
        # nullstellen (f(x) = 0)
        nullstellen = self.nullstellen(self.basis_funktion())
        # ableitung
        ableitung = self.ableitung_ersteller(self.basis_funktion())
        zweite_ableitung = self.basis_exponent_paare_holen(ableitung)

        # extremstellen (f'(x) = 0)
        # wendepunkte (f''(x) = 0)
