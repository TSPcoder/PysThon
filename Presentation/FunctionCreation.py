# Autor : Aymeric ALOUGES

from tkinter import *
from Presentation.Window import *
from Abstraction.Goalfunction import *

#Creation of our window

class FunctionCreation:

    def __init__(self, win):
        self.window = Tk()
        self.win = win

        Label(self.window, text = 'Fonction objectif').grid(row =1, column =1, columnspan =2, padx =10, pady =5)

        Label(self.window, text = 'Coéficient de x1').grid(row =2, column =1, padx =10, pady =5,stick = E)
        coef1 = StringVar()
        coef1.set("")
        self.c1 = Entry(self.window, textvariable=coef1,width=10)
        self.c1.grid(row =2, column =2, padx =10, pady =5)

        Label(self.window, text = 'Coéficient de x2').grid(row =3, column =1, padx =10, pady =5,stick = E)
        coef2 = StringVar()
        coef2.set("")
        self.c2 = Entry(self.window, textvariable=coef2,width=10)
        self.c2.grid(row =3, column =2, padx =10, pady =5)

        Label(self.window, text = 'opérateur').grid(row =4, column =1, padx =10, pady =5,stick = E)
        operator = StringVar()
        operator.set("")
        self.op = Entry(self.window, textvariable=operator,width=10)
        self.op.grid(row =4, column =2, padx =10, pady =5)

        Label(self.window, text = 'constante').grid(row =5, column =1, padx =10, pady =5,stick = E)
        constant = StringVar()
        constant.set("")
        self.cst = Entry(self.window, textvariable=constant,width=10)
        self.cst.grid(row =5, column =2, padx =10, pady =5)

        v = Button(self.window, text ='Valider')
        v.grid(row =6, column =1, padx =10, pady =5)
        v.bind()
        Button(self.window, text ='Annuler').grid(row =6, column =2, padx =10, pady =5)
        # Tkinter loop
        self.window.mainloop()

    def validate(self, event):
        gf = GoalFunction([self.c1.get(), self.c2.get(), self.cst.get()],self.op.get())
        self.win.setGF(gf)