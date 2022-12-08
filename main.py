# numpy, matplotlib, math, sympy, random, time, glob, queue, collections,
# threading, re , tk
from tkinter import Tk, Label, Entry, Button
import utils
from database import create_db

def main():
    login_win = Tk()

    Label(login_win, text="Username:").pack()
    username_entry = Entry(login_win, width=20)
    username_entry.pack()
    utils.global_dict["username_entry"] = username_entry

    Label(login_win, text="Password:").pack()
    password_entry = Entry(login_win, show="*", width=20)
    password_entry.pack()
    utils.global_dict["password_entry"] = password_entry

    Button(login_win, text="Login", command=utils.eval_user_and_pw).pack()

    utils.global_dict["login_win"] = login_win
    login_win.mainloop()


if __name__ == "__main__":
  #  create_db()
    main()
