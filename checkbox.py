from tkinter import *


APP = Tk()

check = StringVar()
chk = Checkbutton(APP, text='Checkbox', variable=check, onvalue='Yes', offvalue='No')
chk.deselect()
chk.pack()

def show():
    msg = Label(APP, text=check.get())
    msg.pack()

B = Button(APP, text='show', command=show)
B.pack()

APP.mainloop()