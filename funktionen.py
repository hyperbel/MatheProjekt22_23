"""@package funktionen
hier werden die Frames fuer die Funktionen definiert
"""
from tkinter import Frame, Label, Entry, Button, TOP, LEFT, BOTH, NW, NE, END, StringVar, messagebox
import utils
import matplotlib.pyplot as plt
import numpy as np
import re
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class FunktionFrame(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
    
    def verlauf_appendieren(self) -> None:
        """ fuegt die funktion in den Verlauf ein 
            soll überschrieben werden"""
        raise NotImplementedError


class Ganzrational(FunktionFrame):
    def __init__(self, master):
        super().__init__(master)
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

        self.canvas = FigureCanvasTkAgg(fig, master=self)
        self.canvas.draw()

        kurvendiskussion_button = Button(self,
                                         text="Kurvendiskussion",
                                         command=self.kurvendiskussion)
        kurvendiskussion_button.pack(side=TOP, anchor=NW)
        self.canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=False)

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

class Exponential(FunktionFrame):
    def __init__(self, master):
        super().__init__(master)
        self.von_entry = Entry(self)
        self.bis_entry = Entry(self)
        self.a_entry = Entry(self)
        # x_label = Label(self, text="x: ")
        # x_entry = Entry(self)
        self.x_achse_entry = Entry(self)
        self.y_achse_entry = Entry(self)

        # figure for matplotlib to plot lines on
        fig = plt.Figure(figsize=(10, 10), dpi=100)

        # canvas-like thing for actually draselfg
        self.ax = fig.add_subplot()

        self.create_widgets()

        # range of numhers, see numpy.org for doc on arange
        # put canvas onto tk selfdow
        self.canvas = FigureCanvasTkAgg(fig, master=self)

    # function in function to be used on button click
    def exponential_ausrechnen(self) -> None:
        """ berechnet die funktion """
        # werte holen
        von = float(self.von_entry.get())
        bis = float(self.bis_entry.get())
        a = float(self.a_entry.get())
        # x = float(x_entry.get())

        # checken ob werte floats sind
        assert utils.entry_is_float(von)
        assert utils.entry_is_float(bis)
        assert utils.entry_is_float(a)
        # assert entry_is_float(x)

        # range mit von - bis
        self.x_werte = np.arange(von, bis, 0.2)

        # setze namen der achsen
        self.ax.set_xlabel(self.x_achse_entry.get())
        self.ax.set_ylabel(self.y_achse_entry.get())

        # lineare funktion plotten
        self.ax.plot(self.x_werte, a ** self.x_werte)

        self.canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True)
        self.canvas.draw()

    def exponential_help(self) -> None:
        pass

    def create_widgets(self):
        # display everything
        Label(self, text="anfang: ").pack(side=TOP, anchor=NW)
        self.von_entry.pack(side=TOP, anchor=NW)
        Label(self, text="ende: ").pack(side=TOP, anchor=NW)
        self.bis_entry.pack(side=TOP, anchor=NW)
        Label(self, text="a: ").pack(side=TOP, anchor=NW)
        self.a_entry.pack(side=TOP, anchor=NW)
        Label(self, text="x-Achsenbeschriftung:").pack(side=TOP, anchor=NW)
        self.x_achse_entry.pack(side=TOP, anchor=NW)
        Label(self, text="y-Achsenbeschriftung:").pack(side=TOP, anchor=NW)
        self.y_achse_entry.pack(side=TOP, anchor=NW)

        # use function declared earlier to compute stuff
        Button(self, command=self.exponential_ausrechnen, text="Anzeigen").pack(side=TOP,
                                                                     anchor=NW)
        Button(self, text="?", command=self.exponential_help).pack(side=TOP, anchor=NE)


