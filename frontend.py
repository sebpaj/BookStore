'''
A program that stores this book information:
Title, Autor
Year, ISBN

User can:
View all records
Search an entry
Add entry
Update entry
Delete
close
'''
from tkinter import *

window = Tk()

l1 = Label(window,text="Title")
l1.grid(row=0,column=0)

l2 = Label(window,text="Author")
l2.grid(row=0,column=2)

l3 = Label(window,text="Year")
l3.grid(row=1,column=0)

l3 = Label(window,text="ISBN")
l3.grid(row=1,column=2)

titleText = StringVar()
e1=Entry(window,textvariable=titleText)
e1.grid(row=0,column=1)

authorText = StringVar()
e1=Entry(window,textvariable=authorText)
e1.grid(row=0,column=3)

yearText = StringVar()
e1=Entry(window,textvariable=yearText)
e1.grid(row=1,column=1)

ISBNText = StringVar()
e1=Entry(window,textvariable=ISBNText)
e1.grid(row=1,column=3)

window.mainloop()
