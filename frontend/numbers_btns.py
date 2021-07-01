from tkinter import *

class NumbersBTN:
    def __init__(self) :
        self.btn_numbers = []
        for i in range(10):
            self.btn_numbers.append(
                Button(width=5, height=1, padx=5, text=str(i), font='times 14 bold', bd=6,
                       command=lambda x=i: self.enterNumber(x)))
        
        self.btn_text = 1
        for i in range(3, 6):  # dar satre 3,4,5
            for j in range(3):  # dar sotoone 0,1,2
                self.btn_numbers[self.btn_text].grid(row=i, column=j)
                self.btn_text += 1