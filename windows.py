"""@package windows
Fenster für die GUI
"""
import re
import sqlite3
from tkinter import Tk, TOP, BOTH, Menu, Label, Entry, Button
from tkinter import NW, NE, Listbox, LEFT, END, Scrollbar, RIGHT, Frame, Radiobutton, StringVar
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

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

def open_trigonometrische_window() -> None:
    """ Fenster für trigonometrische funktionen """
    win = base_tk(name="Trigonometrische Funktionen Rechner")

    # labels und entries
    amplitude_label =  Label(win, text="Amplitude:")
    amplitude_entry = Entry(win)
    frequenz_label = Label(win, text="Frequenz:")
    frequenz_entry = Entry(win)
    phase_label = Label(win, text="Phase:")
    phase_entry = Entry(win)
    function_type_var = StringVar(value='sin')
    sin_radio = Radiobutton(win, text='Sinus', variable=function_type_var, value='sin')
    cos_radio = Radiobutton(win, text='Cosinus', variable=function_type_var, value='cos')
    tan_radio = Radiobutton(win, text='Tangens', variable=function_type_var, value='tan')



    # figure for matplotlib to plot lines on
    fig = plt.Figure(figsize=(10, 10), dpi=100)

    # canvas-like thing for actually drawing
    ax = fig.add_subplot()

    # range of numhers, see numpy.org for doc on arange
    # put canvas onto tk window
    canvas = FigureCanvasTkAgg(fig, master=win)
    canvas.draw()

    def trigonometrische_ausrechnen():

        amp = float(amplitude_entry.get())
        freq = float(frequenz_entry.get())
        phas = float(phase_entry.get())

         # checken ob werte floats sind
        assert entry_is_float(amp)
        assert entry_is_float(freq)
        assert entry_is_float(phas)
        # assert entry_is_float(x)

         # x-Werte des Graphen berechnen
        x = np.linspace(0, 2*np.pi, 1000)

        if function_type_var.get() == 'sin':
            print("sin")
            y = amp * np.sin(freq * x + phas)
            title = 'Sinusfunktion'
            ax.clear()
            ax.plot(x, y)
            ax.set_xlabel('x')
            ax.set_ylabel('y')
            ax.set_title(title)
            canvas.draw()
        elif function_type_var.get() == 'cos':
            print("cos")
            y = amp * np.cos(freq * x + phas)
            title = 'Cosinusfunktion'
            ax.clear()
            ax.plot(x, y)
            ax.set_xlabel('x')
            ax.set_ylabel('y')
            ax.set_title(title)
            canvas.draw()
        elif function_type_var.get() == 'tan':
            print("tan")
            y = amp * np.tan(freq * x + phas)
            title = 'Tangensfunktion'
            ax.clear()
            ax.plot(x, y)
            ax.set_xlabel('x')
            ax.set_ylabel('y')
            ax.set_title(title)
            canvas.draw()

        
         # range mit von - bis
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True)


        print("lol")


    def trigonometische_help() -> None:
        pass

      # display everything
    amplitude_label.pack(side=TOP, anchor=NW)
    amplitude_entry.pack(side=TOP, anchor=NW)
    frequenz_label.pack(side=TOP, anchor=NW)
    frequenz_entry.pack(side=TOP, anchor=NW)
    phase_label.pack(side=TOP, anchor=NW)
    phase_entry.pack(side=TOP, anchor=NW)
    tan_radio.pack(side=TOP, anchor=NW)
    cos_radio.pack(side=TOP, anchor=NW)
    sin_radio.pack(side=TOP, anchor=NW)

    # use function declared earlier to compute stuff
    Button(win, command=trigonometrische_ausrechnen, text="Anzeigen").pack(side=TOP,
                                                                 anchor=NW)
    Button(win, text="?", command=trigonometische_help).pack(side=TOP, anchor=NE)

    win.mainloop()


