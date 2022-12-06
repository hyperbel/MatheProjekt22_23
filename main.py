#  numpy, matplotlib, math, sympy, random, time, glob, queue, collections, threading, re , tk
from tkinter import *
import windows as wins

def main():
    root = Tk()

    get_menu(root)
    root.title("Mathe-Funktionen-Rechner 2022/23")
    root.geometry("350x345")
    root.mainloop()

def get_menu(root):
    _menu = Menu(root)
    _menu.add_command(label="Linear", command=wins.open_linear_window(root))
    root.config(menu=_menu)

if __name__ == "__main__":
    main()
