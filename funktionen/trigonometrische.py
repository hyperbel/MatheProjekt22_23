from functionframe import FunktionFrame
import utils
from generator import trigo_generator
from tkinter import Label, Entry, StringVar, TOP, NE, NW, messagebox, Button, BOTH, Radiobutton, ttk,LEFT,RIGHT
import matplotlib.pyplot as plt
import numpy as np
from verlauf import Verlauf
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Trigonometrische(FunktionFrame):
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

    def clear_canvas(self):
        self.ax.clear()
        self.canvas.draw()


    def create_widgets(self):
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
        self.zoom_combobox = ttk.Combobox(self, values=["25%", "50%", "75%", "100%"], state="readonly", width=5)
        self.zoom_combobox.current(3)  # standardmäßig 100% auswählen
        Button(self, text="Leeren", command=self.clear_canvas).pack(side="right", padx=5, pady=5)



        # figure for matplotlib to plot lines on
        self.fig = plt.Figure(figsize=(10, 10), dpi=100)

        # canvas-like thing for actually draselfg
        self.ax = self.fig.add_subplot()

        self.canvas = FigureCanvasTkAgg(self.fig, master=self)

        Button(self, command=self.trigonometrische_ausrechnen, text="Anzeigen").pack(side=TOP,
                                                                     anchor=NW)
        Button(self, text="?", command=self.get_help).pack(side=TOP, anchor=NE)

        # radio buttons for selecting function type
        Radiobutton(self, text="Sinus", variable=self.function_type_var, value='sin').pack(side=TOP, anchor=NW)
        Radiobutton(self, text="Cosinus", variable=self.function_type_var, value='cos').pack(side=TOP, anchor=NW)
        Radiobutton(self, text="Tangens", variable=self.function_type_var, value='tan').pack(side=TOP, anchor=NW)

        self.pack_items()
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



    def pack_items(self):
        self.amplitude_label.pack(side=TOP, anchor=NW)
        self.amplitude_entry.pack(side=TOP, anchor=NW)
        self.frequenz_label.pack(side=TOP, anchor=NW)
        self.frequenz_entry.pack(side=TOP, anchor=NW)
        self.phase_label.pack(side=TOP, anchor=NW)
        self.phase_entry.pack(side=TOP, anchor=NW)
        self.zoom_out_button.pack(side="right", padx=5, pady=5)
        self.zoom_in_button.pack(side="right", padx=5, pady=5)
        self.zoom_combobox.pack(side="right", padx=5, pady=5)
        self.xbeschriftung_label.pack(side="right", padx=5, pady=5)
        self.xbeschriftung_entry.pack(side="right", padx=5, pady=5)
        self.ybeschriftung_label.pack(side="right", padx=5, pady=5)
        self.ybeschriftung_entry.pack(side="right", padx=5, pady=5)


    def trigonometrische_ausrechnen(self):
       try:
            self.amp = float(self.amplitude_entry.get())
            self.freq = float(self.frequenz_entry.get())
            self.phase = float(self.phase_entry.get())

       except ValueError:
            _ = messagebox.showerror(title="Inkorrekte eingabe", message="Sie müssen richtige Werte in die Textbox eingeben, bei hilfe einfach auf das ? klicken")
            return
        # x-Werte des Graphen berechnen

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
       self.canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True)
       self.canvas.draw()
