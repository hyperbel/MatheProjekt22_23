import tkinter as tk

# create a window class
class Window(tk.Tk):
    # initialize the window
    def __init__(self, name: str, size: str):
        # call the super class
        super().__init__()
        # set title
        self.title(name)
        # set size
        self.geometry(size)
        # create a frame
        self.frame = tk.Frame(self)
        # pack the frame
        self.frame.pack()

    # seperate run method
    def run():
        self.mainloop()


class ExponentialFunktionenWindow(Window):
    # initialize thw window
    def __init__(self):
        super().__init("Exponentielle Funktionen", "400x400")


