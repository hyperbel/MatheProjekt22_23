from tkinter import Tk

# dict fuer alle globalen werte
global_dict = {}


# setzt globale werte, fuer mehr info schau in globals.py
def global_set_user_data(user_name, user_password):
    global_dict["user_name"] = user_name
    global_dict["user_password"] = user_password


def entry_is_float(inp):
    import re    # only need regex here
    # magic regex for checking if input is float type
    if type(inp) == float:
        return True
    elif type(inp) != str:
        print(type(inp))
    res = re.match(r"(\+|\-)?\d+(,\d+)?$", inp)
    return res is not None
