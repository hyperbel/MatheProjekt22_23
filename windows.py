"""@package windows 
Fenster für die GUI 
"""
import re
from tkinter import Tk, TOP, BOTH, Menu, Label, Entry, Button, NW, NE, Listbox, LEFT, END, Scrollbar, RIGHT
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import sqlite3

# checks if input (usally from entry) is of type float
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


def zoomin(position):
    """ zoomt rein, muss noch implementiert werden """
    newposition = position -5
    print("zoomin")


def zoomout(position):
    """ zoomt raus, muss noch implementiert werden """
    newposition = position + 5
    print("zoomout")


def term_eingeben_window() -> None:
    """
    Fenster, wo die user ihre funktion eingeben können
    :return: None
    """
    win = base_tk(name="Term/e eingeben")

    Label(win, text="hier Funktionsterm eingeben: ").pack(side=TOP, anchor=NW)
    f_entry = Entry(win)
    f_entry.pack(side=TOP, anchor=NW)
    # labels & entries for bounds of x and y axis
    Label(win, text="x von, bis: ").pack(side=TOP, anchor=NW)
    x_von_bis_entry = Entry(win)
    x_von_bis_entry.pack(side=TOP, anchor=NW)
    Label(win, text="y von, bis: ").pack(side=TOP, anchor=NW)
    y_von_bis_entry = Entry(win)
    y_von_bis_entry.pack(side=TOP, anchor=NW)

    def von_bis(get_from: str) -> tuple[float, float]:
        """
        Holt von und bis werde aus einem string (von, bis)
        :param get_from: der string, aus dem die limits geholt werden sollen
        :type get_from: str
        :return: die Werte aus dem String
        :rtype: tuple[float, float]
        """
        input_bereinigt = leerzeichen_raus_machen(get_from)
        von, bis = input_bereinigt.split(",")
        return float(von), float(bis)


    def _get_help() -> None:
        """ ruft das hilfefenster auf """
        _help = base_tk(size="800x500", name="Hilfe - Funktionen")
        Label(_help,
        text="In das Input feld die Funktion eingeben, die exponenten werden mit einem ^ notiert.\n\
                Also z.B.: 1x^3 + 2x^2 + 1x + 0\n\
                Wenn der erste term ein x vorne hat, muss eine 1 davor geschrieben werden!").pack()
        Button(_help, text="Ok", command=_help.destroy).pack()

    def leerzeichen_raus_machen(inp: str) -> str:
        """ entfernt alle leerzeichen aus einem string """
        outp = ""
        # enumeriert über input mit (index, wert)
        for _, character in enumerate(inp):
            if character != " ": outp += character
        return outp

    def funktion_berechnen() -> None:
        """ holt werte und berechnet die funktion """
        # werte holen
        def get_term(term: str) -> tuple:
            # wenn kein x vorhanden ist, dann ist es ein konstanter term
            if 'x' not in term:
                return int(term), 0
            # wenn kein exponent vorhanden ist, dann ist es ein linearer term
            elif '^' not in term:
                return int(term[:-1]), 1
            # sonst ist es ein term mit exponent
            else:
                # returned basis und exponent
                return int(term[:term.index('x')]), int(term[term.index('^')+1:])

        # gibt term aus, vorzeichen gehören zu den darauf folgenden termen
        def get_zahlen(inp: str) -> list:
            """ holt wichtige zahlen aus dem string """
            # regex magie um alle zahlen zu finden
            dirty_terme = re.findall(r"[+-]?\d*x?\^?\d*", inp)

            # entfernt alle leeren strings
            terme = [t for t in dirty_terme if t != '']
            return terme

        def array_von_leeren_strings_befreien(arr: str) -> str:
            """ entfernt alle leeren strings aus einem array """
            output_string = ""
            # schaut durch alle items im array und filtert alle leeren strings raus
            for a in arr:
                if a != '': output_string += a
            return output_string

        def ableitungs_generator(basis: list[tuple[float, float]]) -> list[tuple[float, float]]:
            ableitung = []
            for basis, exp in basis:
                ableitung.append(basis * exp, exp - 1)
            return ableitung

        # holt input und bereinigt ihn
        input_str = array_von_leeren_strings_befreien(f_entry.get())
        terme = get_zahlen(input_str)
        basis_exponent_paare = [get_term(t) for t in terme]



        # erstellt plot
        fig = plt.Figure(figsize=(10, 20), dpi=100)
        rg = np.arange(-100, 200, 0.2)
        ax = fig.add_subplot()
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_title("Funktionsgraph")
        x_von, x_bis = von_bis(x_von_bis_entry.get())
        ax.set_xlim(x_von, x_bis)
        y_von, y_bis = von_bis(y_von_bis_entry.get())
        ax.set_ylim(y_von, y_bis)
        ax.grid()
        ax.spines.left.set_position('zero')
        ax.spines.right.set_color('none')
        ax.spines.bottom.set_position('zero')
        ax.spines.top.set_color('none')
        ax.yaxis.set_ticks_position('left')
        ax.xaxis.set_ticks_position('bottom')

        ax.scatter(0, 0, color="purple", label="Nullpunkt")


        # berechnet das richtig dismal lol. ich bin so dumm
        def f(x: float) -> float:
            """ berechnet die funktion """
            y = 0
            for b, e in basis_exponent_paare:
                y += b * (x ** e)
            return y

        ax.plot(rg, f(rg), label="linie")
        # setzt eine Legende in die obere rechte Ecke
        ax.legend(loc="upper right")

        cv = FigureCanvasTkAgg(fig, master=win)
        cv.draw()

        def kurvendiskussion():
            def ableitungs_generator(string: str):

                pass
            pass


        kurvendiskussion_button = Button(win, text="Kurvendiskussion", command=kurvendiskussion)
        kurvendiskussion_button.pack(side=TOP, anchor=NW)
        cv.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True)

    _b = Button(win, text="Los gehts!", command=funktion_berechnen)
    Button(win, text="?", command=_get_help).pack(side=TOP, anchor=NE)

    _b.pack(side=TOP, anchor=NW)
    win.mainloop()


