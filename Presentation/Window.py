# Author : Aymeric ALOUGES

from Presentation.Graph import *
from Abstraction.Solver import *
from Abstraction.TableFinale import *
from tkinter.ttk import Labelframe
import matplotlib.pyplot as plt
import matplotlib

from matplotlib.figure import Figure

from tkinter import ttk

# Creation of our window


class Window(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        self.constraints = []
        self.gf = None
        self.solver = None
        self.table = None

        # Left of the GUI
        self.frameLeft = Frame(self, borderwidth=0, relief=GROOVE)
        self.frameLeft.pack(side="left")

        frameTop = Frame(self.frameLeft, borderwidth=0, relief=GROOVE)
        frameTop.pack(side="top")

        frameModification = Labelframe(frameTop, borderwidth=0, relief=GROOVE,text="Modification de la Contrainte")
        Label(frameModification, text='Nom de la contrainte').grid(row=1, column=1, columnspan=2, padx=10, pady=5)
        Label(frameModification, text='Affichage constrainte').grid(row=2, column=1, columnspan=2, padx=10, pady=5)
        m = Button(frameModification, text='Modifier')
        m.grid(row=3, column=1, columnspan=2, padx=10, pady=5)
        m.bind('<Button-1>', self.buttonModifier)
        Button(frameModification, text='Supprimer').grid(row=7, column=1, columnspan=2, padx=10, pady=5)
        frameModification.pack(side="left", padx=5, pady=5)

        # Bottom of the GUI
        self.frameBottom = Frame(self.frameLeft, borderwidth=0, relief=GROOVE)
        self.frameBottom.pack(side="top")

        frameButtons = Frame(self.frameBottom, borderwidth=0, relief=GROOVE)
        solve = Button(frameButtons, text='Lancer la résolution')
        solve.pack(side="bottom", padx=5, pady=5)
        solve.bind('<Button-1>', self.solve)

        f = Button(frameButtons, text='Fonction objectif')
        f.bind('<Button-1>', self.buttonGF)
        f.pack(side="bottom", padx=5, pady=5)

        b = Button(frameButtons, text='Ajouter une Contrainte')
        b.pack(side="bottom", padx=5, pady=5)

        frameButtons.pack(side="left", padx=0, pady=0)

        frameConstraints = Labelframe(self.frameBottom, borderwidth=0, relief=GROOVE, text="Constraintes")
        self.listConstraints = Listbox(frameConstraints)
        self.listConstraints.pack()
        frameConstraints.pack(side="left", padx=5, pady=5)

        frameResults = Labelframe(self.frameLeft, borderwidth=0, relief=GROOVE, text="Résultat")
        labelResults = Label(frameResults, text="Résultats", bg="white")
        labelResults.pack()
        frameResults.pack(side="top", padx=5, pady=5)

        frameTable = LabelFrame(self.frameLeft, borderwidth=0, relief=GROOVE, text="Tableau")
        for ligne in range(5):
            for colonne in range(5):
                Label(frameTable, text='L%s-C%s' % (ligne, colonne), relief=GROOVE, borderwidth=5).grid(row=ligne,
                                                                                                        column=colonne)

        frameTable.pack(side="top", padx=5, pady=5)

        # Tkinter loop
        self.mainloop()

    def graph(self):
        xmax = 0
        ymax = 0
        for c in self.constraints:
            print(type(c))
            table = c.intersection()
            if table[1]>xmax:
                xmax = table[1]
            if table[2]>ymax:
                ymax = table[2]
        plt.axis([0,xmax, 0, ymax])
        for c in self.constraints:
            coefs = c.coeffsConstraint
            if coefs[0] != 0 and coefs[1] != 0:
                plt.plot([0, xmax], [ymax, 0])
            elif coefs[0] == 0 and coefs[1] != 0:
                plt.plot([0, xmax],[coefs[2]/coefs[1], coefs[2]/coefs[1]])
            elif coefs[0] != 0 and coefs[1] == 0:
                plt.plot([coefs[2]/coefs[0],coefs[2]/coefs[0]], [0,ymax])
        plt.show()

    def addConstraint(self, constraint):
        print(constraint.toString())
        n = len(self.constraints) + 1
        self.listConstraints.insert(n, constraint.toString())
        if constraint.operatorConstraint == '=':
            constraint1 = Constraint(constraint.coeffsConstraint, '<=').normalize()
            constraint2 = Constraint(constraint.coeffsConstraint, '>=').normalize()
            self.constraints.append(constraint1)
            self.constraints.append(constraint2)
        else:
            #constraint = constraint.normalize()
            self.constraints.append(constraint)

    def setGF(self, gf):
        self.gf = gf.normalize()

    def buttonConstraint(self, event):
        ConstraintCreation(self)

    def buttonModifier(self, event):
        pass

    def buttonGF(self, event):
        FunctionCreation(self)
        # print("GF")

    def solve(self, event):
        print('solve')
        self.graph()
        #self.table = TableFinale(self.constraints, self.gf)
        #self.solver = Solver(self.table)
        #self.solver.solve()


from Presentation.ConstraintCreation import *
from Presentation.FunctionCreation import *
