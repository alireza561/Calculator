from tkinter import *


# PSMD   --> plus   Submission   Multiplication    Division
class PSMD:
    def __init__(self) :
        for d in range(3, 4):
            for j in range(2, 6):
                if j == 2:
                    i = "+"
                if j == 3:
                    i = "-"
                if j == 4:
                    i = "*"
                if j == 5:
                    i = "/"
                # if j == 6:
                #     i = "%"
                self.btn = Button(width=5, padx=5, font='times 14 bold', text=i, bd=6, bg="powder blue",
                             command=lambda x=i: self.enter_operator(x)) \
                    .grid(row=j, column=d)