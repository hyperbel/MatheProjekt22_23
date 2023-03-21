"""
Main datei im Projekt, was für das öffnen der anderen Fenster verantwortlich ist.
"""
import sqlite3
from tkinter import Tk, Label, Entry, Button
from database import create_db
import windows as wins


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
            wins.open_main_window()
    except Exception as error:
        print(f"Login fehlgeschlagen: {error}")

    return True

def main():
    """ was soll ich hier überhaupt schreiben? """
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
                wins.open_main_window()

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
