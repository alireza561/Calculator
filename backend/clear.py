from tkinter import *

class Clear:
    def func_clear(self):

        self.entry_box.delete(0, END)
        self.entry_box.insert(0, '0')
        self.entry_box2.delete(0, END)
        self.entry_box2.insert(0, '')
        self.check_dot = True
        self.chck_equal = False
        self.a = 0