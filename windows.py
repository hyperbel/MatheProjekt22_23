from tkinter import Tk, TOP, BOTH, Menu, Label, Entry, Button, NW, SW, NE
from tkinter import BOTTOM
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import re

# checks if input (usally from entry) is of type float
def entry_is_float(inp):
    # magic regex for checking if input is float type
    if type(inp) == float:
        return True
    elif type(inp) != str:
        print(type(inp))
    res = re.match(r"(\+|\-)?\d+(,\d+)?$", inp)
    return res is not None


# basic window config
def base_Tk(size="900x600", name="") -> Tk:
    win = Tk()
    win.geometry(size)
    win.title(name)
    return win


def zoomin(position):
	newposition = position -5
	print("zoomin")


def zoomout(position):
	newposition = position + 5
	print("zoomout")


# rechner fuer lineare funktionen
def open_linear_window() -> None:
    def _get_linea_help() -> None:
        _help = base_Tk(size="800x500", name="Hilfe - quadratische Funktionen")
        Label(_help,
              text="Lineare Funktionen sind Funktionen die als Funktionsterm ein Plynom des ersten Grades  besitzen.").pack()
        Button(_help, text="Ok", command=_help.destroy).pack()

    win = base_Tk(name="Lineare Funktionen Rechner")

    # labels und entries
    von_label = Label(win, text="anfang: ")
    von_entry = Entry(win)
    bis_label = Label(win, text="ende: ")
    bis_entry = Entry(win)
    m_label = Label(win, text="m: ")
    m_entry = Entry(win)
    b_label = Label(win, text="b: ")
    b_entry = Entry(win)
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
    def linear_ausrechnen() -> None:
        # werte holen
        von = float(von_entry.get())
        bis = float(bis_entry.get())
        m = float(m_entry.get())
        b = float(b_entry.get())

        # checken ob werte floats sind
        assert entry_is_float(von)
        assert entry_is_float(bis)
        assert entry_is_float(m)
        assert entry_is_float(b)

        # range mit von - bis
        rg = np.arange(von, bis, 0.2)

        # setze namen der achsen
        ax.set_xlabel(x_achse_entry.get())
        ax.set_ylabel(y_achse_entry.get())

        # lineare funktion plotten
        ax.plot(rg, m * rg + b)

        cv.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True)

        def nst() -> float:
            # 0 = m * x + b | -b
            # -b = m * x    | /m
            # -b / m = x    | zusammengefasst: -(b / m) = x
            x = -(b/m)    #
            return x

        # Nonestelle anzeigen
        nst = f"N({nst()}|0)"
        NST_label = Label(win, text=nst)
        NST_label.pack(side=BOTTOM, anchor=SW)

        # y-achsen-abschnitt ist einfach b weil x = None macht y = m * 0 + b, also 0 + b = b
        yaa = f"Y-Achsenabschnitt: {b}"
        YAA_label = Label(win, text=yaa)
        YAA_label.pack(side=BOTTOM, anchor=SW)

    # display everything
    von_label.pack(side=TOP, anchor=NW)
    von_entry.pack(side=TOP, anchor=NW)
    bis_label.pack(side=TOP, anchor=NW)
    bis_entry.pack(side=TOP, anchor=NW)
    m_label.pack(side=TOP, anchor=NW)
    m_entry.pack(side=TOP, anchor=NW)
    b_label.pack(side=TOP, anchor=NW)
    b_entry.pack(side=TOP, anchor=NW)
    x_achse_label.pack(side=TOP, anchor=NW)
    x_achse_entry.pack(side=TOP, anchor=NW)
    y_achse_label.pack(side=TOP, anchor=NW)
    y_achse_entry.pack(side=TOP, anchor=NW)

    # use function declared earlier to compute stuff
    Button(win, command=linear_ausrechnen, text="Anzeigen").pack(side=TOP,
                                                                 anchor=NW)
    Button(win, text="?", command=_get_linea_help).pack(side=TOP, anchor=NE)


    
    win.mainloop()


