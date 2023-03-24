"""
Main datei im Projekt, was für das öffnen der anderen Fenster verantwortlich ist.
"""
import time
import sqlite3
from tkinter import Tk, Label, Entry, Button, PhotoImage, Canvas, NW
from database import create_db

def import_wins():
    global test_func
    import windows as wins
    test_func = wins.open_main_window

"""
def open_main_win():
    wrapper for opening the main window
    # creates loading window
    load = Tk()
    load.overrideredirect(1)
    load.geometry("100x100")
    load.eval('tk::PlaceWindow . center')

    # insert loading.gif into loading window
    img = PhotoImage(file="loading.gif")
    canvas = Canvas(load, width=100, height=100)
    canvas.pack()
    canvas.create_image(0, 0, anchor=NW, image=img)

    load.update()
    # as soon as this shit is imported, destroy loading screen
    load.destroy()
    # and last but not least, open the main window
    open_main_win()
    """


def callback(_input):
    """
    Validiert input
    """
    if _input == 0:
        print(_input + "if1")
        return False
    if _input == " ":
        print(_input + "elif")
        return False

    print(_input + "else")
    return True


def callback_signup(passwd1, passwd2):
    """
    Validiert input für signup
    """
    if passwd1 == passwd2:
        print(passwd1 + "if1")
        return True

    print(passwd1 + "else")
    return False

def eval_user_and_pw(username: str, password: str, win_to_destroy) -> bool:
    """ Validiert input für login
    :param username: Username
    :type username: str
    :param password: Passwort
    :type password: str
    :param win_to_destroy: Fenster das geschlossen werden soll
    :type win_to_destroy: Tk

    :return: True wenn erfolgreich
    :rtype: bool
    """
    try:
        # guards for empty inputs
        if username == " " :
            raise Exception("Username is empty")
        if username == 0:
            raise Exception("Username is empty")
        if password == " ":
            raise Exception("Password is empty")

        con = sqlite3.connect("mathe.db")
        cur = con.cursor()
        sql = f"SELECT * FROM user WHERE username = '{username}' AND passwort = '{password}';"
        userpw = cur.execute(sql).fetchall()
        con.commit()
        if not userpw == " ":
            win_to_destroy.destroy()
            test_func()
    except Exception as error:
        print(f"Login fehlgeschlagen: {error}")

    return True

def create_splash():
    splash = Tk()

    img = PhotoImage(file="bild3.png")
    canvas = Canvas(splash, width=700, height=300)
    canvas.pack()
    canvas.create_image(0, 0, anchor=NW, image=img)
    canvas.create_text(350, 150, text="Mathe-Funktionen-Rechner 2022/23", font=("Arial", 28),fill="blue")
    splash.overrideredirect(1)
    splash.geometry("700x300")
    Label(splash, text="Mathe-Funktionen-Rechner 2022/23", font=("Arial", 20)).pack()
    Label(splash, text="Thomas & Finn", font=("Arial", 15)).pack()

    splash.eval('tk::PlaceWindow . center')
    splash.update()
    import_wins()
    splash.destroy()


def main():
    """ was soll ich hier überhaupt schreiben? """

    create_splash()

    login_win = Tk()

    Label(login_win, text="Username:").pack()
    username_entry = Entry(login_win, width=20)
    username_entry.pack()

    Label(login_win, text="Password:").pack()
    password_entry = Entry(login_win, show="*", width=20)
    password_entry.pack()


    def get_signup_win():

        signup_win = Tk()

        Label(signup_win, text="Username:").pack()
        name_entry_siqnup = Entry(signup_win, width=20)
        name_entry_siqnup.pack()

        Label(signup_win, text="Password:").pack()
        pass_entry_signup = Entry(signup_win, show="*", width=20)
        pass_entry_signup.pack()

        Label(signup_win, text="Confirm Password:").pack()
        confirm_entry = Entry(signup_win, show="*", width=20)
        confirm_entry.pack()
        def do_singup():
            # guards for empty inputs
            if username_entry.get() == " ":
                raise Exception("Username is empty")
            if username_entry.get() == 0:
                raise Exception("Username is empty")
            if password_entry.get() == " ":
                raise Exception("Password is empty")

            if pass_entry_signup.get() == confirm_entry.get():
                con = sqlite3.connect("mathe.db")
                cur = con.cursor()
                sql = f"INSERT INTO user\
                        VALUES( \'{name_entry_siqnup.get()}\', \'{pass_entry_signup.get()}\');"
                cur.execute(sql)
                con.commit()
                signup_win.destroy()
                login_win.destroy()
                test_func()

        Button(signup_win, text="Signup", command=do_singup).pack()

        signup_win.mainloop()

    Button(login_win,
           text="Login",
           command=lambda: eval_user_and_pw(username=username_entry.get(),
                                            password=password_entry.get(),
                                            win_to_destroy=login_win)
           ).pack()
    Button(login_win, text="signup instead?", command=get_signup_win).pack()

    login_win.mainloop()


if __name__ == "__main__":
    try:
        create_db()
    except Exception:
        print("Datenbank gibt es schon")
    main()
