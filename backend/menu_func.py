from tkinter import *
from tkinter import messagebox

class MenuFunction:
    def iExit(self):
        iexit = messagebox.askyesno("scientific calculator", "confirm if you want to exit")
        if iexit:
            self.root.destroy()
            return
    
    def Scientific(self):
        self.root.resizable(0, 0)
        self.root.geometry("550x543+200+100")
        self.history.config(width=30, height=33)
    
    def Standard(self):
        self.root.resizable(0, 0)
        self.root.geometry("550x308+200+100")
        self.history.config(width=30, height=18)