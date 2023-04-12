""" Account management sachen"""
import sqlite3
from tkinter import Tk, Frame, Button, Label, Entry, messagebox

class LoginWindow(Tk):
    """ Login fenster nach dem splash screen"""
    def __init__(self, _next):
        super().__init__()
        self.title("Login")
        self.next = _next
        self.geometry("200x160")

        self.create_widgets()

    def create_widgets(self) -> None:
        """ erstellt widgets"""
        self.login_frame = LoginFrame(master=self, parent=self)
        self.login_frame.pack()

    def proceed(self) -> None:
        """ macht weiter wenn der login erfolgreich war"""
        self.destroy()
        self.next().mainloop()

    def open_signup(self) -> None:
        """ öffnet das signup fenster"""
        self.login_frame.pack_forget()
        SignUpFrame(master=self, parent=self).pack()

class LoginFrame(Frame):
    """ frame für login logik"""
    def __init__(self, master, parent: LoginWindow):
        super().__init__(master)
        self.master = master
        self.parent = parent
        self.create_widgets()

        self.connection = sqlite3.connect("mathe.db")
        self.cursor = self.connection.cursor()

    def create_widgets(self):
        """ holt widgets für die user experience"""
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
        """ loggt den user ein"""
        if self.eval_logindata():
            self.parent.proceed()
        else:
            self.password_entry.delete(0, "end")
            _ = messagebox.showwarning(title="Login Fehlgeschlagen", message="Bitte überprüfe die Anmelde Daten, solltest du noch kein Account haben, erstelle einen")

    def eval_logindata(self) -> bool:
        """ evaluiert Logindaten
        :return: Ob die daten richtig sind
        :rtype: bool
        """
        uname = self.username_entry.get()
        query = f"SELECT * FROM user WHERE username = ?"
        self.cursor.execute(query, (uname,))
        result = self.cursor.fetchall()
        correct = False
        try:
            if len(result) == 0:
                pass
            if result[0][0] == uname:
                if result[0][1] == self.password_entry.get():
                    correct = True
            return correct
        except:
              _ = messagebox.showwarning(title="Login Fehlgeschlagen",
                                         message="Bitte überprüfe die Anmelde Daten, solltest du noch kein Account haben, erstelle einen")
              return False
   

class SignUpFrame(Frame):
    """ frame für signup logik"""
    def __init__(self, master, parent: LoginWindow):
        super().__init__(master)
        self.master = master
        self.parent = parent
        self.create_widgets()

        self.connection = sqlite3.connect("mathe.db")
        self.cursor = self.connection.cursor()

    def create_widgets(self):
        """ holt widgets für die user experience"""
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
        """ evaluiert signup daten"""
        uname = self.username_entry.get()
        passw = self.password_entry.get()
        confi = self.confirm_entry.get()

        if passw != confi:
            pass

        query = f"SELECT * FROM user WHERE username = ?"
        self.cursor.execute(query, (uname,))
        result = self.cursor.fetchall()

        if len(result) != 0:
             _ = messagebox.showwarning(title="Gibt es schon", message="Dieser Benutzer ist bereits da, solltest du das sein logge dich einfach an")
            #raise NotImplementedError("Username already taken")

        query = f"INSERT INTO user VALUES (?, ?)"
        self.cursor.execute(query, (uname, passw))
        self.connection.commit()

    def signup(self):
        """ erstellt einen account"""
        self.eval_signupdata()
        self.parent.proceed()