# rechner fuer quadratische funktionen
def open_quadratisch_window() -> None:
    def _get_quad_help() -> None:
        _help = base_Tk(size="800x500", name="Hilfe - quadratische Funktionen")
        Label(_help,
              text="Quadratische Funktionen sind Funktionen die als Funktionsterm ein Plynom vom Grad 3 besitzen.").pack()
        Button(_help, text="Ok", command=_help.destroy).pack()
    win = base_Tk(name="Quadratische Funktionen Rechner")

    x_a_l = Label(win, text="x-Achsenname")
    x_a_e = Entry(win)
    y_a_l = Label(win, text="y-Achsenname")
    y_a_e = Entry(win)
    von_l = Label(win, text="von: ")
    von_e = Entry(win)
    bis_l = Label(win, text="bis: ")
    bis_e = Entry(win)
    a_l = Label(win, text="a: ")
    a_e = Entry(win)
    b_l = Label(win, text="b: ")
    b_e = Entry(win)
    c_l = Label(win, text="c: ")
    c_e = Entry(win)

    fig = plt.Figure(figsize=(10, 20), dpi=100)

    def quad_berechnen() -> None:
        # werte holen
        von = float(von_e.get())
        bis = float(bis_e.get())
        a = float(a_e.get())
        b = float(b_e.get())
        c = float(c_e.get())

        # range mit von - bis
        rg = np.arange(von, bis, 0.2)

        fig.clear()

        ax = fig.add_subplot()

        # setze namen der achsen
        ax.set_xlabel(x_a_e.get())
        ax.set_ylabel(y_a_e.get())

        # lineare funktion plotten
        quad_term = a * (rg ** 2)
        line_term = b * rg
        y = quad_term + line_term + c
        ax.plot(rg, y)

        import math
        x1 = -(b/2) + math.sqrt(abs(((b/2) ** 2) - c))
        x2 = -(b/2) - math.sqrt(abs(((b/2) ** 2) - c))
        nst1 = f"N({x1}|0)"
        nst2 = f"N({x2}|0)"

        yaa = f"Y-Achsenabschnitt: {c}"

        cv = FigureCanvasTkAgg(fig, master=win)
        cv.draw()

        cv.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True)

        Label(win, text=nst1).pack(side=TOP, anchor=NW)
        Label(win, text=nst2).pack(side=TOP, anchor=NW)
        Label(win, text=yaa).pack(side=TOP, anchor=NW)

    Button(win, text="ausrechnen", command=quad_berechnen).pack()
    Button(win, text="?", command=_get_quad_help).pack(side=TOP, anchor=NE)

    x_a_l.pack(side=TOP, anchor=NW)
    x_a_e.pack(side=TOP, anchor=NW)
    y_a_l.pack(side=TOP, anchor=NW)
    y_a_e.pack(side=TOP, anchor=NW)
    von_l.pack(side=TOP, anchor=NW)

    von_e.pack(side=TOP, anchor=NW)
    bis_l.pack(side=TOP, anchor=NW)
    bis_e.pack(side=TOP, anchor=NW)
    a_l.pack(side=TOP, anchor=NW)
    a_e.pack(side=TOP, anchor=NW)
    b_l.pack(side=TOP, anchor=NW)
    b_e.pack(side=TOP, anchor=NW)
    c_l.pack(side=TOP, anchor=NW)
    c_e.pack(side=TOP, anchor=NW)

    win.mainloop()


def open_ganzrazionale_window() -> None:
    win = base_Tk(name="Ganzrationale Funktionen Rechner")

    Label(win, text="hier Funktionsterm eingeben: ").pack(side=TOP, anchor=NW)
    fEntry = Entry(win)

    def _get_help() -> None:
        _help = base_Tk(size="100x500", name="Hilfe - Ganzrationale Funktionen")
        Label(_help, text="In das Input feld die Funktion eingeben, die exponenten werden mit einem ^ notiert.\nAlso x^3 + 2x^2 + 1x + 0").pack()
        Button(_help, text="Ok", command=_help.destroy).pack()

    def ganzrationale_berechnen() -> None:
        def __clean_str_of_char(inp: str, ch) -> str:
            outp = ""
            for i in range(len(inp)):
                if inp[i] != ch: outp += inp[i]
            return outp

        # werte holen
        def get_term(term: str) -> tuple:
            # wenn kein x vorhanden ist, dann ist es ein konstanter term
            if 'x' not in term:
                return (int(term), 0)
            # wenn kein exponent vorhanden ist, dann ist es ein linearer term
            elif '^' not in term:
                return (int(term[:-1]), 1)
            # sonst ist es ein term mit exponent
            else:
                # returnt basis und exponent
                return (int(term[:term.index('x')]), int(term[term.index('^')+1:]))
        
        # gibt term aus, vorzeichen gehören zu den darauf folgenden termen
        def get_zahlen(inp: str) -> list:
            # regex magic for finding terms
            dirty_terme = re.findall(r"[+-]?\d*x?\^?\d*", inp)

            terme = [t for t in dirty_terme if t != '']
            return terme

        input_str = __clean_str_of_char(fEntry.get(), '')
        terme = get_zahlen(input_str)
        basis_exponent_paare = [get_term(t) for t in terme]

        # funktion welche ganzrationale funktionen berechnet
        def ganzrationale_funktion(x: float) -> float:
            ys = []
            for b, e in basis_exponent_paare:
                # appendiere die berechneten werte
                ys.append(b * (x ** e))
                # print out the value


            return ys

        fig = plt.Figure(figsize=(10, 20), dpi=100)
        rg = np.arange(-100, 200, 0.2)
        ax = fig.add_subplot()
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.plot(rg, basis_exponent_paare[0][0] * (rg ** basis_exponent_paare[0][1]))

        cv = FigureCanvasTkAgg(fig, master=win)
        cv.draw()

        cv.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True)


    _b = Button(win, text="Los gehts!", command=ganzrationale_berechnen)
    Button(win, text="?", command=_get_help).pack(side=TOP, anchor=NE)
    
    fEntry.pack(side=TOP, anchor=NW)
    _b.pack(side=TOP, anchor=NW)
    win.mainloop()


