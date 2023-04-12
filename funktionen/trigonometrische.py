""" Dieses Modul enthält die Klasse Trigonometrische, die die Funktionen Sinus, Cosinus und Tangens berechnet und darstellt. """
from functionframe import FunktionFrame
import utils
from generator import trigo_generator
from tkinter import Label, Entry, StringVar, TOP, NE, NW, messagebox, Button, BOTH, Radiobutton, ttk,LEFT,RIGHT, END, W, E, NSEW, N
import matplotlib.pyplot as plt
import numpy as np
from verlauf import Verlauf
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from oop import MainWindow

class Trigonometrische(FunktionFrame):
    """ Dieses Frame ist für Funktionen Sinus, Cosinus und Tangens gedacht. """
    def __init__(self, master, parent: MainWindow, funktion = None):
        super().__init__(master)
        
        self.parent = parent

        self.create_widgets()

        if funktion != None:
            zahlen = funktion.split(",")
            zahl1 = zahlen[0]
            zahl2 = zahlen[1]
            zahl3 = zahlen[2]
            self.amplitude_entry.insert(END, zahl1)
            self.frequenz_entry.insert(END, zahl2)
            self.phase_entry.insert(END, zahl3)
            self.xbeschriftung_entry.delete(0, END)
            self.ybeschriftung_entry.delete(0, END)
            self.xbeschriftung_entry.insert(0, "x")
            self.ybeschriftung_entry.insert(0, "y")

    def basis_funktion(self) -> str:
        """ gibt die Basisfunktion zurück
        :return: Basisfunktion
        :rtype: str
        """

        ganzes = self.amplitude_entry.get() + "," + self.frequenz_entry.get() + "," + self.phase_entry.get()
        return ganzes

    def verlauf_appendieren(self, verlauf: Verlauf) -> None:
        """ fügt den Verlauf hinzu
        :param verlauf: Verlauf
        :type verlauf: Verlauf
        """
        verlauf.appendieren(self.basis_funktion())

    def get_help(self) -> None:
        """ ruft das hilfefenster auf """
        _help = utils.base_tk(size="1000x500", name="Hilfe - Funktionen")
        Label(_help,
        text="Trage werte in alle Felder ein\n\
                \nTrigonometrische Funktionen sind mathematische Funktionen,\n die Winkelmessungen in Verbindung mit geometrischen Beziehungen wie dem Einheitskreis oder Dreiecken verwenden,\n um periodische Schwingungen zu beschreiben, wie sie in Wellen, Schall und anderen Phänomenen auftreten können.").grid(row=1, column=0, padx=5, pady=5, sticky=E)
        Button(_help, text="Ok", command=_help.destroy).grid(row=6, column=3, padx=5, pady=5, sticky=E)

    def clear_canvas(self):
        """ leert das canvas """
        self.ax.clear()
        self.canvas.draw()
        self.amplitude_entry.delete(0, END)
        self.frequenz_entry.delete(0, END)
        self.phase_entry.delete(0, END)


    def trigo_button_clicked(self):
        """ ruft die trigo_generator() auf und füllt die Felder mit den Werten """
        amplitude, frequenz, phase = trigo_generator()

        self.amplitude_entry.delete(0, END)
        self.amplitude_entry.insert(0, amplitude)
        self.frequenz_entry.delete(0, END)
        self.frequenz_entry.insert(0, frequenz)
        self.phase_entry.delete(0, END)
        self.phase_entry.insert(0, phase)
        self.xbeschriftung_entry.delete(0, END)
        self.ybeschriftung_entry.delete(0, END)
        self.xbeschriftung_entry.insert(0, "x")
        self.ybeschriftung_entry.insert(0, "y")

    def create_widgets(self):
        """ erstellt die widgets """
        self.amplitude_label =  Label(self, text="Amplitude:")
        self.amplitude_entry = Entry(self)
        self.frequenz_label = Label(self, text="Frequenz:")
        self.frequenz_entry = Entry(self)
        self.phase_label = Label(self, text="Phase:")
        self.phase_entry = Entry(self)
        self.function_type_var = StringVar(value='sin')
        self.xbeschriftung_label =  Label(self, text="X-Beschriftung:")
        self.xbeschriftung_entry = Entry(self)
        self.ybeschriftung_label = Label(self, text="Y-Beschriftung:")
        self.ybeschriftung_entry = Entry(self)
        self.zoom_in_button = Button(self, text="+", command=self.zoom_in)
        self.zoom_out_button = Button(self, text="-", command=self.zoom_out)
        Button(self, text="Leeren", command=self.clear_canvas).grid(row=10, column=3, padx=5, pady=5, sticky=E)
        expo_button = ttk.Button(self, text="Beispiel", command=self.trigo_button_clicked)
        expo_button.grid(row=0, column=3, sticky=NE)



        # figure for matplotlib to plot lines on
        self.fig = plt.Figure(figsize=(5, 5), dpi=100)

        # canvas-like thing for actually draselfg
        self.ax = self.fig.add_subplot()

        self.canvas = FigureCanvasTkAgg(self.fig, master=self)

        Button(self, command=self.trigonometrische_ausrechnen, text="Anzeigen").grid(row=9, column=0, sticky=NW)
        Button(self, text="?", command=self.get_help).grid(row=0, column=2, sticky=NE)

        # radio buttons for selecting function type
        Radiobutton(self, text="Sinus", variable=self.function_type_var, value='sin').grid(row=0, column=0, sticky=NW)
        Radiobutton(self, text="Cosinus", variable=self.function_type_var, value='cos').grid(row=1, column=0, sticky=NW)
        Radiobutton(self, text="Tangens", variable=self.function_type_var, value='tan').grid(row=2, column=0, sticky=NW)
        self.pack_items()

    def zoom_in(self):
        """ zoomt rein """
        self.ax.set_xlim(self.ax.get_xlim()[0] * 0.9, self.ax.get_xlim()[1] * 0.9)
        self.ax.set_ylim(self.ax.get_ylim()[0] * 0.9, self.ax.get_ylim()[1] * 0.9)
        self.canvas.draw()

    def zoom_out(self):
        """ zoomt raus"""
        self.ax.set_xlim(self.ax.get_xlim()[0] * 1.1, self.ax.get_xlim()[1] * 1.1)
        self.ax.set_ylim(self.ax.get_ylim()[0] * 1.1, self.ax.get_ylim()[1] * 1.1)
        self.canvas.draw()

    def pack_items(self):
        """ packt (oder eher gridded) die widgets """
        self.amplitude_label.grid(row=4, column=0, sticky=NW)
        self.amplitude_entry.grid(row=4, column=1, sticky=NW)
        self.frequenz_label.grid(row=5, column=0, sticky=NW)
        self.frequenz_entry.grid(row=5, column=1, sticky=NW)
        self.phase_label.grid(row=6, column=0, sticky=NW)
        self.phase_entry.grid(row=6, column=1, sticky=NW)
        self.xbeschriftung_label.grid(row=7, column=0, sticky=NW)
        self.xbeschriftung_entry.grid(row=7, column=1, sticky=NW)
        self.ybeschriftung_label.grid(row=8, column=0, sticky=NW)
        self.ybeschriftung_entry.grid(row=8, column=1, sticky=NW)
        self.zoom_out_button.grid(row=10, column=1, padx=5, pady=5, sticky=W)
        self.zoom_in_button.grid(row=10, column=0, padx=5, pady=5, sticky=E)


    def trigonometrische_ausrechnen(self):
        """ berechnet die Werte für die Funktion und zeichnet den Graphen """
        try:
             self.amp = float(self.amplitude_entry.get())
             self.freq = float(self.frequenz_entry.get())
             self.phase = float(self.phase_entry.get())
  
        except ValueError:
             _ = messagebox.showerror(title="Inkorrekte eingabe", message="Sie müssen richtige Werte in die Textbox eingeben, bei hilfe einfach auf das ? klicken")
             return
         # x-Werte des Graphen berechnen
  
        self.verlauf_appendieren(self.parent.get_verlauf())
  
        xbeschr = self.xbeschriftung_entry.get()
        ybeschr = self.ybeschriftung_entry.get()  
  
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
        self.ax.set_xlabel(xbeschr)
        self.ax.set_ylabel(ybeschr)
        self.ax.plot(self.x, self.y, label= "Linie")
        self.ax.legend(loc="upper right")
        self.ax.set_title(self.title)
        self.canvas.draw()
         # range mit von - bis
        self.canvas.get_tk_widget().grid(row=6, column=0, padx=5, pady=5)
        self.canvas.draw()
