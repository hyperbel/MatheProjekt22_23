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


def get_menu(root):
    # main menu item
    _menu = Menu(root, tearoff=0)
    # submenu fuer funktionen erstellen
    funktionen_menu = Menu(_menu, tearoff=0)
    # adding submenu
    _menu.add_cascade(label="Funktionen", menu=funktionen_menu)
    # submenu item "lineare funktionen"
    funktionen_menu.add_command(label="Linear",
                                command=wins.open_linear_window)
    return _menu


if __name__ == "__main__":
    main()