def open_trigonometrische_window() -> None:
    win = base_Tk(name="Trigonometrische Funktionen Rechner")
    win.mainloop()


# f(x) = a ^ x
def open_exponential_window() -> None:
    win = base_Tk(name="Exponential Funktionen Rechner")

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
        import math
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
    # x_label.pack(side=TOP, anchor=NW)
    # x_entry.pack(side=TOP, anchor=NW)
    x_achse_label.pack(side=TOP, anchor=NW)
    x_achse_entry.pack(side=TOP, anchor=NW)
    y_achse_label.pack(side=TOP, anchor=NW)
    y_achse_entry.pack(side=TOP, anchor=NW)

    # use function declared earlier to compute stuff
    Button(win, command=exponential_ausrechnen, text="Anzeigen").pack(side=TOP,
                                                                 anchor=NW)
    Button(win, text="?", command=exponential_help).pack(side=TOP, anchor=NE)

    win.mainloop()


def open_defferenzial_window() -> None:
    win = base_Tk(name="Einstieg Diefferenzialrechnung")
    win.mainloop()


def open_kurvendiskussion_window() -> None:
    win = base_Tk(name="Kurvendiskussion")
    win.mainloop()


def open_integralrechnung_window() -> None:
    win = base_Tk(name="Integralrechnung")
    win.mainloop()


def open_hilfe_window() -> None:
    win = base_Tk(name="hilfe")
    win.mainloop()


def open_ueber_window() -> None:
    win = base_Tk(name="über")
    win.mainloop()


def open_verlauf_window() -> None:
    win = base_Tk(name="verlauf")
    win.mainloop()


def open_main_window() -> None:
    root = Tk()

    menu = get_menu(root)
    root.config(menu=menu)
    root.title("Mathe-Funktionen-Rechner 2022/23")
    root.geometry("350x345")
    root.mainloop()


# generiert main menu fuer das root win
def get_menu(root) -> Menu:
    _menu = Menu(root, tearoff=0)
    funktionen_menu = Menu(_menu, tearoff=0)
    account_menu = Menu(_menu, tearoff=0)
    hilfe_menu = Menu(_menu, tearoff=0)

    funktionen_menu.add_command(label="Linear",
                                command=open_linear_window)
    funktionen_menu.add_command(label="Quadratisch",
                                command=open_quadratisch_window)
    funktionen_menu.add_command(label="Ganzrationale Funktionen",
                                command=open_ganzrazionale_window)
    funktionen_menu.add_command(label="Trigonometrische",
                                command=open_trigonometrische_window)
    funktionen_menu.add_command(label="Exponential",
                                command=open_exponential_window)
    funktionen_menu.add_command(label="Differenzial",
                                command=open_defferenzial_window)
    funktionen_menu.add_command(label="Kurvendiskusion",
                                command=open_kurvendiskussion_window)
    funktionen_menu.add_command(label="Integralrechnung",
                                command=open_integralrechnung_window)
    _menu.add_cascade(label="Funktionen", menu=funktionen_menu)

    account_menu.add_command(label="Logout",
                             command=open_linear_window)
    account_menu.add_command(label="Verlauf",
                             command=open_verlauf_window)
    _menu.add_cascade(label="Account", menu=account_menu)

    hilfe_menu.add_command(label="hilfe",
                                 command=open_hilfe_window)
    _menu.add_cascade(label="Hilfe", menu=hilfe_menu)
    hilfe_menu.add_command(label="über",
                                 command=open_ueber_window)
    return _menu
