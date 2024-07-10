from tkinter import *
from random import choice, sample

""" Getting input from user using entry field widgets"""
#App settings

App = Tk()
# App.title('App')
App.title('Element Picker')
App.geometry('220x150')
#App['background'] = 'black'

inp = Entry(App, background='grey', foreground='black', relief='raised', borderwidth=3, width=25)
inp.grid(row=0, column=0, columnspan=2, padx=25, pady=5)

no_choice = IntVar()
sld = Scale(App, from_=1, to=5, variable=no_choice, orient='horizontal')
sld.grid(row=1, column=0, columnspan=2, padx=25, pady=5)

import re

def pick():
    var = inp.get().split(',')

    if no_choice.get() != 1:
       ele = sample(var, no_choice.get())
       lbl = ''
       for i in ele:
           lbl +=' '+ i
       chois = "Choice: "+ str(lbl)
    else:
        chois = "Choice: "+ str(choice(var))

    #CREATING DIFFERENT WINDOW
    OutWin = Toplevel()
    OutWin.title('Output')


    msg = Label(OutWin, text=chois, width=25)
    msg.grid(row=3,column=0,columnspan=2, padx=40, pady=5)

    if quitB['state'] == DISABLED:
        quitB['state'] = NORMAL


#Button widgets
B = Button(App, text='Choose', command=pick,  background='white', foreground='black', relief='groove', borderwidth=5)
B.grid(row=2, column=0, padx=25, pady=5)

quitB = Button(App, text='Cancel', command=App.quit, state=DISABLED,  background='red', foreground='white', borderwidth=5)
quitB.grid(row=2, column=1, padx=25, pady=5)




#main loop
App.mainloop()