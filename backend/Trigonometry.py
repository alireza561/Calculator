from tkinter import *
import math

class Trigonometry:
    def trigonometry(self, method):
        try:
            my_number = self.entry_box.get()
            if method == 'cos':
                my_method = math.cos(float(my_number))
            if method == 'cosh':
                my_method = math.cosh(float(my_number))
            if method == 'acosh':
                my_method = math.acosh(float(my_number))
            if method == 'sin':
                my_method = math.sin(float(my_number))
            if method == 'sinh':
                my_method = math.sinh(float(my_number))
            if method == 'asinh':
                my_method = math.asinh(float(my_number))
            if method == 'tan':
                my_method = math.tan(float(my_number))
            if method == 'tanh':
                my_method = math.tanh(float(my_number))

            self.entry_box.delete(0, END)
            self.entry_box.insert(0, str(my_method))
            self.func_scientific = True
            self.g3 = self.entry_box.get()
            self.g0 = self.g1
        except Exception as e:
            pass