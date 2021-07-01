from tkinter import *

class ExtraBTN:
    def __init__(self) :
        self.btn_zero = Button(width=5, padx=5, text='0', bd=6, font='times 14 bold', command=lambda x=0: self.enterNumber(x))
        self.btn_zero.grid(row=6, column=1)

        self.btn_clear = Button(width=5, padx=5, text='C', font='times 14 bold', bd=6, bg="red", command=self.func_clear)
        self.btn_clear.grid(row=2, column=1)

        self.btn_dot = Button(width=5, padx=5, text='0.0', font='times 14 bold', bd=6, bg="yellow", command=self.dot)
        self.btn_dot.grid(row=6, column=0)

        self.btn_equal = Button(width=5, padx=5, text='=', font='times 14 bold', bd=6, bg="yellow", command=self.func_equal)
        self.btn_equal.grid(row=6, column=2)

        self.btn_delet = Button(width=5, padx=5, font='times 14 bold', bd=6, text='del', bg="red", command=self.func_delete)
        self.btn_delet.grid(row=2, column=2)

        self.btn_ch = Button(width=5, padx=5, font='times 14 bold', bd=6, text='CH', bg="red", command=self.func_ch)
        self.btn_ch.grid(row=2, column=0)

        self.btn_darsad =  Button(width=5, padx=5, font='times 14 bold', bd=6, text='%', bg="powder blue", command=self.func_darsad)
        self.btn_darsad.grid(row=6, column=3)
