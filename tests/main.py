from tkinter import Tk, Button

root = Tk()

test = Button(root, text="test")

def motion(ev):
    x, y = ev.x, ev.y
    test.place(x=x, y=y)


root.bind('<B1-Motion>', motion)
root.mainloop()
