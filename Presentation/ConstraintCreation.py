from tkinter import *
from Presentation.Window import Window
from Abstraction.Constraint import *


class ConstraintCreation():
    def __init__(self):
        self.window = Tk()
        self.win = Window()

        Label(self.window, text='Nouvelle Contrainte').grid(row=1, column=1, columnspan=2, padx=10, pady=5)
        name = StringVar()
        name.set("Nom de la contrainte")
        self.nom = Entry(self.window, textvariable=name, width=30)
        self.nom.grid(row=2, column=1, columnspan=2, padx=10, pady=5)

        Label(self.window, text='Coefficient de x1').grid(row=3, column=1, padx=10, pady=5, stick=E)
        coef1 = StringVar()
        coef1.set("")
        self.c1 = Entry(self.window, textvariable=coef1, width=10)
        self.c1.grid(row=3, column=2, padx=10, pady=5)

        Label(self.window, text='Coefficient de x2').grid(row=4, column=1, padx=10, pady=5, stick=E)
        coef2 = StringVar()
        coef2.set("")
        self.c2 = Entry(self.window, textvariable=coef2, width=10)
        self.c2.grid(row=4, column=2, padx=10, pady=5)

        Label(self.window, text='opérateur').grid(row=5, column=1, padx=10, pady=5, stick=E)
        operator = StringVar()
        operator.set("")
        self.op = Entry(self.window, textvariable=operator, width=10)
        self.op.grid(row=5, column=2, padx=10, pady=5)

        Label(self.window, text='constante').grid(row=6, column=1, padx=10, pady=5, stick=E)
        constant = IntVar()
        constant.set("")
        self.cst = Entry(self.window, textvariable=constant, width=10)
        self.cst.grid(row=6, column=2, padx=10, pady=5)

        valider = Button(self.window, text='Valider')
        valider.grid(row=7, column=1, padx=10, pady=5)
        valider.bind('<Button-1>', self.validate)

        Button(self.window, text='Annuler', command=self.window.quit).grid(row=7, column=2, padx=10, pady=5)

        # Tkinter loop
        self.window.mainloop()

    def validate(self, event):
        c = Constraint([self.c1, self.c2, self.cst], self.op)
        # print(self.nom.get(), " : x1 * ", self.c1.get(), " x2 * ", self.c2.get(), " ", self.op.get(), " ", self.cst.get())
        self.win.addConstraint(c)
