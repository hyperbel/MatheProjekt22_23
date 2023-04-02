import sqlite3
from tkinter import Tk, Frame, Button, Label, Entry

class LoginWindow(Tk):
    def __init__(self, _next):
        super().__init__()
        self.title("Login")
        self.next = _next
        self.geometry("300x200")

        self.create_widgets()

    def create_widgets(self) -> None:
        self.login_frame = LoginFrame(master=self, parent=self)
        self.login_frame.pack()

    def proceed(self) -> None:
        self.destroy()
        self.next().mainloop()

    def open_signup(self) -> None:
        self.login_frame.pack_forget()
        SignUpFrame(master=self, parent=self).pack()

class LoginFrame(Frame):
    def __init__(self, master, parent: LoginWindow):
        super().__init__(master)
        self.master = master
        self.parent = parent
        self.create_widgets()

        self.connection = sqlite3.connect("mathe.db")
        self.cursor = self.connection.cursor()

    def create_widgets(self):
        self.username_label = Label(self, text="Username")
        self.username_label.pack()
        self.username_entry = Entry(self)
        self.username_entry.pack()
        self.password_label = Label(self, text="Password")
        self.password_label.pack()
        self.password_entry = Entry(self, show="*")
        self.password_entry.pack()
        self.login_button = Button(self, text="Login", command=self.login)
        self.login_button.pack()
        self.signup_button = Button(self, text="Sign Up", command=self.parent.open_signup)
        self.signup_button.pack()


    def login(self) -> None:
        if self.eval_logindata():
            self.parent.proceed()
        else:
            self.password_entry.delete(0, "end")

    def eval_logindata(self) -> bool:
        uname = self.username_entry.get()
        query = f"SELECT * FROM user WHERE username = ?"
        self.cursor.execute(query, (uname,))
        result = self.cursor.fetchall()
        correct = False
        if len(result) == 0:
            pass
        if result[0][0] == uname:
            if result[0][1] == self.password_entry.get():
                correct = True
        return correct


class SignUpFrame(Frame):
    def __init__(self, master, parent: LoginWindow):
        super().__init__(master)
        self.master = master
        self.parent = parent
        self.create_widgets()

        self.connection = sqlite3.connect("mathe.db")
        self.cursor = self.connection.cursor()

    def create_widgets(self):
        self.username_label = Label(self, text="Username")
        self.username_label.pack()
        self.username_entry = Entry(self)
        self.username_entry.pack()
        self.password_label = Label(self, text="Password")
        self.password_label.pack()
        self.password_entry = Entry(self, show="*")
        self.password_entry.pack()
        self.confirm_label = Label(self, text="Password")
        self.confirm_label.pack()
        self.confirm_entry = Entry(self, show="*")
        self.confirm_entry.pack()
        self.signup_button = Button(self, text="Create Account", command=self.signup)
        self.signup_button.pack()

    def eval_signupdata(self) -> None:
        uname = self.username_entry.get()
        passw = self.password_entry.get()
        confi = self.confirm_entry.get()


        if passw != confi:
            pass

        query = f"SELECT * FROM user WHERE username = ?"
        self.cursor.execute(query, (uname,))
        result = self.cursor.fetchall()

        if len(result) != 0:
            raise NotImplementedError("Username already taken")

        query = f"INSERT INTO user VALUES (?, ?)"
        self.cursor.execute(query, (uname, passw))
        self.connection.commit()

    def signup(self):
        self.eval_signupdata()
        self.parent.proceed()
