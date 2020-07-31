import tkinter
from tkinter import *
def name():
    a=e1.get()
    b=e2.get()
    c=a+" "+b
    print("Name : "+str(c))
    e3.insert(0,c)
master = Tk() 
Label(master, text='First Name').grid(row=0) 
Label(master, text='Last Name').grid(row=1)
Label(master, text='Name').grid(row=2)
e1 = Entry(master) 
e2 = Entry(master)
e3 = Entry(master)
e1.grid(row=0, column=1) 
e2.grid(row=1, column=1) 
e3.grid(row=2, column=1)
button=tkinter.Button(master, text='Ok', width=10, command=name).grid(row=3)
mainloop()