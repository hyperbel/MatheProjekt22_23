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
    account_menu = Menu(_menu, tearoff=0)
    hilfe_menu = Menu(_menu, tearoff=0)
    funktionen_menu.add_command(label="Linear",
                                command=wins.open_linear_window)
    funktionen_menu.add_command(label="Quadratisch",
                                command=wins.open_quadratisch_window)
    _menu.add_cascade(label="Funktionen", menu=funktionen_menu)
    account_menu.add_command(label="Login/logout",
				 command=wins.open_linear_window)
    account_menu.add_command(label="Verlauf",
                                 command=wins.open_linear_window)
    _menu.add_cascade(label="Account", menu=account_menu)
    hilfe_menu.add_command(label="hilfe",
                                 command=wins.open_linear_window)
    _menu.add_cascade(label="Hilfe", menu=hilfe_menu)
    hilfe_menu.add_command(label="über",
                                 command=wins.open_linear_window)



    return _menu


if __name__ == "__main__":
    main()
