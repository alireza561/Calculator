from tkinter import *

class DOT:
    def dot(self):

        if self.func_scientific:
            pass

        else:

            if self.chck_equal:   # inja yani age mosavi zade shode va mikhaim adade jadid vared konim
                self.entry_box.delete(0, END)
                self.entry_box.insert(0, "0")
                self.entry_box2.delete(0, END)
                self.entry_box2.insert(0, "")
                self.chck_equal = False
            
            if self.check :  # inja sharte avalie baraye adad vared kardan naghz shode va bayad adade jadid vared she
                self.entry_box.delete(0, END)
                self.entry_box.insert(0, "0")
                if self.entry_box.get() == "0":
                    if self.check_dot:
                        length = len(self.entry_box.get())
                        self.entry_box.insert(length, ".")
                        self.check_dot = False
                        self.check = False
                    else:
                        pass
            
            if not self.check:
                if self.entry_box.get() != "0": # chon adad vared kardim pas dge meghdare pishfarz 0 nist -->(masalan 12.3)
                    if self.check_dot: # sharte avalie baraye momaiez gozashtan
                        length = len(self.entry_box.get())
                        self.entry_box.insert(length, ".")
                        self.check_dot = False   #inja shart ro taghir dadim ke chand ta momaiez dar yek adad nashe vared kard
                    else:
                        pass
                
                if self.entry_box.get() == "0":  # inja hanuz adad vared nakardim va mikhaim ba momaiez shoroo konim -->(masalan 0.12)
                    if self.check_dot:  # sharte avalie baraye momaiez gozashtan
                        length = len(self.entry_box.get())
                        self.entry_box.insert(length, ".")
                        self.check_dot = False   #inja shart ro taghir dadim ke chand ta momaiez dar yek adad nashe vared kard
                    else:
                        pass
            
            self.chck_equal = False