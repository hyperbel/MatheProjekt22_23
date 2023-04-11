from math import sqrt, ceil 
import re
import utils
from generator import terme_generator
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from functionframe import FunktionFrame
from tkinter import Label, NW, TOP, Entry, Button, NE, BOTH, Frame, ttk, NE, END,E
from verlauf import Verlauf
from oop import MainWindow

class TermEingeben(FunktionFrame):
    def __init__(self, master, parent: MainWindow, funktion = None):
        super().__init__(master)
        self.parent = parent

        Label(self, text="hier Funktionsterm eingeben: ").grid(row=0, column=0, sticky=NW)


        self.f_entry = Entry(self)
        self.f_entry.grid(row=0, column=1, sticky=NW)

        if funktion != None:
            self.f_entry.insert(END, funktion)

        # labels & entries for bounds of x and y axis
        Label(self, text="x von, bis: ").grid(row=1, column=0, sticky=NW)
        self.x_von_bis_entry = Entry(self)
        self.x_von_bis_entry.grid(row=1, column=1, sticky=NW)
        Label(self, text="y von, bis: ").grid(row=2, column=0, sticky=NW)
        self.y_von_bis_entry = Entry(self)
        self.y_von_bis_entry.grid(row=2, column=1, sticky=NW)


        _b = Button(self, text="anzeigen", command=self.funktion_berechnen)
        Button(self, text="?", command=self.get_help).grid(row=0, column=3, sticky=NE)

        _b.grid(row=5, column=0, sticky=NW)

        # Zeug zum Zoomen und leeren

        self.zoom_control_frame = Frame(self)
        self.zoom_control_frame.grid(row=10, column=0, sticky=NW)
        Button(self.zoom_control_frame, text="Leeren", command=self.clear_canvas).pack(side="right", padx=5, pady=5)

        self.zoom_in_button = Button(self.zoom_control_frame, text="+", command=self.zoom_in)
        self.zoom_out_button = Button(self.zoom_control_frame, text="-", command=self.zoom_out)
        self.zoom_out_button.pack(side="right", padx=5, pady=5)
        self.zoom_in_button.pack(side="right", padx=5, pady=5)

        self.beschriftung_frame = Frame(self)

        # Beschriftungszeug
        self.xbeschriftung_label =  Label(self.beschriftung_frame, text="X-Beschriftung:")
        #self.xbeschriftung_label.pack(side="right", padx=5, pady=5)
        self.xbeschriftung_label.grid(row=0, column=0, sticky=NE)
        self.xbeschriftung_entry = Entry(self)
        self.ybeschriftung_label = Label(self.beschriftung_frame, text="Y-Beschriftung:")
        self.ybeschriftung_entry = Entry(self.beschriftung_frame)
        self.xbeschriftung_entry.grid(row=7, column=1, sticky=NE)
        self.ybeschriftung_label.grid(row=7, column=2, sticky=NE)
        self.ybeschriftung_entry.grid(row=7, column=3, sticky=NE)

        self.figure_frame = Frame(self)
        self.figure_frame.config(width=50, height=50)

        self.fig = plt.Figure(figsize=(5, 5), dpi=125)
        expo_button = ttk.Button(self, text="Beispiel", command=self.term_button_clicked)
        expo_button.grid(row=0, column=4, sticky=NE)


    def clear_canvas(self):
        # if self.ax exists
        self.ax.clear()
        self.canvas.draw()

    def zoom_in(self):
        self.ax.set_xlim(self.ax.get_xlim()[0] * 0.9, self.ax.get_xlim()[1] * 0.9)
        self.ax.set_ylim(self.ax.get_ylim()[0] * 0.9, self.ax.get_ylim()[1] * 0.9)
        self.canvas.draw()

    def zoom_out(self):
        self.ax.set_xlim(self.ax.get_xlim()[0] * 1.1, self.ax.get_xlim()[1] * 1.1)
        self.ax.set_ylim(self.ax.get_ylim()[0] * 1.1, self.ax.get_ylim()[1] * 1.1)
        self.canvas.draw()

    
    def term_button_clicked(self):
        value = terme_generator()
        self.f_entry.delete(0, END)
        self.f_entry.insert(0, value)
        self.ybeschriftung_entry.delete(0, END)
        self.ybeschriftung_entry.insert(0, "Y")
        self.xbeschriftung_entry.delete(0, END)
        self.xbeschriftung_entry.insert(0, "X")
        self.x_von_bis_entry.delete(0, END)
        self.x_von_bis_entry.insert(0, "-10,10")
        self.y_von_bis_entry.delete(0, END)
        self.y_von_bis_entry.insert(0, "-10,10")
        

    def basis_funktion(self) -> str:
        return self.f_entry.get()

    def get_help(self) -> None:
        """ ruft das hilfefenster auf """
        _help = utils.base_tk(size="1000x500", name="Hilfe - Funktionen")
        Label(_help,
        text="In das Input feld die Funktion eingeben, die exponenten werden mit einem ^ notiert.\n\
                Also z.B.: 1x^3 + 2x^2 + 1x + 0\n\
                Wenn der erste term ein x vorne hat, muss eine 1 davor geschrieben werden!\n\
                    \n Quadratische, lineare und ganzrationale Funktionen sind drei wichtige Arten von Funktionen in der Mathematik.\n\
                     Eine quadratische Funktion ist eine Funktion, die durch eine Gleichung der Form f(x) = ax^2 + bx + c beschrieben wird.\n Hierbei sind a, b und c Konstanten und x ist die unabhängige Variable. \nQuadratische Funktionen sind bekannt für ihre charakteristische Parabel-Form und ihre Eigenschaften wie Scheitelpunkt,\n Achsensymmetrie und Nullstellen können aus der Funktionsgleichung abgeleitet werden.\n\
                     \nEine lineare Funktion ist eine Funktion, die durch eine Gleichung der Form f(x) = mx + b beschrieben wird. \nHierbei sind m und b Konstanten und x ist die unabhängige Variable. \nLineare Funktionen sind durch eine Gerade in einem Koordinatensystem dargestellt und ihre Eigenschaften wie Steigung\n und y-Achsenabschnitt können direkt aus der Funktionsgleichung abgeleitet werden.\n\
                     \nGanzrationale Funktionen sind Funktionen, die durch Polynome dargestellt werden,\n d.h. eine Summe von Potenzen der unabhängigen Variablen x. Eine ganzrationale Funktion kann allgemein durch eine Gleichung\n der Form f(x) = a_n*x^n + a_{n-1}x^{n-1} + ... + a_1x + a_0 beschrieben werden,\n wobei n eine natürliche Zahl und a_n, a_{n-1}, ..., a_1, a_0 Konstanten sind.\n Die graphische Darstellung einer ganzrationalen Funktion kann je nach dem Grad des Polynoms\n und den Koeffizienten sehr unterschiedlich aussehen, z.B. \nkönnen sie Schlingen, Wendepunkte oder Asymptoten haben.\n\
                     \n Die Kenntnis dieser drei Funktionsarten ist wichtig, da sie häufig in vielen Bereichen der Mathematik,\n Physik und Ingenieurwissenschaften verwendet werden und ihre Eigenschaften dazu beitragen können, Probleme in diesen Gebieten zu lösen \nund Phänomene zu beschreiben.").grid(row=1, column=0, padx=5, pady=5, sticky=E)
        Button(_help, text="Ok", command=_help.destroy).grid(row=6, column=3, padx=5, pady=5, sticky=E)

        
       

       

    

    # berechnet das richtig dismal lol. ich bin so dumm
    def funktion(self, x_wert: float) -> float:
        """ berechnet die funktion """
        y_wert = 0
        for basis, exponent in self.basis_exponent_paare:
            y_wert += basis * (x_wert ** exponent)
        return y_wert

    def funktion_von(self, x_wert: float, funktion: str) -> float:
        """ berechnet die funktion """
        y_wert = 0
        for basis, exponent in self.basis_exponent_paare_holen(funktion):
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


        self.ax.plot(x_werte, self.funktion(x_werte), label="linie")
        

        # self.ax.scatter(0, 0, color="purple", label="Nullpunkt")
        __nullstellen = self.nullstellen(self.basis_funktion())

        # duplikate entfernen
        _nullstellen = list(dict.fromkeys(__nullstellen))

        nullstellen = []
        for n in _nullstellen:
            if complex(self.funktion(n)).imag == 0:
                nullstellen.append(n.real)


        self.ax.scatter(nullstellen, [0 for _ in nullstellen], color='red', label="Nullpunkte")

        ableitung = self.ableitung_ersteller(self.basis_funktion())
        self.ax.plot(x_werte, self.funktion_von(x_werte, ableitung), label="1. Ableitung")
        
        extrempunkte = self.nullstellen(ableitung)

        if self.funktionsgrad_bestimmen(self.basis_funktion()) > 1:
            zweite_ableitung = self.ableitung_ersteller(ableitung)

            if self.funktionsgrad_bestimmen(self.basis_funktion()) > 2:
                wendepunkte = self.nullstellen(zweite_ableitung)
                self.ax.scatter(extrempunkte, [self.funktion(x) for x in extrempunkte], color='green', label="Extrempunkte")
                self.ax.scatter(wendepunkte, [self.funktion(x) for x in wendepunkte], color='blue', label="Wendepunkte")
                self.ax.plot(x_werte, self.funktion_von(x_werte, zweite_ableitung), label="2. Ableitung")

        
        # setzt eine Legende in die obere rechte Ecke
        self.ax.legend(loc="upper right")

        self.canvas.get_tk_widget().destroy() if hasattr(self, "canvas") else None
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.figure_frame)
        self.canvas.draw()

        self.canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=False)

        self.figure_frame.grid(row=9, column=0, sticky="nsew")

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
        if len(basis_exponent_paare) == 0:
            return 1
        return max([int(x[1]) for x in basis_exponent_paare])


    def nullterme_reinhauen(self, _funktion) -> str:
        """ fügt nullterme in eine funktion ein 
            beispiel: 2x^4 + 3x^2 -5x + 2
            wird zu:  2x^4 + 0x^3 + 3x^2 -5x + 0x + 2

            beispiel: 2x^4 + 0x^3 + 0x^2 - 5x + 0
        """
        funktionsgrad = self.funktionsgrad_bestimmen(_funktion)
        basis_exponent_paare = self.basis_exponent_paare_holen(_funktion)
        funktion = ""
        # soll runter zählen, bis 0, deswegen -1 bei
        for i in range(funktionsgrad, -1, -1):
            b = 0
            for x in basis_exponent_paare:
                if i == x[1]:
                    b = x[0]
            match i:
                case 0:
                    if b > -1:
                        funktion += f"+{b}"
                    else:
                        funktion += f"{b}"
                case 1:
                    if b > -1:
                        funktion += f"+{b}x"
                    else:
                        funktion += f"{b}x"
                case _:
                    if b > -1:
                        funktion += f"+{b}x^{i}"
                    else:
                        funktion += f"{b}x^{i}"

        return funktion

    def teiler_bestimmen(self, funktion) -> int:
        """ bestimmt den ersten teiler, dass die funktion 0 ergibt"""
        basis_exponent_paare = self.basis_exponent_paare_holen(funktion)
        lin_term = basis_exponent_paare[-1][0]
        def alle_teiler_bestimmen():
            teiler = []
            teiler_range = range(-ceil(abs(lin_term)), ceil(abs(lin_term)+1))
            for i in teiler_range:
                if i == 0:
                    continue
                if lin_term % i == 0:
                    teiler.append(i)
            return teiler

        alle_teiler = alle_teiler_bestimmen()

        for teiler in alle_teiler:
            erg = self.einsetzen(funktion, teiler)
            if erg == 0:
                return teiler

        return 0


    def einsetzen(self, funktion: str, wert: float) -> float:
        """ gibt den wert einer funktion an einem bestimmten punkt zurück """
        basis_exponent_paare = self.basis_exponent_paare_holen(funktion)
        end_wert = 0
        for basis, exponent in basis_exponent_paare:
            match exponent:
                case 0:
                    end_wert += basis
                case 1:
                    end_wert += basis * wert
                case _:
                    end_wert += basis * (wert ** exponent)
        return end_wert



    def nullstellen(self, _funktion) -> list[float]:


        funktion = self.nullterme_reinhauen(_funktion)
        funktionsgrad = self.funktionsgrad_bestimmen(funktion)
        basis_exponent_paare = self.basis_exponent_paare_holen(funktion)

        roots = []

        match funktionsgrad:
            # term umformung (zb: 2x + 1)
            # 0 = 2x + 1
            # -1 = 2x
            # -0.5 = x
            # das aber in einer zeile
            case 1:
                if basis_exponent_paare[1][0] != 0 and basis_exponent_paare[0][0] != 0:
                    roots = [-(basis_exponent_paare[1][0]) / basis_exponent_paare[0][0]]
            # pq Formel (zb: x^2 + 2x + 1)
            case 2:
                x1, x2 = self.pq_formel_von(funktion)
                if x1 != None and x2 != None:
                    roots = [x1, x2]
            # sonst polynomdivision
            case _:
                gute_funktion = self.nullterme_reinhauen(funktion)
                diese_basis_exponent_paare = self.basis_exponent_paare_holen(gute_funktion)
                werte = [basis_exponent_paar[0] for basis_exponent_paar in diese_basis_exponent_paare]

                roots = np.roots(werte)


        return roots



    def pq_formel_von(self, funktion: str) -> tuple[float,float]:
        gute_funktion = self.nullterme_reinhauen(funktion)
        basis_exponent_paare = self.basis_exponent_paare_holen(gute_funktion)
        normiert_p = basis_exponent_paare[1][0] / basis_exponent_paare[0][0]
        normiert_q = basis_exponent_paare[2][0] / basis_exponent_paare[0][0]
        x1, x2 = self.pq_formel(normiert_p, normiert_q)
        return x1, x2

    def pq_formel(self, p: float, q: float) -> tuple[float, float]:
        """ berechnet die nullstellen einer quadratischen funktion """
        # -p/2 +- sqrt((p/2)^2 - q)
        try:
            x1 = (-(p/2)) + sqrt((p/2)**2 - q)
            x2 = (-(p/2)) - sqrt((p/2)**2 - q)
        except:
            return None, None

        return x1, x2
