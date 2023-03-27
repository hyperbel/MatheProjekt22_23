from tkinter import Tk, LEFT, BOTH, Menu, RIGHT
import funktionen as f
from verlauf import Verlauf


class MainWindow(Tk):
    def __init__(self):
        super().__init__()
        self.title("Mathe Projekt 22/23")
        self.geometry("900x600")

        self.create_menu()
        self.config(menu=self.menu, bg="red")

        self.verlauf = Verlauf(self)
        self.verlauf.pack(side=LEFT, fill=BOTH, expand=False)

        self.selected_frame = None

    def hide_all_frames(self):
        if self.selected_frame is not None:
            self.selected_frame.pack_forget()

    def select_ganzrational(self):
        self.hide_all_frames()
        self.selected_frame = f.Ganzrational(self)
        self.selected_frame.pack(side=RIGHT, fill=BOTH, expand=True)

    def select_exponential(self):
        self.hide_all_frames()
        self.selected_frame = f.Exponential(self)
        self.selected_frame.pack(side=RIGHT, fill=BOTH, expand=True)

    # generiert main menu fuer das root win
    def create_menu(self) -> None:
        """ generiert main menu für das root win """
        self.menu = Menu(self, tearoff=0)
        funktionen_menu = Menu(self.menu, tearoff=0)
        # account_menu = Menu(_menu, tearoff=0)
        # hilfe_menu = Menu(_menu, tearoff=0)

        funktionen_menu.add_command(label="Ganzrational", command=self.select_ganzrational)

        funktionen_menu.add_command(label="Exponential", command=self.select_exponential)


        self.menu.add_cascade(label="Funktionen", menu=funktionen_menu)

        # funktionen_menu.add_command(label="Trigonometrische", command=open_trigonometrische_window)
        # # Differenzial Rechnen = Ableitungen, deshalb wir dies in dem anderen Fenster sein
        # funktionen_menu.add_command(label="Integralrechnung", command=open_integralrechnung_window)
        # _menu.add_cascade(label="Funktionen", menu=funktionen_menu)

        # account_menu.add_command(label="Logout", command=self.destroy)
        # _menu.add_cascade(label="Account", menu=account_menu)

        # hilfe_menu.add_command(label="hilfe", command=open_hilfe_window)
        #_menu.add_cascade(label="Hilfe", menu=hilfe_menu)
        # hilfe_menu.add_command(label="über", command=open_ueber_window)


if __name__ == "__main__":
    MainWindow().mainloop()
