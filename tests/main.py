from tkinter import Tk, Button

class MainWin(Tk):
    def __init__(self):
        super().__init__()

        self.test = Button(self, text="test")
        self.last_x = self.winfo_width() 
        self.bind('<B1-Motion>', self.motion)


    def motion(self, ev):
        const_Y = self.winfo_height() / 2 # center of y axis
        x = self.last_x + ev.x
        self.test.place(x=x, y=const_Y)
        last_x = ev.x

win = MainWin()
win.mainloop()
