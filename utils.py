from tkinter import Tk
from globals import Globals as G

# dict fuer alle globalen werte
global_dict = {}


# basic window config
def base_Tk(size="900x600", name=""):
    win = Tk()
    win.geometry(size)
    win.title(name)
    return win


# setzt globale werte, fuer mehr info schau in globals.py
def global_set_user_data(user_name, user_password):
    global_dict["user_name"] = user_name
    global_dict["user_password"] = user_password


def debug_log(item):
    if G.debug:
        print(item)
