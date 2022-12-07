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


def open_main_window():
    root = Tk()

    menu = utils.get_menu(root)
    root.config(menu=menu)
    root.title("Mathe-Funktionen-Rechner 2022/23")
    root.geometry("350x345")
    root.mainloop()