def open_exponential_window() -> None:
    """ Fenster für exponentielle funktionen """
    win = base_tk(name="Exponential Funktionen Rechner")

    # entries
    von_entry = Entry(win)
    bis_entry = Entry(win)
    a_entry = Entry(win)
    # x_label = Label(win, text="x: ")
    # x_entry = Entry(win)
    x_achse_entry = Entry(win)
    y_achse_entry = Entry(win)

    # figure for matplotlib to plot lines on
    fig = plt.Figure(figsize=(10, 10), dpi=100)

    # canvas-like thing for actually drawing
    ax = fig.add_subplot()

    # range of numhers, see numpy.org for doc on arange
    # put canvas onto tk window
    canvas = FigureCanvasTkAgg(fig, master=win)
    canvas.draw()

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
        x_werte = np.arange(von, bis, 0.2)

        # setze namen der achsen
        ax.set_xlabel(x_achse_entry.get())
        ax.set_ylabel(y_achse_entry.get())

        # lineare funktion plotten
        ax.plot(x_werte, a ** x_werte)

        canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True)

    def exponential_help() -> None:
        pass

    # display everything
    Label(win, text="anfang: ").pack(side=TOP, anchor=NW)
    von_entry.pack(side=TOP, anchor=NW)
    Label(win, text="ende: ").pack(side=TOP, anchor=NW)
    bis_entry.pack(side=TOP, anchor=NW)
    Label(win, text="a: ").pack(side=TOP, anchor=NW)
    a_entry.pack(side=TOP, anchor=NW)
    Label(win, text="x-Achsenbeschriftung:").pack(side=TOP, anchor=NW)
    x_achse_entry.pack(side=TOP, anchor=NW)
    Label(win, text="y-Achsenbeschriftung:").pack(side=TOP, anchor=NW)
    y_achse_entry.pack(side=TOP, anchor=NW)

    # use function declared earlier to compute stuff
    Button(win, command=exponential_ausrechnen, text="Anzeigen").pack(side=TOP,
                                                                 anchor=NW)
    Button(win, text="?", command=exponential_help).pack(side=TOP, anchor=NE)


    win.mainloop()


def open_integralrechnung_window() -> None:
    """ Fenster für integralrechnung funktionen """
    win = base_tk(name="Integralrechnung")

    # labels und entries
    funktion_label =  Label(win, text="Funktion:")
    funktion_entry = Entry(win)
    anfangX_label = Label(win, text="Anfang von X:")
    anfangX_entry = Entry(win)
    endeX_label = Label(win, text="Ende von X:")
    endeX_entry = Entry(win)  

    def integral_ausrechnen():

        # Hohle Werte
        funktion_text = funktion_entry.get()
        anfangx = float(anfangX_entry.get())
        endex = float(endeX_entry.get())
        y = int(y_entry.get())

         # checken ob werte floats sind
        assert entry_is_float(anfangx)
        assert entry_is_float(endex)
        # assert entry_is_float(x)

        # hier wird durch ein bischen numpy Magie das Integral einer Funktion berechnet
        func = lambda x: eval(funktion_text)

        x = np.linspace(anfangx, endex, y)
        y = func(x)
        integral = np.trapz(y, x)

        # Rundet das Ergebnis und gibt es in der Box aus
        ergebnis = round(integral)
        loesung_entry.delete(0, END)
        loesung_entry.insert(0, str(ergebnis))


        canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

        ax.clear()
        ax.plot(x, y)
        ax.fill_between(x, y, 0, alpha=0.2)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_title("Integral")
        canvas.draw()


    y_label = Label(win, text="Y:")
    y_entry = Entry(win)
    loesung_label = Label(win, text="Lösung")
    loesung_entry = Entry(win)

    # figure for matplotlib to plot lines on
    fig = plt.Figure(figsize=(10, 10), dpi=100)

    # canvas-like thing for actually drawing
    ax = fig.add_subplot()

    # range of numhers, see numpy.org for doc on arange
    # put canvas onto tk window
    canvas = FigureCanvasTkAgg(fig, master=win)
    canvas.draw()
       # range mit von - bis
    
    
    def integral_help() -> None:
        pass

      # display everything
    funktion_label.pack(side=TOP, anchor=NW)
    funktion_entry.pack(side=TOP, anchor=NW)
    anfangX_label.pack(side=TOP, anchor=NW)
    anfangX_entry.pack(side=TOP, anchor=NW)
    endeX_label.pack(side=TOP, anchor=NW)
    endeX_entry.pack(side=TOP, anchor=NW)
    y_label.pack(side=TOP, anchor=NW)
    y_entry.pack(side=TOP, anchor=NW)
    loesung_label.pack(side=TOP, anchor=NW)
    loesung_entry.pack(side=TOP, anchor=NW)
 
    # use function declared earlier to compute stuff
    Button(win, command=integral_ausrechnen, text="Anzeigen").pack(side=TOP,
                                                                 anchor=NW)
    Button(win, text="?", command=integral_help).pack(side=TOP, anchor=NE)

    win.mainloop()



