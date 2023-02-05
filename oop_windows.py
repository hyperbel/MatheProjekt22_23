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
        self._title = name
        self._geometry = size
        # set window type
        self._window_type = win_type
        # create a frame
        self._frame = tk.Frame(self)
        self._plot_function = None

        if self._window_type == WindowType.Main:
            # create button to get exponential functions
            self._button = tk.Button(self.frame,
                                    text="Exponentielle Funktionen",
                                    command=self.get_expon_win).pack()

        self.frame.pack()

    @property
    def window_type(self):
        return self._window_type

    @property
    def title(self):
        return self._title

    @property
    def geometry(self):
        return self._geometry

    @property
    def frame(self):
        return self._frame

    @property
    def plot_function(self):
        return self._plot_function



    @window_type.setter
    def window_type(self, win_type: WindowType):
        self._window_type = win_type

    @title.setter
    def title(self, name: str):
        self.title(name)

    @geometry.setter
    def geometry(self, size: str):
        self.geometry(size)

    @frame.setter
    def frame(self, frame: tk.Frame):
        self._frame = frame

    @plot_function.setter
    def plot_function(self, plot_function):
        self._plot_function = plot_function

    @window_type.deleter
    def window_type(self):
        del self._window_type

    @title.deleter
    def title(self):
        del self._title

    @geometry.deleter
    def geometry(self):
        del self._geometry

    @frame.deleter
    def frame(self):
        del self._frame

    @plot_function.deleter
    def plot_function(self):
        del self._plot_function

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


class FunktionenWindow(Window):
    def __init__(self, name: str, size: str, win_type:
                 WindowType = WindowType.Other):
        super().__init__(name, size, win_type)
        self.window_type = win_type

    def plot(self):
        pass


class ExponentialFunktionenWindow(FunktionenWindow):
    # initialize thw window
    def __init__(self, plot_function):
        super().__init__("Exponentielle Funktionen", "400x400",
                         WindowType.Exponential)
        self.window_type = WindowType.Exponential
        self.plot_function = plot_function

    # create a plot
    def plot(self):
        # create a figure
        fig = plt.figure()
        # create a subplot
        ax = fig.add_subplot(111)
        # create a range
        x = np.arange(0, 10, 100)
        # create a function
        y = np.exp(x)
        # plot the function
        ax.plot(x, y)
        # show the plot
        plt.show()


class LineareFunktionenWindow(FunktionenWindow):
    # initialize thw window
    def __init__(self, plot_function):
        super().__init__("Lineare Funktionen", "400x400",
                         WindowType.Linear)
        self.window_type = WindowType.Linear
        self.plot_function = plot_function

        self.widgets()
        self.pack()

    def widgets(self):
        # labels und entries
        self.von_label = tk.Label(self.frame, text="Von:")
        self.von_entry = tk.Entry(self.frame)
        self.bis_label = tk.Label(self.frame, text="Bis:")
        self.bis_entry = tk.Entry(self.frame)
        self.m_label = tk.Label(self.frame, text="Steigung:")
        self.m_entry = tk.Entry(self.frame)
        self.b_label = tk.Label(self.frame, text="y-Achsenabschnitt:")
        self.b_entry = tk.Entry(self.frame)
        self.x_achse_label = tk.Label(self.frame, text="x-Achse:")
        self.x_achse_entry = tk.Entry(self.frame)
        self.y_achse_label = tk.Label(self.frame, text="y-Achse:")
        self.y_achse_entry = tk.Entry(self.frame)


    def pack(self):
        # items packen
        self.von_label.pack()
        self.von_entry.pack()
        self.bis_label.pack()
        self.bis_entry.pack()
        self.m_label.pack()
        self.m_entry.pack()
        self.b_label.pack()
        self.b_entry.pack()
        self.x_achse_label.pack()
        self.x_achse_entry.pack()
        self.y_achse_label.pack()
        self.y_achse_entry.pack()



class QuadratischeFunktionenWindow(FunktionenWindow):
    # initialize thw window
    def __init__(self, plot_function):
        super().__init__("Quadratische Funktionen", "400x400",
                         WindowType.Quadratisch)
        self.window_type = WindowType.Quadratisch
        self.plot_function = plot_function

    # create a plot
    def plot(self):
        # create a figure
        fig = plt.figure()
        # create a subplot
        ax = fig.add_subplot(111)
        # create a range
        x = np.arange(0, 10, 100)
        # create a function
        # plot the function
        ax.plot(x, y)
        # show the plot
        plt.show()


class GanzrationaleFunktionenWindow(FunktionenWindow):
    # initialize thw window
    def __init__(self, plot_function):
        super().__init__("Ganzrationale Funktionen", "400x400",
                         WindowType.Ganzrational)
        self.window_type = WindowType.Ganzrational
        self.plot_function = plot_function

    # create a plot
    def plot(self):
        # create a figure
        fig = plt.figure()
        # create a subplot
        ax = fig.add_subplot(111)
        # create a range
        x = np.arange(0, 10, 100)
        # create a function
        # plot the function
        # ax.plot(x, y)
        # show the plot
        plt.show()