def open_trigonometrische_window() -> None:
    """ Fenster für trigonometrische funktionen """
    win = base_tk(name="Trigonometrische Funktionen Rechner")

    # labels und entries
    von_label =  Label(win, text="Von: ")
    von_entry = Entry(win)
    bis_label = Label(win, text="Bis: ")
    bis_entry = Entry(win)
    a_label = Label(win, text="a: ")
    a_entry = Entry(win)
    x_label = Label(win, text="x: ")
    x_entry = Entry(win)
    x_achse_label = Label(win, text="x-Achsenbeschriftung:")
    x_achse_entry = Entry(win)
    y_achse_label = Label(win, text="y-Achsenbeschriftung:")
    y_achse_entry = Entry(win)

    # figure for matplotlib to plot lines on
    fig = plt.Figure(figsize=(10, 10), dpi=100)

    # canvas-like thing for actually drawing
    ax = fig.add_subplot()

    # range of numhers, see numpy.org for doc on arange
    # put canvas onto tk window
    cv = FigureCanvasTkAgg(fig, master=win)
    cv.draw()

    def trigonometrische_ausrechnen():
        def grad_in_bogen(Awert):
            return (Awert / 180) * math.pi

        def bogen_in_grad(Xwert):
            return (x / math.pi ) * 180

        von = float(von_entry.get())
        bis = float(bis_entry.get())
        a = float(a_entry.get())

         # checken ob werte floats sind
        assert entry_is_float(von)
        assert entry_is_float(bis)
        assert entry_is_float(a)
        # assert entry_is_float(x)

        x = np.arange(0,4*np.pi,0.1)   # start,stop,step
        y = np.sin(x)

         # range mit von - bis
        rg = np.arange(von, bis, 0.2)

        # setze namen der achsen
        ax.set_xlabel(x_achse_entry.get())
        ax.set_ylabel(y_achse_entry.get())

        plt.plot(x,y)
        cv.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True)


        print("lol")


    def trigonometische_help() -> None:
        pass

      # display everything
    von_label.pack(side=TOP, anchor=NW)
    von_entry.pack(side=TOP, anchor=NW)
    bis_label.pack(side=TOP, anchor=NW)
    bis_entry.pack(side=TOP, anchor=NW)
    a_label.pack(side=TOP, anchor=NW)
    a_entry.pack(side=TOP, anchor=NW)
    x_label.pack(side=TOP, anchor=NW)
    x_entry.pack(side=TOP, anchor=NW)
    x_achse_label.pack(side=TOP, anchor=NW)
    x_achse_entry.pack(side=TOP, anchor=NW)
    y_achse_label.pack(side=TOP, anchor=NW)
    y_achse_entry.pack(side=TOP, anchor=NW)

    # use function declared earlier to compute stuff
    Button(win, command=trigonometrische_ausrechnen, text="Anzeigen").pack(side=TOP,
                                                                 anchor=NW)
    Button(win, text="?", command=trigonometische_help).pack(side=TOP, anchor=NE)

    win.mainloop()


