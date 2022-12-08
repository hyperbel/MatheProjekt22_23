import utils
from tkinter import Tk


# rechner fuer lineare funktionen
def open_linear_window():
    win = utils.base_Tk(name="Lineare Funktionen Rechner")
    win.winfo_pathname

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

    menu = utils.get_menu(root)
    root.config(menu=menu)
    root.title("Mathe-Funktionen-Rechner 2022/23")
    root.geometry("350x345")
    root.mainloop()