class Trigonometrische(FunktionFrame):
    def __init__(self, master):
        super().__init__(master)

    def create_widgets(self):
        self.amplitude_label =  Label(self, text="Amplitude:")
        self.amplitude_entry = Entry(self)
        self.frequenz_label = Label(self, text="Frequenz:")
        self.frequenz_entry = Entry(self)
        self.phase_label = Label(self, text="Phase:")
        self.phase_entry = Entry(self)
        self.function_type_var = StringVar(value='sin')

        # figure for matplotlib to plot lines on
        self.fig = plt.Figure(figsize=(10, 10), dpi=100)

        # canvas-like thing for actually draselfg
        self.ax = self.fig.add_subplot()

        self.canvas = FigureCanvasTkAgg(self.fig, master=self)


    def trigonometrische_ausrechnen(self):
       try:
            self.amp = float(self.amplitude_entry.get())
            self.freq = float(self.frequenz_entry.get())
            self.phase = float(self.phase_entry.get())

                # checken ob werte floats sind
            assert utils.entry_is_float(self.amp)
            assert utils.entry_is_float(self.freq)
            assert utils.entry_is_float(self.phase)
       except:
            error = messagebox.showerror(title="Inkorekte eingabe", message="Sie müssen richtige Werte in die Textbox eingeben, bei hilfe einfach auf das ? klicken", **options)
       # assert entry_is_float(x)

        # x-Werte des Graphen berechnen
        
       self.x = np.linspace(0, 2*np.pi, 1000)

       if self.function_type_var.get() == 'sin':
           self.y = self.amp * np.sin(self.freq * self.x + self.phase)
           self.title = 'Sinusfunktion'
       elif self.function_type_var.get() == 'cos':
           self.y = self.amp * np.cos(self.freq * self.x + self.phase)
           self.title = 'Cosinusfunktion'
       elif self.function_type_var.get() == 'tan':
           self.y = self.amp * np.tan(self.freq * self.x + self.phase)
           self.title = 'Tangensfunktion'
        
       self.ax.clear()
       self.ax.plot(self.x, self.y)
       self.ax.set_xlabel('x')
       self.ax.set_ylabel('y')
       self.ax.set_title(self.title)
       self.canvas.draw()
        # range mit von - bis
       self.canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True)
       self.canvas.draw()



class Integralrechnung(FunktionFrame):
    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()

    def create_widgets(self):
        self.funktion_label =  Label(self, text="Funktion:")
        self.funktion_entry = Entry(self)
        self.anfangX_label = Label(self, text="Anfang von X:")
        self.anfangX_entry = Entry(self)
        self.endeX_label = Label(self, text="Ende von X:")
        self.endeX_entry = Entry(self)  

        self.y_label = Label(self, text="Y:")
        self.y_entry = Entry(self)
        self.loesung_label = Label(self, text="Lösung")
        self.loesung_entry = Entry(self)

        fig = plt.Figure(figsize=(10, 10), dpi=100)

        # canvas-like thing for actually drawing
        self.ax = fig.add_subplot()

        # range of numhers, see numpy.org for doc on arange
        # put canvas onto tk window
        self.canvas = FigureCanvasTkAgg(fig, master=self)

    def integral_ausrechnen(self):
        # Hohle Werte
        funktion_text = self.funktion_entry.get()
        anfangx = float(self.anfangX_entry.get())
        endex = float(self.endeX_entry.get())
        y = int(self.y_entry.get())

         # checken ob werte floats sind
        assert utils.entry_is_float(anfangx)
        assert utils.entry_is_float(endex)
        # assert entry_is_float(x)

        # hier wird durch ein bischen numpy Magie das Integral einer Funktion berechnet
        func = lambda x: eval(funktion_text)

        x = np.linspace(anfangx, endex, y)
        y = func(x)
        integral = np.trapz(y, x)

        # Rundet das Ergebnis und gibt es in der Box aus
        ergebnis = round(integral)
        self.loesung_entry.delete(0, END)
        self.loesung_entry.insert(0, str(ergebnis))


        self.canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

        self.ax.clear()
        self.ax.plot(x, y)
        self.ax.fill_between(x, y, 0, alpha=0.2)
        self.ax.set_xlabel('x')
        self.ax.set_ylabel('y')
        self.ax.set_title("Integral")
        self.canvas.draw()
