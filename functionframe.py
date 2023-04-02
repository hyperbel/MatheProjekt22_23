from tkinter import Frame

class FunktionFrame(Frame):
    def __init__(self, master):
        super().__init__(master)
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
