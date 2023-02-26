# numpy, matplotlib, math, sympy, random, time, glob, queue, collections,
# threading, re , tk
from tkinter import Tk, Label, Entry, Button
from database import create_db
import windows as wins
import sqlite3


def callback(input):
    return True if input else False

def callback_signup(passwd1, passwd2):
    if passwd1 == passwd2:
        return True

    else:
        return False

def main():
    login_win = Tk()

    Label(login_win, text="Username:").pack()
    username_entry = Entry(login_win, width=20)
    username_entry.pack()

    Label(login_win, text="Password:").pack()
    password_entry = Entry(login_win, show="*", width=20)
    password_entry.pack()

    def eval_user_and_pw():
        try:
             if  username_entry.get() and password_entry.get():
                    con = sqlite3.connect("mathe.db")
                    cur = con.cursor()
                    uname = username_entry.get()
                    passw = password_entry.get()
                    sql = f"SELECT * FROM user WHERE username = '{uname}' AND passwort = '{passw}';"
                    userpw = cur.execute(sql).fetchall()
                    con.commit()
                    print("moin")
             
                    login_win.destroy()
                    wins.open_main_window()
        except Exception:
            print("Login fehlgeschlagen")

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

            if name_entry_siqnup.get() and confirm_entry.get()  and pass_entry_signup.get():
                if callback_signup(pass_entry_signup.pack(), confirm_entry.pack()):
                    # if pass_entry_signup.get() == confirm_entry.get():
                    con = sqlite3.connect("mathe.db")
                    cur = con.cursor()
                    sql = f"INSERT INTO user VALUES( \'{name_entry_siqnup.get()}\', \'{pass_entry_signup.get()}\');"
                    cur.execute(sql)
                    con.commit()
                    signup_win.destroy()
                    login_win.destroy()
                    wins.open_main_window()

        Button(signup_win, text="Signup", command=do_singup).pack()

        #login_win.destroy()
        signup_win.mainloop()

    Button(login_win, text="Login", command=eval_user_and_pw).pack()
    Button(login_win, text="signup instead?", command=get_signup_win).pack()

    login_win.mainloop()


if __name__ == "__main__":
    try:
        create_db()
    except Exception:
        print("Datenbank gibt es schon")
    main()
