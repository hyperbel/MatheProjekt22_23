from tkinter import Tk

class BaseWindow(Tk):
    def __init__(self):
        super().__init__()
        self.title("Mathe Projekt 22/23")
        self.minsize(1200, 850)
        self.maxsize(1200, 850)

    def select_by_name(self, name: str, funktion: str = None):
        pass

    
