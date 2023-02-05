""" This is the main file of the project. """
from tkinter import Tk, Button, Label, Entry
import sqlite3
# import oop_windows as wins


def callback(input_str):
    """ callback used to check if the user has entered a username and password. """
    if input_str:
        print(input_str + "if1")
        return True

    print(input_str + "else")
    return False


def callback_signup(passwd1, passwd2):
    """ callback used when user signs up. """
    if passwd1 == passwd2:
        print("if1")
        return True

    print("else")
    return False


def main():
    """ entry point of the program. """
    login_win = Tk()

    Label(login_win, text="Username:").pack()
    username_entry = Entry(login_win, width=20)
    username_entry.pack()

    Label(login_win, text="Password:").pack()
    password_entry = Entry(login_win, show="*", width=20)
    password_entry.pack()

    def eval_user_and_pw():
        try:
            if username_entry.get() or username_entry.get() and password_entry.get():
                con = sqlite3.connect("mathe.db")
                cur = con.cursor()
                uname = username_entry.get()
                passw = password_entry.get()
                sql = f"SELECT * FROM user WHERE username = '{uname}' AND passwort = '{passw}';"
                userpw = cur.execute(sql).fetchall()
                con.commit()
                if not userpw == " ":
                    login_win.destroy()
                    # wins.open_main_window()
        except sqlite3.Error as exception_e:
            print("Login fehlgeschlagen: " + str(exception_e))

    def get_signup_win():
        """ executes when user wants to sign up. """

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

            if username_entry.get() or username_entry.get() and password_entry.get():
                if callback_signup(pass_entry_signup.pack(),
                                   confirm_entry.pack()):
                    con = sqlite3.connect("mathe.db")
                    cur = con.cursor()
                    sql = f"""INSERT INTO user
                              VALUES( \'{name_entry_siqnup.get()}\',
                                      \'{pass_entry_signup.get()}\');"""
                    cur.execute(sql)
                    con.commit()
                    signup_win.destroy()
                    login_win.destroy()
                    # wins.open_main_window()

        Button(signup_win, text="Signup", command=do_singup).pack()

        # login_win.destroy()
        signup_win.mainloop()

    Button(login_win, text="Login", command=eval_user_and_pw).pack()
    Button(login_win, text="signup instead?", command=get_signup_win).pack()

    login_win.mainloop()


# call main function
if __name__ == "__main__":
    main()
