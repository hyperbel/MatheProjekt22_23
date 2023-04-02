from functionframe import FunktionFrame
from tkinter import Label, Entry, StringVar, TOP, NE, NW, messagebox, Button, BOTH, Radiobutton
import matplotlib.pyplot as plt
import numpy as np
from verlauf import Verlauf
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Trigonometrische(FunktionFrame):
    def __init__(self, master):
        super().__init__(master)

        self.create_widgets()

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

        Button(self, command=self.trigonometrische_ausrechnen, text="Anzeigen").pack(side=TOP,
                                                                     anchor=NW)
        Button(self, text="?", command=self.get_help).pack(side=TOP, anchor=NE)

        # radio buttons for selecting function type
        Radiobutton(self, text="Sinus", variable=self.function_type_var, value='sin').pack(side=TOP, anchor=NW)
        Radiobutton(self, text="Cosinus", variable=self.function_type_var, value='cos').pack(side=TOP, anchor=NW)
        Radiobutton(self, text="Tangens", variable=self.function_type_var, value='tan').pack(side=TOP, anchor=NW)

        self.pack_items()

    def pack_items(self):
        self.amplitude_label.pack(side=TOP, anchor=NW)
        self.amplitude_entry.pack(side=TOP, anchor=NW)
        self.frequenz_label.pack(side=TOP, anchor=NW)
        self.frequenz_entry.pack(side=TOP, anchor=NW)
        self.phase_label.pack(side=TOP, anchor=NW)
        self.phase_entry.pack(side=TOP, anchor=NW)


    def trigonometrische_ausrechnen(self):
       try:
            self.amp = float(self.amplitude_entry.get())
            self.freq = float(self.frequenz_entry.get())
            self.phase = float(self.phase_entry.get())

       except ValueError:
            _ = messagebox.showerror(title="Inkorrekte eingabe", message="Sie müssen richtige Werte in die Textbox eingeben, bei hilfe einfach auf das ? klicken")
            return
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