def open_exponential_window() -> None:
    """ Fenster für exponentielle funktionen """
    win = base_tk(name="Exponential Funktionen Rechner")

    # labels und entries
    von_label = Label(win, text="anfang: ")
    von_entry = Entry(win)
    bis_label = Label(win, text="ende: ")
    bis_entry = Entry(win)
    a_label = Label(win, text="a: ")
    a_entry = Entry(win)
    # x_label = Label(win, text="x: ")
    # x_entry = Entry(win)
    x_achse_label = Label(win, text="x-Achsenbeschriftung:")
    x_achse_entry = Entry(win)
    y_achse_label = Label(win, text="y-Achsenbeschriftung:")
    y_achse_entry = Entry(win)

    # figure for matplotlib to plot lines on
    fig = plt.Figure(figsize=(10, 10), dpi=100)

    # canvas-like thing for actually drawing
    ax = fig.add_subplot()

    # range of numhers, see numpy.org for doc on arange
    # put canvas onto tk window
    cv = FigureCanvasTkAgg(fig, master=win)
    cv.draw()

    # function in function to be used on button click
    def exponential_ausrechnen() -> None:
        """ berechnet die funktion """
        # werte holen
        von = float(von_entry.get())
        bis = float(bis_entry.get())
        a = float(a_entry.get())
        # x = float(x_entry.get())

        # checken ob werte floats sind
        assert entry_is_float(von)
        assert entry_is_float(bis)
        assert entry_is_float(a)
        # assert entry_is_float(x)

        # range mit von - bis
        rg = np.arange(von, bis, 0.2)

        # setze namen der achsen
        ax.set_xlabel(x_achse_entry.get())
        ax.set_ylabel(y_achse_entry.get())

        # lineare funktion plotten
        ax.plot(rg, a ** rg)

        cv.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True)

    def exponential_help() -> None:
        pass

    # display everything
    von_label.pack(side=TOP, anchor=NW)
    von_entry.pack(side=TOP, anchor=NW)
    bis_label.pack(side=TOP, anchor=NW)
    bis_entry.pack(side=TOP, anchor=NW)
    a_label.pack(side=TOP, anchor=NW)
    a_entry.pack(side=TOP, anchor=NW)
    x_achse_label.pack(side=TOP, anchor=NW)
    x_achse_entry.pack(side=TOP, anchor=NW)
    y_achse_label.pack(side=TOP, anchor=NW)
    y_achse_entry.pack(side=TOP, anchor=NW)

    # use function declared earlier to compute stuff
    Button(win, command=exponential_ausrechnen, text="Anzeigen").pack(side=TOP,
                                                                 anchor=NW)
    Button(win, text="?", command=exponential_help).pack(side=TOP, anchor=NE)

    win.mainloop()


def open_integralrechnung_window() -> None:
    """ Fenster für integralrechnung funktionen """
    win = base_tk(name="Integralrechnung")
    win.mainloop()


