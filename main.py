# import tk and regex
import tkinter as tk
import re

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
        # mainloop
        self.mainloop()


# create a main function
def main():
    # create a window
    window = Window("Funktionen-Rechner", "400x400")


# call main function
if __name__ == "__main__":
    main()

