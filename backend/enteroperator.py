from tkinter import *

class EnterOperator:
    def enter_operator(self, x):  # when you enter -> + = * / %
        if x == "MOD":
            x = "%"
        
        try:

            if self.chck_equal:  # in shart yani age dokmeye mosavi zade shode
                self.g2 = self.entry_box.get()  # oon chizi ke entry_box paini az ma migire ; mirizim tooye yek moteghayer
                self.g1 = x   # argumani ke (+-*/%) toosh gharar dare ro mirizim tooye yek moteghayer
                if self.g2[-1] == ".":   # mohtavaye entry_box yek list az reshte hast
                    z = str(self.g2[:-1]) + self.g1
                else:
                    z = str(eval(self.g2)) + self.g1
                self.entry_box2.delete(0, END)
                self.entry_box2.insert(0, z)
                all_text = self.entry_box2.get()
                all_char = all_text[:-1]
                res = eval(all_char)
                self.entry_box.delete(0, END)
                self.entry_box.insert(0, res)
                self.chck_equal = False

            else:
                length = len(self.entry_box2.get())
                self.g1 = x
                self.g2 = self.entry_box.get()
                if self.g2[-1] == ".":
                    z = str(self.g2[:-1]) + self.g1
                else:
                    z = str(eval(self.g2)) + self.g1

                if self.entry_box2.get() != self.entry_box.get():
                    if self.entry_box2.get() == "":
                        self.entry_box2.insert(0, z)
                        all_text = self.entry_box2.get()
                        all_char = all_text[:-1]
                        res = eval(all_char)
                        self.entry_box.delete(0, END)
                        self.entry_box.insert(0, res)
                    else:
                        self.entry_box2.insert(length, z)
                        self.entry_box.delete(0, END)
                        all_text = self.entry_box2.get()
                        all_char = all_text[:-1]
                        res = eval(all_char)
                        self.entry_box.insert(0, res)

                elif self.entry_box2.get() == self.entry_box.get():
                    self.entry_box2.delete(0, END)
                    self.entry_box2.insert(length, z)
                    self.entry_box.delete(0, END)
                    all_text = self.entry_box2.get()
                    all_char = all_text[:-1]
                    res = eval(all_char)
                    self.entry_box.insert(0, res)
                
        except:
            self.entry_box.insert(END, "")

        self.check_dot = True
        self.check = True   
        self.a = 1
        self.chck_equal = False
        self.b = 0
        self.c = 1  

        self.func_scientific = False