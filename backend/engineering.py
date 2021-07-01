from tkinter import *
import math

class Engineering:
    def engineer(self , method):
        try:
                my_number = self.entry_box.get()
                if method == 'xp':
                    my_method = math.exp(float(my_number))
                if method == 'deg':
                    my_method = math.degrees(float(my_number))
                if method == 'e':
                    my_method = math.e
                if method == 'expm1':
                    my_method = math.expm1(float(my_number))
                if method == 'sqrt':
                    my_method = math.sqrt(float(my_number))

                self.entry_box.delete(0, END)
                self.entry_box.insert(0, str(my_method))
                self.func_scientific = True
                self.g3 = self.entry_box.get()
                self.g0 = self.g1

        except Exception as e:
            pass