def open_hilfe_window() -> None:
    """ Fenster für Hilfe zum Programm """
    win = base_tk(name="hilfe")
    hilfe_label =  Label(win, text="Wenn du etwas nicht verstehst, dann bekommst du bei jedem Fenster individuell Hilfe")
    hilfe_label.pack(side=TOP, anchor=NW)
    win.mainloop()


def open_ueber_window() -> None:
    """ Fenster für Informationen über das Programm """
    win = base_tk(name="über")
    hilfe_label =  Label(win, text="Diese Software wurde für den Informatik Untericht entwickelt")
    hilfe2_label =  Label(win, text="Ziel ist es das der User Mathematische Funktionen ausgerechnet und erklärt bekommt")
    hilfe3_label =  Label(win, text="Version: 0.1")
    hilfe4_label =  Label(win, text="Lizenz: GPL_2.0")
    hilfe5_label =  Label(win, text="Autor:Loste Kinder ")
    hilfe6_label =  Label(win, text="Copyright: 2023")
    hilfe7_label =  Label(win, text="Link: https://github.com/hyperbel/MatheProjekt22_23")
    hilfe_label.pack(side=TOP, anchor=NW)
    hilfe2_label.pack(side=TOP, anchor=NW)
    hilfe3_label.pack(side=TOP, anchor=NW)
    hilfe4_label.pack(side=TOP, anchor=NW)
    hilfe5_label.pack(side=TOP, anchor=NW)
    hilfe6_label.pack(side=TOP, anchor=NW)
    hilfe7_label.pack(side=TOP, anchor=NW)
    win.mainloop()


def open_verlauf_window() -> None:
    """ Fenster für den Verlauf """
    win = base_tk(name="verlauf")
    con = sqlite3.connect("mathe.db")
    cur = con.cursor()
    userid=1
    sql = f"SELECT funktion from funktionen WHERE userid=\'{userid}\';"
    ergebnis = cur.execute(sql).fetchall()
    print (ergebnis)
    win.mainloop()


def open_main_window() -> None:
    """ Hauptfenster """

    root = Tk()

    menu = get_menu(root)
    root.config(menu=menu)
    root.title("Mathe-Funktionen-Rechner 2022/23")
    root.geometry("350x345")
    # add Listbox to root
    listbox = Listbox(root, width=20, height=100)
    listbox.pack(side=LEFT, fill=BOTH, expand=False)
    # add random items to listbox
    for i in range(100):
        listbox.insert(END, f"item {i}")
    # add scrollbar to root
    scrollbar = Scrollbar(root)
    scrollbar.pack(side=RIGHT, fill=BOTH)
    # add scrollbar to listbox
    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)


    root.mainloop()


# generiert main menu fuer das root win
def get_menu(root) -> Menu:
    """ generiert main menu für das root win """
    _menu = Menu(root, tearoff=0)
    funktionen_menu = Menu(_menu, tearoff=0)
    account_menu = Menu(_menu, tearoff=0)
    hilfe_menu = Menu(_menu, tearoff=0)

    funktionen_menu.add_command(label="Term/e eingeben",
                                command=term_eingeben_window)
    funktionen_menu.add_command(label="Trigonometrische",
                                command=open_trigonometrische_window)
    funktionen_menu.add_command(label="Exponential",
                                command=open_exponential_window)
    """funktionen_menu.add_command(label="Differenzial",
                                command=open_defferenzial_window)"""
    # Differenzial Rechnen = Ableitungen, deshalb wir dies in dem anderen Fenster sein
    funktionen_menu.add_command(label="Integralrechnung",
                                command=open_integralrechnung_window)
    _menu.add_cascade(label="Funktionen", menu=funktionen_menu)

    account_menu.add_command(label="Logout",
                             command=root.destroy)
    """account_menu.add_command(label="Verlauf",
                             command=open_verlauf_window)"""
    _menu.add_cascade(label="Account", menu=account_menu)

    hilfe_menu.add_command(label="hilfe",
                                 command=open_hilfe_window)
    _menu.add_cascade(label="Hilfe", menu=hilfe_menu)
    hilfe_menu.add_command(label="über",
                                 command=open_ueber_window)
    return _menu
