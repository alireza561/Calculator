from tkinter import *
import math

class PMethods:
    def Pi(self):
        my_pi = math.pi
        self.entry_box.delete(0, END)
        self.entry_box.insert(0, str(my_pi))
        self.func_scientific = True
        self.g3 = self.entry_box.get()
        self.g0 = self.g1

    # ======================================= func 2pi ==========================================================

    def _2Pi(self):
        my_2pi = math.pi + math.pi
        self.entry_box.delete(0, END)
        self.entry_box.insert(0, str(my_2pi))
        self.func_scientific = True
        self.g3 = self.entry_box.get()
        self.g0 = self.g1
