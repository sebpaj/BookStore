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
e2=Entry(window,textvariable=authorText)
e2.grid(row=0,column=3)

yearText = StringVar()
e3=Entry(window,textvariable=yearText)
e3.grid(row=1,column=1)

ISBNText = StringVar()
e4=Entry(window,textvariable=ISBNText)
e4.grid(row=1,column=3)

list1 = Listbox(window,height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

b1 = Button(window,text="View all", width=12)
b1.grid(row=2,column=3)

b2 = Button(window, text = "Search entry", width=12)
b2.grid(row=3,column=3)

b3 = Button(window, text="Add entry", width=12)
b3.grid(row=4,column=3)

b4 = Button(window, text="Update selected", width=12)
b4.grid(row=5,column=3)

b5 = Button(window, text="Delete selected", width=12)
b5.grid(row=6,column=3)

b6 = Button(window, text ="Close", width=12)
b6.grid(row=7,column=3)

window.mainloop()
