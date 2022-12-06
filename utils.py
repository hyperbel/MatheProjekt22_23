from tkinter import Tk


# basic window config
def base_Tk(size="200x200", name=""):
    win = Tk()
    win.geometry(size)
    win.title(name)
    return win
