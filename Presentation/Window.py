# Author : Aymeric ALOUGES

from Presentation.Graph import *
from Abstraction.Solver import *
from Abstraction.TableFinale import *
from Presentation.Graph import Graph
from tkinter.ttk import Labelframe
import numpy as np
import matplotlib as mpl
from Presentation.ConstraintCreation import *
from Presentation.FunctionCreation import *
from tkinter import *


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
        Button(frameModification, text='Modifier').grid(row=3, column=1, columnspan=2, padx=10, pady=5)
        Button(frameModification, text='décaler à gauche').grid(row=4, column=1, padx=10, pady=2.5, stick=E)
        Button(frameModification, text='décaler à droite').grid(row=4, column=2, padx=10, pady=5, stick=W)
        Button(frameModification, text='décaler en haut').grid(row=5, column=1, padx=10, pady=5, stick=E)
        Button(frameModification, text='décaler en bas').grid(row=5, column=2, padx=10, pady=5, stick=W)
        Button(frameModification, text='tourner sens horaire').grid(row=6, column=1, padx=10, pady=5, stick=E)
        Button(frameModification, text='tourner sens anti horaire').grid(row=6, column=2, padx=10, pady=5, stick=W)
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

        Button(frameTable, text='Suivant').grid(row=1, column=1, padx=10, pady=2.5, stick=E)
        Button(frameTable, text='Précedent').grid(row=1, column=2, padx=10, pady=5, stick=W)
        frameTable.pack(side="top", padx=5, pady=5)

        #Right of the GUI

        self.frameRight = Frame(self, borderwidth = 0, relief = GROOVE)
        self.frameRight.pack(side = "right")


        canvasGraph = Graph(self.frameRight)
        canvasGraph.pack(side = "right")

        # Generate some example data
        X = np.linspace(0, 2.0*3.14, 50)
        Y = np.sin(X)

        # Create the figure we desire to add to an existing canvas
        fig = mpl.figure.Figure()
        ax = fig.add_axes([0, 0, 1, 1])
        ax.plot(X, Y)

        # Keep this handle alive, or else figure will disappear
        fig_x, fig_y = 100, 100
        fig_photo = canvasGraph.draw_figure(fig)
        fig_w, fig_h = fig_photo.width(), fig_photo.height()

        #draw_figure(canvasGraph, figure, loc=(0, 0))
        #Graphic = Graph(self.FrameTop, width=1000, height=750)
        #Graphic.pack(side="right", padx=5, pady=5)

        # Tkinter loop
        self.mainloop()

    def graph(self):
        fig = mpl.figure.Figure()
        self.ax = self.canvasGraph.draw_constraints(self.constraints, fig)
        fig.set_figheight(self.height/fig.dpi)
        fig.set_figwidth(self.width/fig.dpi)
        fig_x, fig_y = 0, 0
        fig_photo = self.canvasGraph.draw_figure(fig, loc=(fig_x, fig_y))
        fig_w, fig_h = fig_photo.width(), fig_photo.height()

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

    def buttonGF(self, event):
        FunctionCreation(self)
        # print("GF")

    def solve(self, event):
        self.graph()
        self.table = TableFinale(self.constraints, self.gf)
        self.solver = Solver(self.table)
        self.solver.solve()
