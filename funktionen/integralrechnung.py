from functionframe import FunktionFrame
from tkinter import Label, Entry, BOTH, NW, TOP, END, Button, messagebox,ttk, NE, LEFT,RIGHT, PhotoImage, Canvas, Frame, END, W, E, NSEW
import tkinter.constants as tkc
import utils
from generator import integral_generator
import numpy as np
import matplotlib.pyplot as plt
from verlauf import Verlauf
import sqlite3
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from oop import MainWindow

class Integralrechnung(FunktionFrame):
    def __init__(self, master, funktion = None):
        super().__init__(master)
        self.create_widgets()

        if funktion != None:
            self.funktion_entry.insert(END, funktion)

    def basis_funktion(self) -> str:
        return self.funktion_entry.get()

    def verlauf_appendieren(self, verlauf: Verlauf) -> None:
        verlauf.appendieren(self.basis_funktion())

    def get_help(self) -> None:
        """ ruft das hilfefenster auf """
        _help = utils.base_tk(size="1000x500", name="Hilfe - Funktionen")
        Label(_help,
        text="In das Input feld die Funktion eingeben, die exponenten werden mit einem ** notiert.\n\
                Also z.B.: x**1\n\
                \nDas Integralrechnen ist ein Zweig der Analysis, der sich mit der Berechnung von Flächen unter einer Kurve,\n dem Bestimmen von Volumina und Schwerpunkten von dreidimensionalen Objekten sowie der Lösung von Differentialgleichungen befasst,\n indem es die Umkehrung des Differenzierens darstellt.").grid(row=1, column=0, padx=5, pady=5, sticky=E)
        Button(_help, text="Ok", command=_help.destroy).grid(row=6, column=3, padx=5, pady=5, sticky=E)

        _help.image = img

    def clear_canvas(self):
        self.loesung_entry.delete(0, END)
        self.funktion_entry.delete(0, END)
        self.ax.clear()
        self.canvas.draw()
    
    def trigo_button_clicked(self):
        value = integral_generator()
        self.funktion_entry.delete(0, END)
        self.funktion_entry.insert(0, value)
        self.ybeschriftung_entry.delete(0, END)
        self.xbeschriftung_entry.delete(0, END)
        self.xbeschriftung_entry.insert(0, "X")
        self.ybeschriftung_entry.insert(0, "Y")

    def create_widgets(self):
        self.funktion_label =  Label(self, text="Funktion:")
        self.funktion_entry = Entry(self)
        """self.anfangX_label = Label(self, text="Anfang von X:")
        self.anfangX_entry = Entry(self)
        self.endeX_label = Label(self, text="Ende von X:")
        self.endeX_entry = Entry(self)  
        self.y_label = Label(self, text="Y:")
        self.y_entry = Entry(self)"""
        self.xbeschriftung_label =  Label(self, text="X-Beschriftung:")
        self.xbeschriftung_entry = Entry(self)
        self.ybeschriftung_label = Label(self, text="Y-Beschriftung:")
        self.ybeschriftung_entry = Entry(self)
        self.loesung_label = Label(self, text="Lösung")
        self.loesung_entry = Entry(self)
        self.zoom_in_button = Button(self, text="+", command=self.zoom_in)
        self.zoom_out_button = Button(self, text="-", command=self.zoom_out)
        self.calculate_button = Button(self, text="anzeigen", command=self.integral_ausrechnen)
        Button(self, text="Leeren", command=self.clear_canvas).grid(row=6, column=2, padx=5, pady=5, sticky=E)
        expo_button = ttk.Button(self, text="Beispiel", command=self.trigo_button_clicked)
        expo_button.grid(row=0, column=3, sticky=NE)
       

        fig = plt.Figure(figsize=(5, 5), dpi=100)

        # canvas-like thing for actually drawing
        self.ax = fig.add_subplot()

        # range of numhers, see numpy.org for doc on arange
        # put canvas onto tk window
        self.canvas = FigureCanvasTkAgg(fig, master=self)

        self.pack_widgets()
        

    def zoom_in(self):
        self.ax.set_xlim(self.ax.get_xlim()[0] * 0.9, self.ax.get_xlim()[1] * 0.9)
        self.ax.set_ylim(self.ax.get_ylim()[0] * 0.9, self.ax.get_ylim()[1] * 0.9)
        self.canvas.draw()

    def zoom_out(self):
        self.ax.set_xlim(self.ax.get_xlim()[0] * 1.1, self.ax.get_xlim()[1] * 1.1)
        self.ax.set_ylim(self.ax.get_ylim()[0] * 1.1, self.ax.get_ylim()[1] * 1.1)
        self.canvas.draw()


    def pack_widgets(self) -> None:
        # Anordnung der Eingabefelder und Beschriftungen oben links
        self.funktion_label.grid(row=0, column=0, sticky=NW)
        self.funktion_entry.grid(row=0, column=1, sticky=NW)
        self.xbeschriftung_label.grid(row=1, column=0, sticky=NW)
        self.xbeschriftung_entry.grid(row=1, column=1, sticky=NW)
        self.ybeschriftung_label.grid(row=2, column=0, sticky=NW)
        self.ybeschriftung_entry.grid(row=2, column=1, sticky=NW)

        # Anordnung des Anzeige-Buttons unter den Input-Feldern
        self.calculate_button.grid(row=4, column=0, sticky=NW)

        # Anordnung der Lösungsfelder rechts von den Beschriftungen
        self.loesung_entry.grid(row=3, column=1, padx=5, pady=5)
        self.loesung_label.grid(row=3, column=0, padx=5, pady=5)
       
        # Anordnung des Berechnen-Buttons unter den Lösungsfeldern
        self.calculate_button.grid(row=5, column=0, padx=5, pady=5)

        # Anordnung der Zoom-Elemente unter den Lösungsfeldern
        self.zoom_out_button.grid(row=6, column=0, padx=5, pady=5)
        self.zoom_in_button.grid(row=6, column=1, padx=5, pady=5)

        # Hilfe-Button in der oberen rechten Ecke
        Button(self, text="?", command=self.get_help).grid(row=0, column=2, sticky=NE)






    def integral_ausrechnen(self):
        # Hohle Werte
        try: 
            funktion_text = self.funktion_entry.get()
            
        except ValueError:
            _ = messagebox.showerror(title="Inkorrekte eingabe", message="Sie müssen richtige Werte in die Textbox eingeben, bei hilfe einfach auf das ? klicken")
            return

        # assert entry_is_float(x)

        self.verlauf_appendieren(self.master.get_verlauf())

        xbeschr = self.xbeschriftung_entry.get()
        ybeschr = self.ybeschriftung_entry.get()
        """
        if xbeschr == None:
            xbeschr = "X"
        if ybeschr == None:
            ybeschr = "Y" """

        # hier wird durch ein bischen numpy Magie das Integral einer Funktion berechne
        func = lambda x: eval(funktion_text)

        x = np.linspace(-100, 100, 100)
        y = func(x)
        integral = np.trapz(y, x)

        # Rundet das Ergebnis und gibt es in der Box aus
        ergebnis = round(integral)
        self.loesung_entry.delete(0, END)
        self.loesung_entry.insert(0, str(ergebnis))
        self.x_achse_entry = Entry(self)
        self.y_achse_entry = Entry(self)

        self.canvas.get_tk_widget().grid(row=6, column=0, padx=5, pady=5)

        self.ax.clear()
        self.ax.set_xlabel(xbeschr)
        self.ax.set_ylabel(ybeschr)
        self.ax.plot(x, y, label=funktion_text)
        self.ax.legend(loc="upper right")
        self.ax.fill_between(x, y, 0, alpha=0.2)
        self.ax.set_title("Integral")
        self.canvas.draw()
