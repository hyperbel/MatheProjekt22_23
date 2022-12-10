import utils
from tkinter import Tk, TOP, BOTH, Menu
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np


# rechner fuer lineare funktionen
def open_linear_window():
    win = utils.base_Tk(name="Lineare Funktionen Rechner")

    # figure for matplotlib to plot lines on
    fig = plt.Figure(figsize=(10, 10), dpi=100)

    # canvas-like thing for actually drawing
    ax = fig.add_subplot()

    # range of numhers, see numpy.org for doc on arange
    rg = np.arange(0, 10, 0.2)
    ax.plot(rg, rg * rg)
    ax.set_xlabel("x axis")
    ax.set_ylabel("y axis")

    cv = FigureCanvasTkAgg(fig, master=win)
    cv.draw()

    cv.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True)

    win.mainloop()


# rechner fuer quadratische funktionen
def open_quadratisch_window():
    win = utils.base_Tk(name="Quadratische Funktionen Rechner")
    win.mainloop()


def open_Ganzrazionale_window():
    win = utils.base_Tk(name="Ganzrationale Funktionen Rechner")
    win.mainloop()


def open_Trigonometrische_window():
    win = utils.base_Tk(name="Trigonometrische Funktionen Rechner")
    win.mainloop()


def open_Exponential_window():
    win = utils.base_Tk(name="Exponential Funktionen Rechner")
    win.mainloop()


def open_defferenzial_window():
    win = utils.base_Tk(name="Einstieg Diefferenzialrechnung")
    win.mainloop()


def open_Kurvendiskussion_window():
    win = utils.base_Tk(name="Kurvendiskussion")
    win.mainloop()


def open_Integralrechnung_window():
    win = utils.base_Tk(name="Integralrechnung")
    win.mainloop()


def open_hilfe_window():
    win = utils.base_Tk(name="hilfe")
    win.mainloop()


def open_ueber_window():
    win = utils.base_Tk(name="über")
    win.mainloop()


def open_verlauf_window():
    win = utils.base_Tk(name="verlauf")
    win.mainloop()


def open_main_window():
    root = Tk()

    menu = get_menu(root)
    root.config(menu=menu)
    root.title("Mathe-Funktionen-Rechner 2022/23")
    root.geometry("350x345")
    root.mainloop()


# generiert main menu fuer das root win
def get_menu(root):
    _menu = Menu(root, tearoff=0)
    funktionen_menu = Menu(_menu, tearoff=0)
    account_menu = Menu(_menu, tearoff=0)
    hilfe_menu = Menu(_menu, tearoff=0)

    funktionen_menu.add_command(label="Linear",
                                command=open_linear_window)
    funktionen_menu.add_command(label="Quadratisch",
                                command=open_quadratisch_window)
    funktionen_menu.add_command(label="Ganzrationale Funktionen",
                                command=open_Ganzrazionale_window)
    funktionen_menu.add_command(label="Trigonometrische",
                                command=open_Trigonometrische_window)
    funktionen_menu.add_command(label="Exponential",
                                command=open_Exponential_window)
    funktionen_menu.add_command(label="Differenzial",
                                command=open_defferenzial_window)
    funktionen_menu.add_command(label="Kurvendiskusion",
                                command=open_Kurvendiskussion_window)
    funktionen_menu.add_command(label="Integralrechnung",
                                command=open_Integralrechnung_window)
    _menu.add_cascade(label="Funktionen", menu=funktionen_menu)

    account_menu.add_command(label="Logout",
                             command=open_linear_window)
    account_menu.add_command(label="Verlauf",
                             command=open_verlauf_window)
    _menu.add_cascade(label="Account", menu=account_menu)

    hilfe_menu.add_command(label="hilfe",
                                 command=open_hilfe_window)
    _menu.add_cascade(label="Hilfe", menu=hilfe_menu)
    hilfe_menu.add_command(label="über",
                                 command=open_ueber_window)

    return _menu
