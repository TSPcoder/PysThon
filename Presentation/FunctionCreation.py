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
        v.bind('<Button-1>', self.validate)
        Button(self.window, text ='Annuler', command=self.window.destroy).grid(row =6, column =2, padx =10, pady =5)
        # Tkinter loop
        self.window.mainloop()

    def str_to_int(self, a):
        try:
            return int(a)
        except:
            print("l'argument n'est pas du bon type")
            return a

    def str_to_float(self, a):
        try:
            return float(a)
        except:
            print("l'argument n'est pas du bon type")
            return a

    def validate(self, event):
        temp = self.op.get()
        if type(self.str_to_int(self.c1.get())) != int:
            # message d'alerte : c1 mal saisi
            showwarning('Attention !', 'Le premier coefficient est mal saisi.')
            print("c1 est mal saisi")
        elif type(self.str_to_int(self.c2.get())) != int:
            # message d'alerte : c2 est mal saisi
            showwarning('Attention !', 'Le deuxième coefficient est mal saisi.')
            print("c2 esl mal saisi")
        elif temp != "min" and temp != "max":
            # message d'alerte : op est mal saisi
            showwarning('Attention !', "L'opérateur est mal saisi.")
            print("op est mal saisi")
        elif type(self.str_to_int(self.cst.get())) != int:
            # message d'alerte : cst est mal saisi
            showwarning('Attention !', 'La constante est mal saisie.')
            print("cst est mal saisi")
        else:
            gf = GoalFunction([self.str_to_int(self.c1.get()), self.str_to_float(self.c2.get()), self.str_to_float(self.cst.get())]
                              ,self.op.get())
            self.win.set_gf(gf)
            self.win.build_gf_frame_filled()
            self.window.destroy()