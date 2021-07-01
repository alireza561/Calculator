from tkinter import *

class Equal:
    def func_equal(self):

        if self.entry_box.get() == '0' and self.entry_box2.get() == '0' :
            pass
        elif not self.chck_equal:
            if self.a == 0: 
                length = self.entry_box.get()
                self.entry_box.delete(0, END)
                self.entry_box.insert(0, '0')
                self.entry_box2.delete(0, END)
                self.entry_box2.insert(0, length)
                length = length + "="
                self.history.insert(0, length)
                self.b = 1    
                self.chck_equal == True

            elif self.entry_box.get() == "0":    
                content = self.entry_box2.get()
                content2 = content[:-1]   
                result = eval(content2)
                self.entry_box2.delete(0, END)
                self.entry_box2.insert(0, "")
                self.entry_box.delete(0, END)
                self.entry_box.insert(0, result)
                length = content + "=" + "0"
                self.history.insert(0, length)



            else:
                if self.c == 0 or self.func_scientific == True:  
                    extra_num = self.entry_box.get()
                    length = len(self.entry_box2.get())
                    self.entry_box2.insert(length, extra_num)
                    content = self.entry_box2.get()
                    result = eval(content)
                    self.entry_box2.delete(0, END)
                    self.entry_box2.insert(0, "0")
                    self.entry_box.delete(0, END)
                    self.entry_box.insert(0, result)
                    length = content + "=" + self.entry_box.get()
                    self.history.insert(0, length)



                else:
                    content = self.entry_box2.get()
                    content2 = content[:-1]
                    result = eval(content2)
                    self.entry_box2.delete(0, END)
                    self.entry_box2.insert(0, "0")
                    self.entry_box.delete(0, END)
                    self.entry_box.insert(0, result)
                    length = content2 + "=" + self.entry_box.get()
                    self.history.insert(0, length)

                self.chck_equal = True



        elif self.g0 != 0: #
                length = self.entry_box.get()
                value = str(self.g0) + str(self.g3)
                self.entry_box.insert(END, value)
                content = self.entry_box.get()
                self.entry_box.delete(0, END)
                self.entry_box.insert(0, eval(content))
                self.chck_equal = True  
                length2 = length + str(self.g0) + str(self.g3) + "=" + self.entry_box.get()
                self.history.insert(0, length2)
        else:
            pass

        self.check_dot = True
        self.a = 0
        self.g1 = 0
        self.func_scientific = False
