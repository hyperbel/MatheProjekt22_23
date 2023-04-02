from functionframe import FunktionFrame
import utils
import numpy as np
from tkinter import Label, Entry, BOTH, NW, TOP, Button, NE
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

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
