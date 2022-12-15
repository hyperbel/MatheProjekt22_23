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
            login_win.destroy()
            wins.open_main_window()

    def get_signup_win():
        signup_win = Tk()

        Label(signup_win, text="Username:").pack()
        name_entry = Entry(signup_win, width=20)
        name_entry.pack()

        Label(signup_win, text="Password:").pack()
        pass_entry = Entry(signup_win, show="*", width=20)
        pass_entry.pack()

        Label(signup_win, text="Confirm Password:").pack()
        confirm_entry = Entry(signup_win, show="*", width=20)
        confirm_entry.pack()

        def do_singup():
            signup_win.destroy()
            wins.open_main_window()

        Button(signup_win, text="Signup", command=do_singup)

        login_win.destroy()
        signup_win.mainloop()

    Button(login_win, text="Login", command=eval_user_and_pw).pack()
    Button(login_win, text="signup instead?", command=get_signup_win).pack()

    # utils.global_dict["login_win"] = login_win
    login_win.mainloop()


if __name__ == "__main__":
    # create_db()
    main()
