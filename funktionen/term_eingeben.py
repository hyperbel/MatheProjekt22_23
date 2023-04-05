from math import sqrt, ceil
import re
import utils
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from functionframe import FunktionFrame
from tkinter import Label, NW, TOP, Entry, Button, NE, LEFT, BOTH, Frame, ttk
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

        # Beschriftungszeug
        self.xbeschriftung_label =  Label(self, text="X-Beschriftung:")
        self.xbeschriftung_entry = Entry(self)
        self.ybeschriftung_label = Label(self, text="Y-Beschriftung:")
        self.ybeschriftung_entry = Entry(self)
        self.xbeschriftung_label.pack(side="right", padx=5, pady=5)
        self.xbeschriftung_entry.pack(side="right", padx=5, pady=5)
        self.ybeschriftung_label.pack(side="right", padx=5, pady=5)
        self.ybeschriftung_entry.pack(side="right", padx=5, pady=5)

        # Zeug zum Zoomen und leeren
        self.zoom_in_button = Button(self, text="+", command=self.zoom_in)
        self.zoom_out_button = Button(self, text="-", command=self.zoom_out)
        self.zoom_combobox = ttk.Combobox(self, values=["25%", "50%", "75%", "100%"], state="readonly", width=5)
        self.zoom_combobox.current(3)  # standardmäßig 100% auswählen
        self.zoom_out_button.pack(side="right", padx=5, pady=5)
        self.zoom_in_button.pack(side="right", padx=5, pady=5)
        self.zoom_combobox.pack(side="right", padx=5, pady=5)

        _b = Button(self, text="Los gehts!", command=self.funktion_berechnen)
        Button(self, text="?", command=self.get_help).pack(side=TOP, anchor=NE)

        _b.pack(side=TOP, anchor=NW)

        self.figure_frame = Frame(self)
        # set frame size of frame
        self.figure_frame.config(width=100, height=100)


        self.fig = plt.Figure(figsize=(10, 10), dpi=125)

        self.pack(side=LEFT, fill=BOTH, expand=False)

    def zoom_in(self):
        self.ax.set_xlim(self.ax.get_xlim()[0] * 0.9, self.ax.get_xlim()[1] * 0.9)
        self.ax.set_ylim(self.ax.get_ylim()[0] * 0.9, self.ax.get_ylim()[1] * 0.9)
        self.canvas.draw()

    def zoom_out(self):
        self.ax.set_xlim(self.ax.get_xlim()[0] * 1.1, self.ax.get_xlim()[1] * 1.1)
        self.ax.set_ylim(self.ax.get_ylim()[0] * 1.1, self.ax.get_ylim()[1] * 1.1)
        self.canvas.draw()
    def set_zoom_percentage(self):
        zoom_percentage = int(self.zoom_combobox.get().replace("%", ""))
        current_xlim = self.ax.get_xlim()
        current_ylim = self.ax.get_ylim()
        new_range_x = (current_xlim[1] - current_xlim[0]) / zoom_percentage * 100
        new_range_y = (current_ylim[1] - current_ylim[0]) / zoom_percentage * 100
        mid_x = sum(current_xlim) / 2
        mid_y = sum(current_ylim) / 2
        self.ax.set_xlim(mid_x - new_range_x / 2, mid_x + new_range_x / 2)
        self.ax.set_ylim(mid_y - new_range_y / 2, mid_y + new_range_y / 2)
        self.canvas.draw()

        self.zoom_combobox.bind("<<ComboboxSelected>>", lambda event: self.set_zoom_percentage())


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

        # Beschreibung hohlen
        xbeschr = self.xbeschriftung_entry.get()
        ybeschr = self.ybeschriftung_entry.get()

        # holt input und bereinigt ihn
        self.basis_exponent_paare = self.basis_exponent_paare_holen(self.f_entry.get())

        # erstellt plot

        self.fig.clear()

        x_werte = np.arange(-100, 200, 0.1)
        self.ax = self.fig.add_subplot()
        self.ax.set_xlabel(xbeschr)
        self.ax.set_ylabel(ybeschr)
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
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.figure_frame)
        self.canvas.draw()

        kurvendiskussion_button = Button(self,
                                         text="Kurvendiskussion",
                                         command=self.kurvendiskussion)
        kurvendiskussion_button.pack(side=TOP, anchor=NW)
        self.canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=False)

        self.figure_frame.pack(side=LEFT, fill=BOTH, expand=False)

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


    def nullterme_reinhauen(self, funktion) -> str:
        """ fügt nullterme in eine funktion ein 
            beispiel: 2x^4 + 3x^2 -5x + 2
            wird zu:  2x^4 + 0x^3 + 3x^2 -5x + 0x + 2

            beispiel: 2x^4 + 0x^3 + 0x^2 - 5x + 0
        """
        funktionsgrad = self.funktionsgrad_bestimmen(funktion)
        basis_exponent_paare = self.basis_exponent_paare_holen(funktion)
        for i in range(funktionsgrad):
            if i not in [x[1] for x in basis_exponent_paare]:
                funktion += f"+0x^{i}"
        return funktion

    def teiler_bestimmen(self, funktion) -> int:
        """ bestimmt den ersten teiler, dass die funktion 0 ergibt"""
        basis_exponent_paare = self.basis_exponent_paare_holen(funktion)
        lin_term = basis_exponent_paare[-1][0]
        print(lin_term)
        def alle_teiler_bestimmen():
            teiler = []
            for i in range(ceil(lin_term)):
                print(i)
                print(lin_term % i)
                if lin_term % i == 0:
                    print(teiler)
                    teiler.append(i)
            return teiler

        alle_teiler = alle_teiler_bestimmen()
        print(alle_teiler)

        for teiler in alle_teiler:
            erg = self.einsetzen(funktion, teiler)
            if erg == 0:
                return teiler

        raise Exception("kein teiler gefunden")


    def einsetzen(self, funktion: str, wert: float) -> float:
        """ gibt den wert einer funktion an einem bestimmten punkt zurück """
        basis_exponent_paare = self.basis_exponent_paare_holen(funktion)
        wert = 0
        for basis, exponent in basis_exponent_paare:
            wert += basis * (wert ** exponent)
        return wert



    def nullstellen(self, funktion) -> list[float]:

        funktionsgrad = self.funktionsgrad_bestimmen(funktion)

        basis_exponent_paare = self.basis_exponent_paare_holen(funktion)

        match funktionsgrad:
            # term umformung (zb: 2x + 1)
            # 0 = 2x + 1
            # -1 = 2x
            # -0.5 = x
            # das aber in einer zeile
            case 1:
                return [-(basis_exponent_paare[1][0]) / basis_exponent_paare[0][0]]
            # pq Formel (zb: x^2 + 2x + 1)
            case 2:
                normiert_p = basis_exponent_paare[1][0] / basis_exponent_paare[0][0]
                normiert_q = basis_exponent_paare[2][0] / basis_exponent_paare[0][0]
                x1, x2 = self.pq_formel(normiert_p, normiert_q)
                return [x1, x2]
            # sonst polynomdivision
            case _:
                gute_funktion = self.nullterme_reinhauen(funktion)
                diese_basis_exponent_paare = self.basis_exponent_paare_holen(gute_funktion)
                werte = [basis_exponent_paar[0] for basis_exponent_paar in diese_basis_exponent_paare]

                quo, rest = np.polydiv(werte, [1, self.teiler_bestimmen(funktion)])
                if rest:
                    raise Exception("rest nicht 0")

                return quo.tolist()

    def pq_formel(self, p: float, q: float) -> tuple[float, float]:
        """ berechnet die nullstellen einer quadratischen funktion """
        # -p/2 +- sqrt((p/2)^2 - q)
        x1 = (-(p/2)) + sqrt((p/2)**2 - q)
        x2 = (-(p/2)) - sqrt((p/2)**2 - q)

        return x1, x2


    def kurvendiskussion(self) -> None:
        # funktionsgrad
        funktionsgrad = self.funktionsgrad_bestimmen(self.basis_funktion())
        # nullstellen (f(x) = 0)
        nullstellen = self.nullstellen(self.basis_funktion())
        # ableitung
        ableitung = self.ableitung_ersteller(self.basis_funktion())
        zweite_ableitung = self.basis_exponent_paare_holen(ableitung)

        # extremstellen (f'(x) = 0)
        # wendepunkte (f''(x) = 0)
