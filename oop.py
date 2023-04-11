from account import LoginWindow
from verlauf import Verlauf
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



class MainWindow(BaseWindow):
    def __init__(self):
        super().__init__()
        self.title("Mathe Projekt 22/23")
        self.minsize(1200, 850)
        self.maxsize(1200, 850)

        self.create_menu()
        self.config(menu=self.menu)

        # set column height
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.verlauf = Verlauf(self, self)
        self.verlauf.grid(row=0, column=0, sticky="nsew")

        self.selected_frame = None

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

    def select_by_name(self, frame: str) -> None:
        self.hide_all_frames()

        match frame:
            case "term_eingeben":
                self.selected_frame = f.term_eingeben.TermEingeben(self, self)
            case "exponential":
                self.selected_frame = f.exponential.Exponential(self)
            case "trigonometrische":
                self.selected_frame = f.trigonometrische.Trigonometrische(self)
            case "integralrechnung":
                self.selected_frame = f.integralrechnung.Integralrechnung(self)
            case _:
                raise ValueError("Frame not found")

        self.selected_frame.config(height=self.winfo_height())
        self.selected_frame.grid(row=0, column=1, sticky="nsew")

    def logout(self):
            """beendet das Programm"""
            if messagebox.askokcancel("Quit", "Wirklich beenden?"):
                self.destroy()

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
        self.menu.add_cascade(label="Account", menu=account_menu)

        

        # funktionen_menu.add_command(label="Trigonometrische", command=open_trigonometrische_window)
        # # Differenzial Rechnen = Ableitungen, deshalb wir dies in dem anderen Fenster sein
        # funktionen_menu.add_command(label="Integralrechnung", command=open_integralrechnung_window)
        # _menu.add_cascade(label="Funktionen", menu=funktionen_menu)

        # account_menu.add_command(label="Logout", command=self.destroy)
        # _menu.add_cascade(label="Account", menu=account_menu)

        # hilfe_menu.add_command(label="hilfe", command=open_hilfe_window)
        #_menu.add_cascade(label="Hilfe", menu=hilfe_menu)
        # hilfe_menu.add_command(label="über", command=open_ueber_window)

class WelcomeWizard:
    def __init__(self, master):
        self.master = master
        master.title("Willkommen")

        self.pages = []
        self.current_page = 0

        page1 = Frame(master)
        label1 = Label(page1, text="Willkommen beim Mathefunktionsrechner!")
        label1.pack()
        self.pages.append(page1)

        page2 = Frame(master)
        label2 = Label(page2, text="Diese Software kann dir mathematische Funktionen berechnen und erklären.")
        label2.pack()
        self.pages.append(page2)

        page3 = Frame(master)
        label3 = Label(page3, text="Wenn du hilfe brauchst klicke einfach auf das ? im Fenster")
        label3.pack(side="left")
        self.finish_button = Button(page3, text="Finish", command=self.finish)
        self.finish_button.pack(side="left")
        self.pages.append(page3)

        button_frame = Frame(master)
        self.back_button = Button(button_frame, text="Back", command=self.back)
        self.back_button.pack(side="left")
        self.next_button = Button(button_frame, text="Next", command=self.next)
        self.next_button.pack(side="left")

        self.show_current_page()
        button_frame.pack()

    def show_current_page(self):
        self.pages[self.current_page].pack()
        if self.current_page == 0:
            self.next_button.pack()
        elif self.current_page == len(self.pages) - 1:
            self.back_button.pack()
            self.finish_button.pack(side="left")
            self.next_button.pack_forget()
        else:
            self.back_button.pack()
            self.next_button.pack()

    def hide_current_page(self):
        self.pages[self.current_page].pack_forget()

    def next(self):
        self.hide_current_page()
        self.current_page += 1
        self.show_current_page()

    def back(self):
        self.hide_current_page()
        self.current_page -= 1
        self.show_current_page()

    def finish(self):
        self.master.destroy()


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
