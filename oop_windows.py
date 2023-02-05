""" This module contains the window classes for the GUI """
import tkinter as tk
from tkinter import ttk
from enum import Enum
import matplotlib.pyplot as plt
import numpy as np


class WindowType(Enum):
    """ enum for window types """
    OTHER = -1
    MAIN = 1
    LINEAR = 2
    EXPONENTIAL = 3
    QUADRATISCH = 4
    GANZRATIONAL = 5


class Window(tk.Tk):
    """ basic window class """
    # initialize the window
    def __init__(self, name: str, size: str, win_type:
                 WindowType = WindowType.OTHER):
        """ initialize the window """
        # call the super class
        super().__init__()
        # set ttk theme
        ttk.Style().theme_use("classic")
        # set window title
        self._title = name
        # set window size
        self._geometry = size
        # set window type
        self._window_type = win_type
        # create a frame
        self._frame = tk.Frame(self)
        self._plot_function = None

        if self._window_type == WindowType.MAIN:
            # create button to get exponential functions
            tk.Button(self.frame, text="Exponentielle Funktionen",
                                    command=self.get_expon_win).pack()
            tk.Button(self.frame, text="Lineare Funktionen",
                                    command=self.get_linear_win).pack()
            tk.Button(self.frame, text="Quadratische Funktionen",
                                    command=self.get_quadratisch_win).pack()
            tk.Button(self.frame, text="Ganzrationale Funktionen",
                                    command=self.get_ganzrational_win).pack()

        self.frame.pack()

    @property
    def window_type(self):
        """ getter for window type """
        return self._window_type

    @property
    def title(self):
        """ getter for title """
        return self._title

    @property
    def geometry(self):
        """ getter for geometry """
        return self._geometry

    @property
    def frame(self):
        """ getter for frame """
        return self._frame

    @property
    def plot_function(self):
        """ getter for plot function """
        return self._plot_function



    @window_type.setter
    def window_type(self, win_type: WindowType):
        """ setter for window type """
        self._window_type = win_type

    @title.setter
    def title(self, name: str):
        """ setter for title """
        self.title(name)

    @geometry.setter
    def geometry(self, size: str):
        """ setter for geometry """
        self._geometry = size

    @frame.setter
    def frame(self, frame: tk.Frame):
        """ setter for frame """
        self._frame = frame

    @plot_function.setter
    def plot_function(self, plot_function):
        """ setter for plot function """
        self._plot_function = plot_function

    @window_type.deleter
    def window_type(self):
        """ deleter for window type """
        del self._window_type

    @title.deleter
    def title(self):
        """ deleter for title """
        del self._title

    @geometry.deleter
    def geometry(self):
        """ deleter for geometry """
        del self._geometry

    @frame.deleter
    def frame(self):
        """ deleter for frame """
        del self._frame

    @plot_function.deleter
    def plot_function(self):
        """ deleter for plot function """
        del self._plot_function

    # seperate run method
    def run(self):
        """ run the window """
        self.mainloop()

    # exponential window method
    def get_expon_win(self):
        """ gets exponential window """

        # create a window
        expon_win = ExponentialFunktionenWindow(np.exp)
        # run the window
        expon_win.run()

    def get_linear_win(self):
        """ gets linear window """
        # create a window
        linear_win = LineareFunktionenWindow(np.exp)
        # run the window
        linear_win.run()

    def get_quadratisch_win(self):
        """ gets quadratic window """
        # create a window
        quadratic_win = QuadratischeFunktionenWindow(np.exp)
        # run the window
        quadratic_win.run()

    def get_ganzrational_win(self):
        """ gets rational window """
        # create a window
        rational_win = GanzrationaleFunktionenWindow(np.exp)
        # run the window
        rational_win.run()


class FunktionenWindow(Window):
    """ base window for the mathematical functions """
    def __init__(self, name: str, size: str, win_type:
                 WindowType = WindowType.OTHER):
        """ initialize the window """
        super().__init__(name, size, win_type)
        self.window_type = win_type


class ExponentialFunktionenWindow(FunktionenWindow):
    """ window for exponential functions """
    def __init__(self, plot_function):
        super().__init__("Exponentielle Funktionen", "400x400",
                         WindowType.EXPONENTIAL)
        self.window_type = WindowType.EXPONENTIAL
        self.plot_function = plot_function

    # create a plot
    def plot(self):
        """ plot the function """
        # create a figure
        fig = plt.figure()
        # create a subplot
        figure_ax = fig.add_subplot(111)
        # create a range
        f_x = np.arange(0, 10, 100)
        # create a function
        res_y = np.exp(f_x)
        # plot the function
        figure_ax.plot(f_x, res_y)
        # show the plot
        plt.show()


class LineareFunktionenWindow(FunktionenWindow):
    """ Fenster für lineare Funktionen """
    # initialize thw window
    def __init__(self, plot_function):
        super().__init__("Lineare Funktionen", "400x400", WindowType.LINEAR)
        # """ initialize the window """
        self.plot_function = plot_function

        self.widgets()
        self.pack()

    def widgets(self):
        """ labels und entries """
        self.von_entry = tk.Entry(self.frame)
        self.bis_entry = tk.Entry(self.frame)
        self.m_entry = tk.Entry(self.frame)
        self.b_entry = tk.Entry(self.frame)
        self.x_achse_entry = tk.Entry(self.frame)
        self.y_achse_entry = tk.Entry(self.frame)


    def pack(self):
        """ items packen """
        tk.Label(self.frame, text="Von:").pack()
        self.von_entry.pack()
        tk.Label(self.frame, text="Bis:").pack()
        self.bis_entry.pack()
        tk.Label(self.frame, text="Steigung:").pack()
        self.m_entry.pack()
        tk.Label(self.frame, text="y-Achsenabschnitt:").pack()
        self.b_entry.pack()
        tk.Label(self.frame, text="x-Achse:").pack()
        self.x_achse_entry.pack()
        tk.Label(self.frame, text="y-Achse:").pack()
        self.y_achse_entry.pack()



class QuadratischeFunktionenWindow(FunktionenWindow):
    """ fenster für quadratische funktionen """
    def __init__(self, plot_function):
        super().__init__("Quadratische Funktionen", "400x400",
                         WindowType.QUADRATISCH)
        self.window_type = WindowType.QUADRATISCH
        self.plot_function = plot_function

    # create a plot
    def plot(self, a_var, b_var, c_var):
        """ plot the function """
        def function_f(x_var):
            """ function to plot (y = ax^2 + bx + c) """
            return np.array([a_var * i_x ** 2 + b_var * i_x + c_var for i_x in x_var])
        # create a figure
        fig = plt.figure()
        # create a subplot
        figure_ax = fig.add_subplot(111)
        # create a range
        f_x = np.arange(0, 10, 100)
        res_y = function_f(f_x)
        # plot the function
        figure_ax.plot(f_x, res_y)
        # show the plot
        plt.show()


class GanzrationaleFunktionenWindow(FunktionenWindow):
    """ fenster für ganzrationale funktionen """
    def __init__(self, plot_function):
        super().__init__("Ganzrationale Funktionen", "400x400",
                         WindowType.GANZRATIONAL)
        self.window_type = WindowType.GANZRATIONAL
        self.plot_function = plot_function
