from tkinter import Tk, Menu
import windows as wins

# dict fuer alle globalen werte
global_dict = {}


# basic window config
def base_Tk(size="200x200", name=""):
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
    _menu.add_cascade(label="Funktionen", menu=funktionen_menu)

    account_menu.add_command(label="Login/logout",
                             command=wins.open_linear_window)
    account_menu.add_command(label="Verlauf",
                             command=wins.open_linear_window)
    _menu.add_cascade(label="Account", menu=account_menu)

    hilfe_menu.add_command(label="hilfe",
                                 command=wins.open_linear_window)
    _menu.add_cascade(label="Hilfe", menu=hilfe_menu)
    hilfe_menu.add_command(label="über",
                                 command=wins.open_linear_window)

    return _menu
