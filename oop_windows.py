import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np


# enum for window types
class WindowType:
    Other = -1
    Main = 1
    Linear = 2
    Exponential = 3
    Quadratisch = 4
    Ganzrational = 5


# create a window class
class Window(tk.Tk):

    # initialize the window
    def __init__(self, name: str, size: str, win_type:
                 WindowType = WindowType.Other):
        # call the super class
        super().__init__()
        # set window type
        self.window_type = win_type
        # set title
        self.title(name)
        # set size
        self.geometry(size)
        # create a frame
        self.frame = tk.Frame(self)
        self.plot_function = None

        if self.window_type == WindowType.Main:
            # create button to get exponential functions
            self.button = tk.Button(self.frame,
                                    text="Exponentielle Funktionen",
                                    command=self.get_expon_win)
            # pack the items

            self.button.pack()

        self.frame.pack()

    # seperate run method
    def run(self):
        self.mainloop()

    # exponential window method
    def get_expon_win(self):
        # exponential function

        # create a window
        expon_win = ExponentialFunktionenWindow(np.exp)
        # run the window
        expon_win.run()

    # method to set window type enum
    def set_window_type(self, win_type: WindowType):
        self.window_type = win_type

    # set function to plot
    def set_plot_function(self, func):
        self.plot_function = func


class ExponentialFunktionenWindow(Window):
    # initialize thw window
    def __init__(self, plot_function):
        super().__init__("Exponentielle Funktionen", "400x400",
                         WindowType.Exponential)
        self.window_type = WindowType.Exponential
        self.plot_function = plot_function


class LineareFunktionenWindow(Window):
    # initialize thw window
    def __init__(self, plot_function):
        super().__init__("Lineare Funktionen", "400x400",
                         WindowType.Linear)
        self.window_type = WindowType.Linear
        self.plot_function = plot_function


class QuadratischeFunktionenWindow(Window):
    # initialize thw window
    def __init__(self, plot_function):
        super().__init__("Quadratische Funktionen", "400x400",
                         WindowType.Quadratisch)
        self.window_type = WindowType.Quadratisch
        self.plot_function = plot_function


class GanzrationaleFunktionenWindow(Window):
    # initialize thw window
    def __init__(self, plot_function):
        super().__init__("Ganzrationale Funktionen", "400x400",
                         WindowType.Ganzrational)
        self.window_type = WindowType.Ganzrational
        self.plot_function = plot_function
