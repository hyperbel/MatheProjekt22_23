""" Funktions basis frame, wieder für circular-import probleme"""
from tkinter import Frame

class FunktionFrame(Frame):
    """ Basis frame für die Funktionen """
    def __init__(self, master, width=1000, height=800):
        super().__init__(master, width=width, height=height)
        self.master = master
    
    def verlauf_appendieren(self) -> None:
        """ fuegt die funktion in den Verlauf ein 
            soll überschrieben werden"""
        raise NotImplementedError

    def get_help(self) -> None:
        """ ruft das hilfefenster auf 
            soll überschrieben werden"""
        raise NotImplementedError

    def plot(self) -> None:
        """ erstellt den plot 
            soll überschrieben werden"""
        raise NotImplementedError
