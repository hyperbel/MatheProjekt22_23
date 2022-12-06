# numpy, matplotlib, math, sympy, random, time, glob, queue, collections,
# threading, re , tk
from tkinter import Tk, Menu
import windows as wins


def main():
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
    _menu.add_cascade(label="Funktionen", menu=funktionen_menu)
    funktionen_menu.add_command(label="Linear",
                                command=wins.open_linear_window)
    funktionen_menu.add_command(label="Quadratisch",
                                command=wins.open_quadratisch_window)
    return _menu


if __name__ == "__main__":
    main()
