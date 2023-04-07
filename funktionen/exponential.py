from functionframe import FunktionFrame
import utils
import numpy as np
from verlauf import Verlauf
from generator import expo_generator
from tkinter import Label, Entry, BOTH, NW, TOP, Button, NE,ttk, messagebox,RIGHT,LEFT
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

    def basis_funktion(self) -> str:
        return self.a_entry.get()

    def verlauf_appendieren(self, verlauf: Verlauf) -> None:
        verlauf.appendieren(self.basis_funktion())

    def get_help(self) -> None:
        """ ruft das hilfefenster auf """
        _help = utils.base_tk(size="1000x500", name="Hilfe - Funktionen")
        Label(_help,
        text="In dem Feld a kommt der Wachstumsfaktor rein. Kommerta werden mit einem . gemacht!\n\
                Also 1.9\n\
                \nExponentialfunktionen sind Funktionen, bei denen eine bestimmte Basiszahl (auch Wachstumsfaktor genannt)\n durch eine Potenzfunktion immer wieder mit sich selbst multipliziert wird,\n wodurch die Funktionswerte exponentiell steigen oder fallen können.").pack()
        Button(_help, text="Ok", command=_help.destroy).pack()
    
    def clear_canvas(self):
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

    # function in function to be used on button click
    def exponential_ausrechnen(self) -> None:
        """ berechnet die funktion """
        # werte holen
        try:
            von = float(self.von_entry.get())
            bis = float(self.bis_entry.get())
            a = float(self.a_entry.get())
            # x = float(x_entry.get())

            # checken ob werte floats sind
            assert utils.entry_is_float(von)
            assert utils.entry_is_float(bis)
            assert utils.entry_is_float(a)
            # assert entry_is_float(x)
        except ValueError:
            fehler = messagebox.showerror(title="Inkorrekte eingabe", message="Sie müssen richtige Werte in die Textbox eingeben, bei hilfe einfach auf das ? klicken")
            return

        self.verlauf_appendieren(self.master.get_verlauf())

        # range mit von - bis
        self.x_werte = np.arange(von, bis, 0.2)

        # setze namen der achsen
        self.ax.set_xlabel(self.x_achse_entry.get())
        self.ax.set_ylabel(self.y_achse_entry.get())

        # lineare funktion plotten
        self.ax.plot(self.x_werte, a ** self.x_werte, label=a)
        self.ax.legend(loc="upper right")
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
        self.zoom_in_button = Button(self, text="+", command=self.zoom_in)
        self.zoom_out_button = Button(self, text="-", command=self.zoom_out)
        self.zoom_combobox = ttk.Combobox(self, values=["25%", "50%", "75%", "100%"], state="readonly", width=5)
        self.zoom_combobox.current(3)  # standardmäßig 100% auswählen
        self.zoom_out_button.pack(side="right", padx=5, pady=5)
        self.zoom_in_button.pack(side="right", padx=5, pady=5)
        self.zoom_combobox.pack(side="right", padx=5, pady=5)
        Button(self, text="Leeren", command=self.clear_canvas).pack(side="right", padx=5, pady=5)

        # use function declared earlier to compute stuff
        Button(self, command=self.exponential_ausrechnen, text="Anzeigen").pack(side=TOP,
                                                                     anchor=NW)
        Button(self, text="?", command=self.get_help).pack(side=TOP, anchor=NE)
