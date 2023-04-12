""" Basis-Klasse für das MainWindow, damit ich das wo anders importieren kann"""
from tkinter import Tk
from tkinter import PhotoImage

class BaseWindow(Tk):
    """ Basis-Klasse für das MainWindow, damit ich das wo anders importieren kann"""
    def __init__(self):
        """ Initialisiert das MainWindow """
        super().__init__()
        self.title("Mathe Projekt 22/23")
        self.minsize(1200, 850)
        self.maxsize(1200, 850)

        photo = PhotoImage(file= "./logo.png")
        self.iconphoto(False, photo)

    def select_by_name(self, name: str, funktion: str = None):
        """ wird implementiert, vertau mir
        :param name: Name des Widgets
        :param funktion: Name der Funktion
        """
        pass

    

