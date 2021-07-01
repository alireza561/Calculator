from tkinter import *

class ScientificBTN:
    def __init__(self) :

        for i in range(7, 12):
            for j in range(0, 4):
                self.btn = Button(self.root, width=5, padx=5, font='times 14 bold', bd=6, bg="powder blue")
                self.btn.grid(row=i, column=j)

                if i == 7:
                    if j == 0:
                        self.btn['text'] = "π"
                        self.btn['command'] = self.Pi
                    if j == 1:
                        self.btn['text'] = "2π"
                        self.btn['command'] = self._2Pi
                    if j == 2:
                        self.btn['text'] = "Log"
                        self.btn['command'] = lambda: self.Log('log')
                    if j == 3:
                        self.btn['text'] = "Log2"
                        self.btn['command'] = lambda: self.Log('log2')

                if i == 8:
                    if j == 0:
                        self.btn['text'] = "Log10"
                        self.btn['command'] = lambda: self.Log('log10')
                    if j == 1:
                        self.btn['text'] = "Cos"
                        self.btn['command'] = lambda: self.trigonometry('cos')
                    if j == 2:
                        self.btn['text'] = "Cosh"
                        self.btn['command'] = lambda: self.trigonometry('cosh')
                    if j == 3:
                        self.btn['text'] = "Xp"
                        self.btn['command'] = lambda : self.engineer('xp')

                if i == 9:
                    if j == 0:
                        self.btn['text'] = "Deg"
                        self.btn['command'] = lambda : self.engineer('deg')
                    if j == 1:
                        self.btn['text'] = "Log1p"
                        self.btn['command'] = lambda: self.Log('log1p')
                    if j == 2:
                        self.btn['text'] = "Tan"
                        self.btn['command'] = lambda: self.trigonometry('tan')
                    if j == 3:
                        self.btn['text'] = "Tanh"
                        self.btn['command'] = lambda: self.trigonometry('tan')

                if i == 10:
                    if j == 0:
                        self.btn['text'] = "Mod"
                        self.btn['command'] = self.Mod
                    if j == 1:
                        self.btn['text'] = "Acosh"
                        self.btn['command'] = lambda: self.trigonometry('acosh')
                    if j == 2:
                        self.btn['text'] = "Expm1"
                        self.btn['command'] = lambda : self.engineer('expm1')
                    if j == 3:
                        self.btn['text'] = "Sin"
                        self.btn['command'] = lambda: self.trigonometry('sin')

                if i == 11:
                    if j == 0:
                        self.btn['text'] = "Sinh"
                        self.btn['command'] = lambda: self.trigonometry('sinh')
                    if j == 1:
                        self.btn['text'] = "e"
                        self.btn['command'] = lambda : self.engineer('e')
                    if j == 2:
                        self.btn['text'] = "Asinh"
                        self.btn['command'] = lambda: self.trigonometry('asinh')
                    if j == 3:
                        self.btn['text'] = "√"
                        self.btn['command'] = lambda : self.engineer('sqrt')