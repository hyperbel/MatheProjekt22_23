from tkinter import Tk, Frame, Label, Entry, Button, TOP, LEFT, BOTH, NW, NE, Menu
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

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

class MainWindow(Tk):
    def __init__(self):
        super().__init__()
        self.title("Mathe Projekt 22/23")
        self.geometry("900x600")

        self.create_menu()
        self.config(menu=self.menu)

        self.selected_frame = None

    def select_ganzrational(self):
        self.selected_frame = Ganzrational(self)
        pass

    # generiert main menu fuer das root win
    def create_menu(self) -> None:
        """ generiert main menu für das root win """
        self.menu = Menu(self, tearoff=0)
        funktionen_menu = Menu(self.menu, tearoff=0)
        # account_menu = Menu(_menu, tearoff=0)
        # hilfe_menu = Menu(_menu, tearoff=0)

        funktionen_menu.add_command(label="Ganzrational", command=self.select_ganzrational)

        self.menu.add_cascade(label="Funktionen", menu=funktionen_menu)

        # funktionen_menu.add_command(label="Trigonometrische", command=open_trigonometrische_window)
        # funktionen_menu.add_command(label="Exponential", command=open_exponential_window)
        # # Differenzial Rechnen = Ableitungen, deshalb wir dies in dem anderen Fenster sein
        # funktionen_menu.add_command(label="Integralrechnung", command=open_integralrechnung_window)
        # _menu.add_cascade(label="Funktionen", menu=funktionen_menu)

        # account_menu.add_command(label="Logout", command=self.destroy)
        # _menu.add_cascade(label="Account", menu=account_menu)

        # hilfe_menu.add_command(label="hilfe", command=open_hilfe_window)
        #_menu.add_cascade(label="Hilfe", menu=hilfe_menu)
        # hilfe_menu.add_command(label="über", command=open_ueber_window)

class Ganzrational(Frame):
    def __init__(self, master):
        super().__init__(master)
        Label(self, text="hier Funktionsterm eingeben: ").pack(side=TOP, anchor=NW)

        self.f_entry = Entry(self)
        self.f_entry.pack(side=TOP, anchor=NW)
        # labels & entries for bounds of x and y axis
        Label(self, text="x von, bis: ").pack(side=TOP, anchor=NW)
        x_von_bis_entry = Entry(self)
        x_von_bis_entry.pack(side=TOP, anchor=NW)
        Label(self, text="y von, bis: ").pack(side=TOP, anchor=NW)
        y_von_bis_entry = Entry(self)
        y_von_bis_entry.pack(side=TOP, anchor=NW)

        _b = Button(self, text="Los gehts!", command=self.funktion_berechnen)
        Button(self, text="?", command=self._get_help).pack(side=TOP, anchor=NE)

        _b.pack(side=TOP, anchor=NW)

        self.pack(side=LEFT, fill=BOTH, expand=True)

    def _get_help(self) -> None:
        """ ruft das hilfefenster auf """
        _help = base_tk(size="800x500", name="Hilfe - Funktionen")
        Label(_help,
        text="In das Input feld die Funktion eingeben, die exponenten werden mit einem ^ notiert.\n\
                Also z.B.: 1x^3 + 2x^2 + 1x + 0\n\
                Wenn der erste term ein x vorne hat, muss eine 1 davor geschrieben werden!").pack()
        Button(_help, text="Ok", command=_help.destroy).pack()

    # berechnet das richtig dismal lol. ich bin so dumm
    def funktion(self, x_wert: float) -> float:
        """ berechnet die funktion """
        y_wert = 0
        for basis, exponent in self.basis_exponent_paare:
            y_wert += basis * (x_wert ** exponent)
        return y_wert


    def funktion_berechnen(self) -> None:
        """ holt werte und berechnet die funktion """

        # holt input und bereinigt ihn
        self.basis_exponent_paare = basis_exponent_paare_holen(self.f_entry.get())

        # erstellt plot
        fig = plt.Figure(figsize=(10, 20), dpi=100)
        x_werte = np.arange(-100, 200, 0.2)
        self.ax = fig.add_subplot()
        self.ax.set_xlabel("x")
        self.ax.set_ylabel("y")
        self.ax.set_title("Funktionsgraph")
        x_von, x_bis = von_bis(x_von_bis_entry.get())
        self.ax.set_xlim(x_von, x_bis)
        y_von, y_bis = von_bis(y_von_bis_entry.get())
        self.ax.set_ylim(y_von, y_bis)
        self.ax.grid()
        self.ax.spines.left.set_position('zero')
        self.ax.spines.right.set_color('none')
        self.ax.spines.bottom.set_position('zero')
        self.ax.spines.top.set_color('none')
        self.ax.yaxis.set_ticks_position('left')
        self.ax.xaxis.set_ticks_position('bottom')

        self.ax.scatter(0, 0, color="purple", label="Nullpunkt")



        self.ax.plot(x_werte, self.funktion(x_werte), label="linie")
        # setzt eine Legende in die obere rechte Ecke
        self.ax.legend(loc="upper right")

        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()

        def kurvendiskussion():
            pass


        kurvendiskussion_button = Button(self,
                                         text="Kurvendiskussion",
                                         command=kurvendiskussion)
        kurvendiskussion_button.pack(side=TOP, anchor=NW)
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True)

if __name__ == "__main__":
    MainWindow().mainloop()
