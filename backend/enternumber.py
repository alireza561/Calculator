from tkinter import *
class EnterNumber:

    def enterNumber(self, x):

        if self.func_scientific == True:
            pass

        else:

            if self.chck_equal == True or self.b == 1 :
                self.entry_box2.delete(0, END)
                self.entry_box2.insert(0, "")
                if self.check_dot:
                    self.entry_box.delete(0, END)
                    self.entry_box.insert(0, "0")

            if not self.check:  
                if self.entry_box.get() == '0':
                    self.entry_box.delete(0, END)
                    self.entry_box.insert(0, str(x))
                else: 
                    length = len(self.entry_box.get())
                    self.entry_box.insert(length, str(x))
            
            if self.check :  
                self.entry_box.delete(0, END)
                self.entry_box.insert(0, "0")

                if self.entry_box.get() == '0': 
                    self.entry_box.delete(0, END)
                    self.entry_box.insert(0, str(x))
                    self.check = False

            self.chck_equal = False
            self.g3 = self.entry_box.get()  
            self.b = 0
            self.c = 0  
            self.g0 = self.g1

