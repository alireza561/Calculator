from tkinter import *

class EntryBox:
    def __init__(self) :
        self.entry_box = Entry(self.root, font='verdona 14 bold', bg='#e6e6fa', justify=RIGHT, width=28, bd=6)
        self.entry_box.insert(0, '0')
        self.entry_box.grid(row=1, column=0, columnspan=4)

        self.entry_box2 = Entry(self.root, font='verdona 14 bold', bg='#e6e6fa', justify=RIGHT, width=28, bd=6)
        self.entry_box2.insert(0, '')
        self.entry_box2.grid(row=0, column=0, columnspan=4)