def open_hilfe_window() -> None:
    """ Fenster für Hilfe zum Programm """
    win = base_tk(name="hilfe")
    hilfe_label =  Label(win,
                         text="Wenn du etwas nicht verstehst,\
                               dann bekommst du bei jedem Fenster individuell Hilfe")
    hilfe_label.pack(side=TOP, anchor=NW)
    win.mainloop()


def open_ueber_window() -> None:
    """ Fenster für Informationen über das Programm """
    win = base_tk(name="über")
    hilfe_label =  Label(win, text="Diese Software wurde für den Informatik Untericht entwickelt")
    hilfe2_label =  Label(win,
                          text="Ziel ist es das der User Mathematische Funktionen\
                                ausgerechnet und erklärt bekommt")
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


def get_verlauf(userid):
    con = sqlite3.connect("mathe.db")
    cur = con.cursor()
    userid=1
    sql = f"SELECT funktion from funktionen WHERE userid=\'{userid}\';"
    ergebnis = cur.execute(sql).fetchall()
    print (ergebnis)
    return ergebnis


def save_function(funktion, userid):
    con = sqlite3.Connection("mathe.db")
    cur = con.cursor()
    sql = f"INSERT INTO funktionen VALUES('\{funktion}\','\{userid}\');"
    print("f")


def leerzeichen_raus_machen(inp: str) -> str:
    """ entfernt alle leerzeichen aus einem string """
    outp = ""
    # enumeriert über input mit (index, wert)
    for _, character in enumerate(inp):
        if character != " ":
            outp += character
    return outp


def get_term(term: str) -> tuple:
    """ gibt einen term als tuple zurück (koeffizient, exponent)
    :param term: term als string
    :type term: str
    :return: tuple mit koeffizient und exponent
    :rtype: tuple
    """

    # wenn kein x vorhanden ist, dann ist es ein konstanter term
    if 'x' not in term:
        return int(term), 0
    # wenn kein exponent vorhanden ist, dann ist es ein linearer term
    if '^' not in term:
        return int(term[:-1]), 1
    # sonst ist es ein term mit exponent
    return int(term[:term.index('x')]), int(term[term.index('^')+1:])


def array_von_leeren_strings_befreien(arr: str) -> str:
    """entfernt alle leeren strings aus einem array """
    output_string = ""
    # schaut durch alle items im array und filtert alle leeren strings raus
    for a in arr:
        if a != '':
            output_string += a
    return output_string



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

def ableitungs_generator(basis: list[tuple[float, float]]) -> list[tuple[float, float]]:
    """generiert die ableitung einer funktion
    :param basis: basis der funktion
    :type basis: list[tuple[float, float]]
    :return: ableitung der funktion
    :rtype: list[tuple[float, float]]
    """
    ableitung = []
    for b, exp in basis:
        ableitung.append((b * exp, exp - 1))
    return ableitung


def verlauf_generator(parent) -> Frame:
    """generiert frame mit verlauf
    :param parent: parent widget
    :type parent: tkinter widget
    :return: frame mit verlauf
    :rtype: Frame
    """
    frame = Frame(parent)
    listbox = Listbox(frame, width=20, height=100)
    listbox.pack(side=LEFT, fill=BOTH, expand=False)

    listbox.insert(END, get_verlauf(1))
    

    scrollbar = Scrollbar(frame)

    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)

    scrollbar.pack(side=RIGHT, fill=BOTH)

    return frame


def get_zahlen(inp: str) -> list:
    """ holt wichtige zahlen aus dem string
    :param inp: string mit allen zahlen
    :type inp: str
    :return: liste mit allen zahlen
    :rtype: list
    """
    # regex magie um alle zahlen zu finden
    dirty_terme = re.findall(r"[+-]?\d*x?\^?\d*", inp)

    # entfernt alle leeren strings
    terme = [t for t in dirty_terme if t != '']
    return terme


def basis_exponent_paare_holen(inp: str) -> list[tuple[float, float]]:
    input_str = array_von_leeren_strings_befreien(inp)
    terme = get_zahlen(input_str)
    return [get_term(t) for t in terme]


