from tkinter import *

class ConstraintCreation() :
    def __init__(self):
        self.window = Tk()
        self.nom = 'Nom de la cotrainte'
        Label(self.window, text = 'Nouvelle Contrainte').grid(row =1, column =1, columnspan =2, padx =10, pady =5)
        self.nom = StringVar()
        Entry(self.window, textvariable=self.nom, width=30).grid(row =2, column =1, columnspan =2, padx =10, pady =5)

        Label(self.window, text = 'Coefficient de x1').grid(row =3, column =1, padx =10, pady =5,stick = E)
        coef1 = StringVar()
        coef1.set("")
        Entry(self.window, width=10).grid(row =3, column =2, padx =10, pady =5)

        Label(self.window, text = 'Coefficient de x2').grid(row =4, column =1, padx =10, pady =5,stick = E)
        coef2 = StringVar()
        coef2.set("")
        Entry(self.window, width=10).grid(row =4, column =2, padx =10, pady =5)

        Label(self.window, text = 'opérateur').grid(row =5, column =1, padx =10, pady =5,stick = E)
        operator = StringVar()
        operator.set("")
        Entry(self.window, width=10).grid(row =5, column =2, padx =10, pady =5)

        Label(self.window, text = 'constante').grid(row =6, column =1, padx =10, pady =5,stick = E)
        constant = StringVar()
        constant.set("")
        Entry(self.window, width=10).grid(row =6, column =2, padx =10, pady =5)

        valider = Button(self.window, text ='Valider')
        valider.grid(row =7, column =1, padx =10, pady =5)
        valider.bind('<Button-1>', self.validate())

        Button(self.window, text ='Annuler', command = self.window.quit).grid(row =7, column =2, padx =10, pady =5)

        # Tkinter loop
        self.window.mainloop()

    def validate(self, event):
        print(self.nom)

#f = ConstraintCreation()