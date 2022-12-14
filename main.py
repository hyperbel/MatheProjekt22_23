# numpy, matplotlib, math, sympy, random, time, glob, queue, collections,
# threading, re , tk
from tkinter import Tk, Label, Entry, Button
from database import create_db
import windows as wins


def main():
    login_win = Tk()

    Label(login_win, text="Username:").pack()
    username_entry = Entry(login_win, width=20)
    username_entry.pack()

    Label(login_win, text="Password:").pack()
    password_entry = Entry(login_win, show="*", width=20)
    password_entry.pack()

    def eval_user_and_pw():
        username_entry.get()
        password_entry.get()
        if True:
            wins.open_main_window()
            login_win.destroy()

    def get_signup_win():
        signup_win = Tk()

        Label(signup_win, text="Username:")
        name_entry = Entry(signup_win, width=20)
        name_entry.pack()

        Label(signup_win, text="Password:")
        pass_entry = Entry(signup_win, show="*", width=20)
        pass_entry.pack()

        login_win.destroy()
        signup_win.mainloop()

    Button(login_win, text="Login", command=eval_user_and_pw).pack()
    Button(login_win, text="signup instead?", command=get_signup_win).pack()

    # utils.global_dict["login_win"] = login_win
    login_win.mainloop()


if __name__ == "__main__":
    # create_db()
    main()
