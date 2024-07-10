from tkinter import *


App = Tk()

menu_ch = StringVar()
options = ['Red', 'Green', 'Black', 'white']
menu = OptionMenu(App, menu_ch, *options)
menu.pack()
menu_ch.set('white')

def show():
    msg = Label(App, text='                     ', background=menu_ch.get().lower())
    msg.pack()

B = Button(App, text='Show', command=show)
B.pack()

App.mainloop()