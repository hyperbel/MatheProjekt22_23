from tkinter import Tk

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
    return True


# setzt globale werte, fuer mehr info schau in globals.py
def global_set_user_data(user_name, user_password):
    global_dict["user_name"] = user_name
    global_dict["user_password"] = user_password
