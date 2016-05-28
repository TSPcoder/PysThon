from Abstraction.Constraint import *
from Presentation.Window import *
from tkinter.messagebox import *
from tkinter import *


class ConstraintCreationWindow:
    def __init__(self, win, bg = "#909090", bd = 1):
        self.window = Tk()
        self.win = win
        self.ops = ['<=', '=', '>=']

        self.frame = Frame(self.window, bg = "#a0a0a0", bd = bd, relief = SUNKEN)
        self.frame.pack(fill = "x", padx = 3, pady = 3)
        Label(self.frame, text = 'Nouvelle Contrainte', bg = "#a0a0a0", bd = bd, relief = SUNKEN).\
            pack(side = "top", padx = 3, pady = 3, fill = "x")
        self.middle_frame = Frame(self.frame, bg = bg)
        self.middle_frame.pack()
        self.label_frame = Frame(self.middle_frame, bg = bg, bd = bd, relief = RAISED)
        self.label_frame.pack(side = "left", fill = "y", padx = 3, pady = 3)
        self.entry_frame = Frame(self.middle_frame, bg = bg, bd = bd, relief = RAISED)
        self.entry_frame.pack(side = "right", fill = "y", padx = 3, pady = 3)
        self.button_frame = Frame(self.frame, bg = bg, bd = bd, relief = RAISED)
        self.button_frame.pack(side = "bottom", padx = 3, pady = 3)

        Label(self.window, text='Coefficient de x1').grid(row = 3, column = 1, padx = 10, pady = 5, stick = E)
        coef1 = StringVar()
        coef1.set("")
        self.c1 = Entry(self.window, textvariable = coef1, width = 10)
        self.c1.grid(row = 3, column = 2, padx = 10, pady = 5)

        Label(self.window, text='Coefficient de x2').grid(row=4, column=1, padx=10, pady=5, stick=E)
        coef2 = StringVar()
        coef2.set("")
        self.c2 = Entry(self.window, textvariable = coef2, width = 10)
        self.c2.grid(row = 4, column = 2, padx = 10, pady = 5)

        Label(self.window, text = 'Opérateur : ').grid(row = 5, column = 1, padx = 10, pady = 5, stick = E)
        operator = StringVar()
        operator.set("")
        self.op = Entry(self.window, textvariable=operator, width=10)
        self.op.grid(row=5, column=2, padx=10, pady=5)

        Label(self.window, text = 'Constante : ').grid(row=6, column=1, padx=10, pady=5, stick=E)
        constant = IntVar()
        constant.set("")
        self.cst = Entry(self.window, textvariable=constant, width=10)
        self.cst.grid(row = 6, column = 2, padx = 10, pady = 5)

        valider = Button(self.window, text = 'Valider')
        valider.grid(row = 7, column = 1, padx = 10, pady = 5)
        valider.bind('<Button-1>', self.validate)
        valider.bind('<Return>', self.validate)

        Button(self.window, text = 'Annuler', command=self.window.destroy).grid(row = 7, column = 2, padx = 10, pady = 5)

        # Tkinter loop
        self.window.mainloop()

    @property
    def getCoefs(self):
        return [self.c1.get(), self.c2.get(), self.cst.get()]

    @property
    def getOp(self):
        return self.op.get()

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
        elif temp != "<=" and temp != "=" and temp != ">=":
            # message d'alerte : op est mal saisi
            showwarning('Attention !', "L'opérateur est mal saisi.")
            print("op est mal saisi")
        elif type(self.str_to_int(self.cst.get())) != int:
            # message d'alerte : cst est mal saisi
            showwarning('Attention !', 'La constante est mal saisie.')
            print("cst est mal saisi")
        else:
            c = Constraint([self.str_to_float(self.c1.get()), self.str_to_float(self.c2.get()), self.str_to_float(self.cst.get())]
                           , self.op.get())
            # print(self.nom.get(), " : x1 * ", self.c1.get(), " x2 * ", self.c2.get(), " ", self.op.get(), " ", self.cst.get())
            self.win.add_constraint(c)
            self.window.destroy()
