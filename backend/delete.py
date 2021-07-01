from tkinter import *

class Delete:
    def func_delete(self):
        if self.func_scientific:
            pass
        else:

            if not self.chck_equal :

                length = len(self.entry_box.get())
                all_text = self.entry_box.get()
                all_char = all_text[:]

                if all_char[-1] == ".":
                    self.entry_box.delete(length - 1, END)
                    self.check_dot = True
                else:
                    self.entry_box.delete(length - 1, END)
                if length == 1:
                    self.entry_box.insert(0, '0')
            else:
                pass
    
    def func_ch(self):
        self.history.delete(0, END)
