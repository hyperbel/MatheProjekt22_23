from account import LoginWindow
from verlauf import Verlauf
import sqlite3
from tkinter import Tk, LEFT, BOTH, Menu, RIGHT, Frame, Label, Canvas, PhotoImage, NW, Button, Label, messagebox
from mainwindowbase import BaseWindow


def import_funktionen():
    """ importiert funktionen.py und macht es als globale variable f verfügbar
        das mache ich, damit das splash ding auch eine funktion hat ausser schön auszusehen
    """
    global f
    __all__ = ['funktionen']
    import funktionen as _f
    f = _f

class WelcomeFrame(Frame):
    def __inít__(self, master):
        super().__init__()

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.verlauf_hilfe = Label(self, text="Links ist der Ferlauf zu sehen. Dort werden Funktionen eingefügt, wenn Sie das Graph sehen!")
        self.terme_eingeben_hilfe = Label(self, text="Im Terme-Eingeben-Teil können sie eine Ganzrationale Funktion eingeben!")
        self.exponential_hilfe = Label(self, text="Hier können Sie sehen, wie eine exponentielle Funktion aussieht!")
        self.trigonometrische_hilfe = Label(self, text="bitte noch einfügen") # TODO
        self.integral_hilfe = Label(self, text="bitte noch einfügen") #TODO

        self.show_labels()

    def show_labels():
        self.verlauf_hilfe.grid(row=0, column=0)
        self.terme_eingeben_hilfe.grid(row=1, column=0)
        self.exponential_hilfe.grid(row=2, column=0)
        self.trigonometrische_hilfe.grid(row=3, column=0)
        self.integral_hilfe.grid(row=4, column=0)


class MainWindow(BaseWindow):
    def __init__(self):
        super().__init__()

        self.create_menu()
        self.config(menu=self.menu)

        # set column height
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.verlauf = Verlauf(self, self)
        self.verlauf.grid(row=0, column=0, sticky="nsew")

        self.selected_frame = WelcomeFrame(self)

        self.selected_frame.config(height=self.winfo_height())
        self.selected_frame.grid(row=0, column=1, sticky="nsew")


    def get_verlauf(self) -> Verlauf:
        return self.verlauf

    def hide_all_frames(self):
        if self.selected_frame is not None:
            self.selected_frame.grid_forget()

    def select(self, frame: Frame) -> None:
        self.hide_all_frames()
        self.selected_frame = frame
        self.selected_frame.config(height=self.winfo_height())
        self.selected_frame.grid(row=0, column=1, sticky="nsew")

    def select_by_name(self, frame: str, funktion: str) -> None:
        self.hide_all_frames()

        match frame:
            case "term_eingeben":
                self.selected_frame = f.term_eingeben.TermEingeben(self, self, funktion)
            case "exponential":
                self.selected_frame = f.exponential.Exponential(self,funktion)
            case "trigonometrische":
                self.selected_frame = f.trigonometrische.Trigonometrische(self, funktion)
            case "integralrechnung":
                self.selected_frame = f.integralrechnung.Integralrechnung(self, funktion)
            case _:
                raise ValueError("Frame not found")

        self.selected_frame.config(height=self.winfo_height())
        self.selected_frame.grid(row=0, column=1, sticky="nsew")

    def logout(self):
            """beendet das Programm"""
            if messagebox.askokcancel("Quit", "Wirklich beenden?"):
                self.destroy()
    
    def loeschen(self):
        """löscht einen Account"""
        if messagebox.askokcancel("Löschen", "Willst du wirklich deinen Account und alle Funktionen LÖSCHEN?"):
            con = sqlite3.connect("mathe.db")
            cur = con.cursor()
            #cur.execute("DELETE FROM user;")
            #con.commit()
            _ = messagebox.showwarning(title="In entwicklung", message="dieses Feature ist noch in der Entwicklung, und wird es nicht in Version 1 schaffen")

    # generiert main menu fuer das root win
    def create_menu(self) -> None:

        """ generiert main menu für das root win """
        self.menu = Menu(self, tearoff=0)
        funktionen_menu = Menu(self.menu, tearoff=0)
        account_menu = Menu(self.menu, tearoff=0)
        # account_menu = Menu(_menu, tearoff=0)
        # hilfe_menu = Menu(_menu, tearoff=0)

        funktionen_menu.add_command(label="Term eingeben", command=lambda: self.select(f.term_eingeben.TermEingeben(self, self)))

        funktionen_menu.add_command(label="Exponential", command=lambda: self.select(f.exponential.Exponential(self)))

        funktionen_menu.add_command(label="Trigonometrische", command=lambda: self.select(f.trigonometrische.Trigonometrische(self)))

        funktionen_menu.add_command(label="Integralrechnung", command=lambda: self.select(f.integralrechnung.Integralrechnung(self)))


        self.menu.add_cascade(label="Funktionen", menu=funktionen_menu)

        account_menu.add_command(label="Logout", command=self.logout)
        account_menu.add_command(label="Löschen", command=self.loeschen)
        self.menu.add_cascade(label="Account", menu=account_menu)

class Splash(Tk):
    def __init__(self):
        super().__init__()
        img = PhotoImage(file="bild3.png")
        canvas = Canvas(self, width=700, height=300)
        canvas.pack()
        canvas.create_image(0, 0, anchor=NW, image=img)
        canvas.create_text(350, 150, text="Mathe-Funktionen-Rechner 2022/23", font=("Arial", 28),fill="blue")
        self.overrideredirect(True)
        self.geometry("700x300")
        Label(self, text="Mathe-Funktionen-Rechner 2022/23", font=("Arial", 20)).pack()
        Label(self, text="Thomas & Finn", font=("Arial", 15)).pack()

        self.eval('tk::PlaceWindow . center')
        self.update()
        
        import_funktionen()

        self.destroy()


def start():
    Splash().mainloop()
    LoginWindow(MainWindow).mainloop()

if __name__ == "__main__":
    Splash().mainloop()
    LoginWindow(MainWindow).mainloop()
