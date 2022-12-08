from tkinter import Tk, Menu
import windows as wins

# dict fuer alle globalen werte
global_dict = {}


# basic window config
def base_Tk(size="900x600", name=""):
    win = Tk()
    win.geometry(size)
    win.title(name)
    return win


def eval_user_and_pw():
    user_name = global_dict["username_entry"].get()
    user_pass = global_dict["password_entry"].get()
    print(user_name)
    print(user_pass)
    if True:
        wins.open_main_window()
        global_dict["login_win"].destroy()


# setzt globale werte, fuer mehr info schau in globals.py
def global_set_user_data(user_name, user_password):
    global_dict["user_name"] = user_name
    global_dict["user_password"] = user_password


# generiert main menu fuer das root win
def get_menu(root):
    _menu = Menu(root, tearoff=0)
    funktionen_menu = Menu(_menu, tearoff=0)
    account_menu = Menu(_menu, tearoff=0)
    hilfe_menu = Menu(_menu, tearoff=0)

    funktionen_menu.add_command(label="Linear",
                                command=wins.open_linear_window)
    funktionen_menu.add_command(label="Quadratisch",
                                command=wins.open_quadratisch_window)
    funktionen_menu.add_command(label="Ganzrationale Funktionen",
                                command=wins.open_Ganzrazio_window)
    funktionen_menu.add_command(label="Trigonometrische",
                                command=wins.open_Trigonometr_window)
    funktionen_menu.add_command(label="Exponential",
                                command=wins.open_Exponential_window)
    funktionen_menu.add_command(label="Differenzial",
                                command=wins.open_defferenz_window)
    funktionen_menu.add_command(label="Kurvendiskusion",
                                command=wins.open_Kurvendiskussion_window)
    funktionen_menu.add_command(label="Integralrechnung",
                                command=wins.open_Integralrechnung_window)
    _menu.add_cascade(label="Funktionen", menu=funktionen_menu)

    account_menu.add_command(label="Logout",
                             command=wins.open_linear_window)
    account_menu.add_command(label="Verlauf",
                             command=wins.open_verlauf_window)
    _menu.add_cascade(label="Account", menu=account_menu)

    hilfe_menu.add_command(label="hilfe",
                                 command=wins.open_hilfe_window)
    _menu.add_cascade(label="Hilfe", menu=hilfe_menu)
    hilfe_menu.add_command(label="über",
                                 command=wins.open_ueber_window)

    return _menu
