from functionframe import FunktionFrame
from tkinter import Label, Entry, BOTH, NW, TOP, END, Button, messagebox,ttk, NE, LEFT,RIGHT
import utils
import numpy as np
import matplotlib.pyplot as plt
from verlauf import Verlauf
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Integralrechnung(FunktionFrame):
    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()

    def get_help(self) -> None:
        """ ruft das hilfefenster auf """
        _help = utils.base_tk(size="800x500", name="Hilfe - Funktionen")
        Label(_help,
        text="In das Input feld die Funktion eingeben, die exponenten werden mit einem ^ notiert.\n\
                Also z.B.: 1x^3 + 2x^2 + 1x + 0\n\
                Wenn der erste term ein x vorne hat, muss eine 1 davor geschrieben werden!").pack()
        Button(_help, text="Ok", command=_help.destroy).pack()

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
        self.zoom_in_button = Button(self, text="+", command=self.zoom_in)
        self.zoom_out_button = Button(self, text="-", command=self.zoom_out)
        self.zoom_combobox = ttk.Combobox(self, values=["25%", "50%", "75%", "100%"], state="readonly", width=5)
        self.zoom_combobox.current(3)  # standardmäßig 100% auswählen
        self.calculate_button = Button(self, text="anzeigen", command=self.integral_ausrechnen)

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
        self.funktion_label.pack(side=TOP, anchor=NW)
        self.funktion_entry.pack(side=TOP, anchor=NW)
        self.anfangX_label.pack(side=TOP, anchor=NW)
        self.anfangX_entry.pack(side=TOP, anchor=NW)
        self.endeX_label.pack(side=TOP, anchor=NW)
        self.endeX_entry.pack(side=TOP, anchor=NW)
        self.y_label.pack(side=TOP, anchor=NW)
        self.y_entry.pack(side=TOP, anchor=NW)
        self.loesung_label.pack(side=TOP, anchor=NW)
        self.loesung_entry.pack(side=TOP, anchor=NW)
        self.calculate_button.pack(side=TOP, anchor=NW)
        self.zoom_out_button.pack(side="right", padx=5, pady=5)
        self.zoom_in_button.pack(side="right", padx=5, pady=5)
        self.zoom_combobox.pack(side="right", padx=5, pady=5)
        Button(self, text="?", command=self.get_help).pack(side=TOP, anchor=NE)



    def integral_ausrechnen(self):
        # Hohle Werte
        try: 
            funktion_text = self.funktion_entry.get()
            anfangx = float(self.anfangX_entry.get())
            endex = float(self.endeX_entry.get())
            y = int(self.y_entry.get())

            # checken ob werte floats sind
            assert utils.entry_is_float(anfangx)
            assert utils.entry_is_float(endex)
            
        except ValueError:
            _ = messagebox.showerror(title="Inkorrekte eingabe", message="Sie müssen richtige Werte in die Textbox eingeben, bei hilfe einfach auf das ? klicken")
            return

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
