from tkinter import Tk, Button

root = Tk()

test = Button(root, text="test")

def motion(ev):
    const_Y = root.winfo_height() / 2 # center of y axis
    x = root.winfo_width() - ev.x
    test.place(x=x, y=const_Y)


root.bind('<B1-Motion>', motion)
root.mainloop()
