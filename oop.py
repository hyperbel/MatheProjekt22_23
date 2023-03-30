import time
from tkinter import Tk, LEFT, BOTH, Menu, RIGHT, Frame, Label, Canvas, PhotoImage, NW, Button

import funktionen as f
from verlauf import Verlauf


class MainWindow(Tk):
    def __init__(self):
        super().__init__()
        self.title("Mathe Projekt 22/23")
        self.geometry("900x600")

        self.create_menu()
        self.config(menu=self.menu)

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

    def select_trigonometrische(self):
        self.hide_all_frames()
        self.selected_frame = f.Trigonometrische(self)
        self.selected_frame.pack(side=RIGHT, fill=BOTH, expand=True)

    def select_integralrechnung(self):
        self.hide_all_frames()
        self.selected_frame = f.Integralrechnung(self)
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

        funktionen_menu.add_command(label="Trigonometrische", command=self.select_trigonometrische)

        funktionen_menu.add_command(label="Integralrechnung", command=self.select_integralrechnung)


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
    def __init__(self, duration_s: int = 2):
        super().__init__()
        img = PhotoImage(file="bild3.png")
        canvas = Canvas(self, width=700, height=300)
        canvas.pack()
        canvas.create_image(0, 0, anchor=NW, image=img)
        canvas.create_text(350, 150, text="Mathe-Funktionen-Rechner 2022/23", font=("Arial", 28),fill="blue")
        self.overrideredirect(1)
        self.geometry("700x300")
        Label(self, text="Mathe-Funktionen-Rechner 2022/23", font=("Arial", 20)).pack()
        Label(self, text="Thomas & Finn", font=("Arial", 15)).pack()

        self.eval('tk::PlaceWindow . center')
        self.update()
        
        time.sleep(duration_s)
        self.destroy()



if __name__ == "__main__":
    Splash(duration_s=3).mainloop()
    MainWindow().mainloop()
