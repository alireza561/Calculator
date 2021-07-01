from tkinter import *
from math import log , log2 , log10 , log1p

class LogMethods:
    def Log(self , method):
        try:
            my_number = self.entry_box.get()
            if method == 'log':
                my_log = log(float(my_number))
            elif method == 'log2':
                my_log = log2(float(my_number))
            elif method == 'log10':
                my_log = log10(float(my_number))
            elif method == 'log1p':
                my_log = log1p(float(my_number))
            
            self.entry_box.delete(0, END)
            self.entry_box.insert(0, str(my_log))
            self.func_scientific = True
            self.g3 = self.entry_box.get()
            self.g0 = self.g1
        except Exception as e:
            pass