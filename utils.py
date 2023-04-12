""" utilities die man einfach gebrauchen kann"""
from tkinter import Tk
import re
# basic window config
def base_tk(size="900x600", name="") -> Tk:
    """basis window config
    :param size: Größe des Fensters
    :type size: str
    :param name: Name des Fensters
    :type name: str

    :return: das Fenster
    :rtype: Tk
    """
    win = Tk()
    win.geometry(size)
    win.title(name)
    return win

def entry_is_float(inp):
    """Schaut, ob der gegebene input in einen float umgewandelt werden kann
    :param inp: der input, der geprüft werden soll
    :return: True, wenn der input in einen float umgewandelt werden kann, sonst False
    :rtype: bool
    """
    # magic regex for checking if input is float type
    if isinstance(inp, float):
        return True

    if not isinstance(inp, str):
        print(type(inp))

    res = re.match(r"(\+|\-)?\d+(,\d+)?$", inp)
    return res is not None

