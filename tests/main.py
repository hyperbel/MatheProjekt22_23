from tkinter import Tk, Button

class MainWin(Tk):
    def __init__(self):
        super().__init__()

        self.test = Button(self, text="test")
        self.last_y = self.winfo_width() 
        self.bind('<B1-Motion>', self.motion)


    def motion(self, ev):
        const_X = self.winfo_width() / 2 # center of x axis
        y = self.last_y + ev.y
        self.test.place(x=const_X, y=self.last_y)
        self.last_y += ev.y


win = MainWin()
win.mainloop()