def open_main_window() -> None:
    """ Hauptfenster """

    root = Tk()

    menu = get_menu(root)
    root.config(menu=menu)
    root.title("Mathe-Funktionen-Rechner 2022/23")
    root.geometry("1000x800")

    verlauf_generator(root).pack(side=LEFT, fill=BOTH, expand=False)

    terme_eingeben_frame = Frame(root)
    Label(terme_eingeben_frame, text="hier Funktionsterm eingeben: ").pack(side=TOP, anchor=NW)

    f_entry = Entry(terme_eingeben_frame)
    f_entry.pack(side=TOP, anchor=NW)
    # labels & entries for bounds of x and y axis
    Label(terme_eingeben_frame, text="x von, bis: ").pack(side=TOP, anchor=NW)
    x_von_bis_entry = Entry(terme_eingeben_frame)
    x_von_bis_entry.pack(side=TOP, anchor=NW)
    Label(terme_eingeben_frame, text="y von, bis: ").pack(side=TOP, anchor=NW)
    y_von_bis_entry = Entry(terme_eingeben_frame)
    y_von_bis_entry.pack(side=TOP, anchor=NW)


    def _get_help() -> None:
        """ ruft das hilfefenster auf """
        _help = base_tk(size="800x500", name="Hilfe - Funktionen")
        Label(_help,
        text="In das Input feld die Funktion eingeben, die exponenten werden mit einem ^ notiert.\n\
                Also z.B.: 1x^3 + 2x^2 + 1x + 0\n\
                Wenn der erste term ein x vorne hat, muss eine 1 davor geschrieben werden!").pack()
        Button(_help, text="Ok", command=_help.destroy).pack()


    def funktion_berechnen() -> None:
        """ holt werte und berechnet die funktion """

        # holt input und bereinigt ihn
        basis_exponent_paare = basis_exponent_paare_holen(f_entry.get())

        # erstellt plot
        fig = plt.Figure(figsize=(10, 20), dpi=100)
        x_werte = np.arange(-100, 200, 0.2)
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
        def funktion(x_wert: float) -> float:
            """ berechnet die funktion """
            y_wert = 0
            for basis, exponent in basis_exponent_paare:
                y_wert += basis * (x_wert ** exponent)
            return y_wert

        ax.plot(x_werte, funktion(x_werte), label="linie")
        # setzt eine Legende in die obere rechte Ecke
        ax.legend(loc="upper right")

        canvas = FigureCanvasTkAgg(fig, master=terme_eingeben_frame)
        canvas.draw()

        def kurvendiskussion():
            pass


        kurvendiskussion_button = Button(terme_eingeben_frame,
                                         text="Kurvendiskussion",
                                         command=kurvendiskussion)
        kurvendiskussion_button.pack(side=TOP, anchor=NW)
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True)

    _b = Button(terme_eingeben_frame, text="Los gehts!", command=funktion_berechnen)
    Button(terme_eingeben_frame, text="?", command=_get_help).pack(side=TOP, anchor=NE)

    _b.pack(side=TOP, anchor=NW)

    terme_eingeben_frame.pack(side=LEFT, fill=BOTH, expand=True)


    root.mainloop()


# generiert main menu fuer das root win
def get_menu(root) -> Menu:
    """ generiert main menu für das root win """
    _menu = Menu(root, tearoff=0)
    funktionen_menu = Menu(_menu, tearoff=0)
    account_menu = Menu(_menu, tearoff=0)
    hilfe_menu = Menu(_menu, tearoff=0)

    funktionen_menu.add_command(label="Trigonometrische",
                                command=open_trigonometrische_window)
    funktionen_menu.add_command(label="Exponential",
                                command=open_exponential_window)
    # Differenzial Rechnen = Ableitungen, deshalb wir dies in dem anderen Fenster sein
    funktionen_menu.add_command(label="Integralrechnung",
                                command=open_integralrechnung_window)
    _menu.add_cascade(label="Funktionen", menu=funktionen_menu)

    account_menu.add_command(label="Logout",
                             command=root.destroy)
    _menu.add_cascade(label="Account", menu=account_menu)

    hilfe_menu.add_command(label="hilfe",
                                 command=open_hilfe_window)
    _menu.add_cascade(label="Hilfe", menu=hilfe_menu)
    hilfe_menu.add_command(label="über",
                                 command=open_ueber_window)
    return _menu


