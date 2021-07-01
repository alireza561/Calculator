from tkinter import *


from frontend.button_psmd import PSMD
from frontend.entry import EntryBox
from frontend.numbers_btns import NumbersBTN
from frontend.extra_btn import ExtraBTN
from frontend.btn_scientific import ScientificBTN

from backend.menu_func import MenuFunction
from backend.enternumber import EnterNumber
from backend.dot import DOT
from backend.enteroperator import EnterOperator
from backend.clear import Clear
from backend.func_equal import Equal
from backend.delete import Delete
from backend.P_methods import PMethods
from backend.log_methods import LogMethods
from backend.Trigonometry import Trigonometry
from backend.engineering import Engineering


class myCALC(PSMD , EntryBox , NumbersBTN , ExtraBTN , ScientificBTN , MenuFunction ,
 EnterNumber , DOT , EnterOperator , Clear , Equal , Delete , PMethods , LogMethods , Trigonometry, Engineering) :

    root = Tk()
    root.title('hey')
    root.geometry('550x308+200+100')
    root.resizable(0, 0)

    def __init__(self):
        PSMD.__init__(self)
        EntryBox.__init__(self)
        NumbersBTN.__init__(self)
        ExtraBTN.__init__(self)
        ScientificBTN.__init__(self)


        self.menubar = Menu(self.root)
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="file", menu=self.filemenu)
        self.filemenu.add_command(label="Standard", command=self.Standard)
        self.filemenu.add_command(label="Scientific", command=self.Scientific)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.iExit)
        self.root.configure(menu=self.menubar)

        # ======================================  flexibles ===============================================

        self.g1 = 0
        self.g2 = 0
        self.z2 = ""
        self.g3 = 0
        self.check_dot = True
        self.check = False
        self.result = 0
        self.history = []
        self.chck_equal = False
        self.a = 0
        self.b = 0
        self.c = 0
        self.g0 = 0
        self.func_scientific = False

        # ======================================  histoty ===============================================

        self.history = Listbox(self.root, bd=9, bg="gray", width=30, height=18)
        self.history.place(x=350)

        # ======================================  mainloop ===============================================
        self.root.mainloop()

        # ======================================  function ===============================================

    def Mod(self):
        self.enter_operator("MOD")

    def func_darsad(self):
        my_number = float(self.entry_box.get()) / 100
        content = str(my_number) + "*"
        self.entry_box2.insert(END, content)
        self.entry_box.delete(0, END)
        self.entry_box.insert(0, "0")
        self.a = 1
        self.chck_equal = False
        self.check_dot = True

calculator = myCALC()