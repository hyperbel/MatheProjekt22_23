from functionframe import FunktionFrame
from tkinter import Label, Entry, BOTH, NW, TOP, END, Button, messagebox,ttk, NE, LEFT,RIGHT, PhotoImage, Canvas, Frame
import tkinter.constants as tkc
import utils
from generator import integral_generator
import numpy as np
import matplotlib.pyplot as plt
from verlauf import Verlauf
import sqlite3
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Integralrechnung(FunktionFrame):
    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()

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
                \nDas Integralrechnen ist ein Zweig der Analysis, der sich mit der Berechnung von Flächen unter einer Kurve,\n dem Bestimmen von Volumina und Schwerpunkten von dreidimensionalen Objekten sowie der Lösung von Differentialgleichungen befasst,\n indem es die Umkehrung des Differenzierens darstellt.").pack()
        img = PhotoImage(file="logo.png")
        canvas = Canvas(self, width=700, height=300)
        canvas.pack()
        canvas.create_image(0, 0, anchor=NW, image=img)
        Button(_help, text="Ok", command=_help.destroy).pack()

        _help.image = img

    def clear_canvas(self):
        self.ax.clear()
        self.canvas.draw()

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
        self.zoom_combobox = ttk.Combobox(self, values=["25%", "50%", "75%", "100%"], state="readonly", width=5)
        self.zoom_combobox.current(3)  # standardmäßig 100% auswählen
        self.calculate_button = Button(self, text="anzeigen", command=self.integral_ausrechnen)
        Button(self, text="Leeren", command=self.clear_canvas).pack(side="right", padx=5, pady=5)
       

        fig = plt.Figure(figsize=(10, 10), dpi=100)

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


    def pack_widgets(self) -> None:
        # Anordnung der Eingabefelder und Beschriftungen oben links
        self.funktion_label.pack(side=TOP, anchor=NW)
        self.funktion_entry.pack(side=TOP, anchor=NW)
        self.xbeschriftung_label.pack(side=TOP, anchor=NW)
        self.xbeschriftung_entry.pack(side=TOP, anchor=NW)
        self.ybeschriftung_label.pack(side=TOP, anchor=NW)
        self.ybeschriftung_entry.pack(side=TOP, anchor=NW)

        # Anordnung des Anzeige-Buttons unter den Input-Feldern
        self.calculate_button.pack(side=TOP, anchor=NW)

        # Anordnung der Lösungsfelder rechts von den Beschriftungen
        self.loesung_label.pack(side=LEFT, padx=5, pady=5)
        self.loesung_entry.pack(side=LEFT, padx=5, pady=5)

        # Anordnung des Berechnen-Buttons unter den Lösungsfeldern
        self.calculate_button.pack(side=LEFT, padx=5, pady=5)

        # Anordnung der Zoom-Elemente unter den Lösungsfeldern
        self.zoom_out_button.pack(side=LEFT, padx=5, pady=5)
        self.zoom_in_button.pack(side=LEFT, padx=5, pady=5)
        self.zoom_combobox.pack(side=LEFT, padx=5, pady=5)

        # Hilfe-Button in der oberen rechten Ecke
        Button(self, text="?", command=self.get_help).pack(side=TOP, anchor=NE)






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

        self.canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

        self.ax.clear()
        self.ax.set_xlabel(xbeschr)
        self.ax.set_ylabel(ybeschr)
        self.ax.plot(x, y, label=funktion_text)
        self.ax.legend(loc="upper right")
        self.ax.fill_between(x, y, 0, alpha=0.2)
        self.ax.set_title("Integral")
        self.canvas.draw()
