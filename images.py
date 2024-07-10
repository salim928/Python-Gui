from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog

App = Tk()
App.iconbitmap(r"ye.ico")
App.title('Fameye PLayer')

#opening the image to a normal image variable
#img = ImageTk.PhotoImage(Image.open(r"C:\Users\LAPTOP\Desktop\GUI\Gui-learning\imgs\ye.jpg"))

#converting to a ImageTk to fit in our Tk APP
#lbl = Label(App, image=img)
#lbl.pack()

"""Creating a dialog box.
   The file dailog craetes a dialog box that Asks for filenames'initialdir', 
   And then the title of the dailog box, 
   And the the file type it should contain"""
def img_select():
    global img

    App.fname = filedialog.askopenfilename(initialdir='imgs', title='Selet an image', filetypes=(
        ('PNG Images','*.png'),('ICON Files','*.ico'),('All Files','*.*')
    ))
    B.destroy()  #destroy the button after viewing the image

    #open image once clicked!
    img = ImageTk.PhotoImage(Image.open(App.fname))
    lbl = Label(App, image=img)
    lbl.pack()

#function


#button
B = Button(App, text='View', command=img_select)
B.pack()

App.mainloop()