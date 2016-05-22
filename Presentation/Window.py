# Author : Aymeric ALOUGES

from Presentation.Graph import *
from Abstraction.Solver import *
from Abstraction.TableFinale import *
from tkinter.ttk import Labelframe
import matplotlib.pyplot as plt

# Creation of our window



class Window(Frame):
    def __init__(self, Boss=None, width=200, height=150):
        self.win = Tk()
        Frame.__init__(self)


        self.configure(width=width, height=height)
        self.width, self.height = self.win.winfo_screenwidth(), self.win.winfo_screenheight()-80
        self.constraints = []
        self.gf = None
        self.solver = None
        self.table = None

        # Left of the GUI
        self.FrameLeft = Frame(self, borderwidth=0, relief=GROOVE)
        self.FrameLeft.pack(side="left")

        FrameTop = Frame(self.FrameLeft, borderwidth=0, relief=GROOVE)
        FrameTop.pack(side="top")

        FrameModification = Labelframe(FrameTop, borderwidth=0, relief=GROOVE,text="Modification de la Contrainte")
        Label(FrameModification, text='Nom de la contrainte').grid(row=1, column=1, columnspan=2, padx=10, pady=5)
        Label(FrameModification, text='Affichage constrainte').grid(row=2, column=1, columnspan=2, padx=10, pady=5)
        Button(FrameModification, text='Modifier').grid(row=3, column=1, columnspan=2, padx=10, pady=5)
        Button(FrameModification, text='décaler à gauche').grid(row=4, column=1, padx=10, pady=2.5, stick=E)
        Button(FrameModification, text='décaler à droite').grid(row=4, column=2, padx=10, pady=5, stick=W)
        Button(FrameModification, text='décaler en haut').grid(row=5, column=1, padx=10, pady=5, stick=E)
        Button(FrameModification, text='décaler en bas').grid(row=5, column=2, padx=10, pady=5, stick=W)
        Button(FrameModification, text='tourner sens horaire').grid(row=6, column=1, padx=10, pady=5, stick=E)
        Button(FrameModification, text='tourner sens anti horaire').grid(row=6, column=2, padx=10, pady=5, stick=W)
        Button(FrameModification, text='Supprimer').grid(row=7, column=1, columnspan=2, padx=10, pady=5)
        FrameModification.pack(side="left", padx=5, pady=5)

        # Bottom of the GUI
        self.FrameBottom = Frame(self.FrameLeft, borderwidth=0, relief=GROOVE)
        self.FrameBottom.pack(side="top")

        FrameButtons = Frame(self.FrameBottom, borderwidth=0, relief=GROOVE)
        solve = Button(FrameButtons, text='Lancer la résolution')
        solve.pack(side="bottom", padx=5, pady=5)
        solve.bind('<Button-1>', self.solve)

        f = Button(FrameButtons, text='Fonction objectif')
        f.bind('<Button-1>', self.buttonGF)
        f.pack(side="bottom", padx=5, pady=5)

        b = Button(FrameButtons, text='Ajouter une Contrainte')
        b.bind('<Button-1>', self.buttonConstraint)
        b.pack(side="bottom", padx=5, pady=5)

        FrameButtons.pack(side="left", padx=0, pady=0)

        FrameConstraints = Labelframe(self.FrameBottom, borderwidth=0, relief=GROOVE, text="Constraintes")
        self.listConstraints = Listbox(FrameConstraints)
        self.listConstraints.pack()
        FrameConstraints.pack(side="left", padx=5, pady=5)

        FrameResults = Labelframe(self.FrameLeft, borderwidth=0, relief=GROOVE, text="Résultat")
        labelResults = Label(FrameResults, text="Résultats", bg="white")
        labelResults.pack()
        FrameResults.pack(side="top", padx=5, pady=5)

        FrameTable = LabelFrame(self.FrameLeft, borderwidth=0, relief=GROOVE, text="Tableau")
        for ligne in range(5):
            for colonne in range(5):
                Label(FrameTable, text='L%s-C%s' % (ligne, colonne), relief=GROOVE, borderwidth=5).grid(row=ligne,
                                                                                                        column=colonne)

        Button(FrameTable, text='Suivant').grid(row=1, column=1, padx=10, pady=2.5, stick=E)
        Button(FrameTable, text='Précedent').grid(row=1, column=2, padx=10, pady=5, stick=W)
        FrameTable.pack(side="top", padx=5, pady=5)

        #Right of the GUI

        self.FrameRight = Frame(self, borderwidth=0, relief=GROOVE)
        self.FrameRight.pack(side="right")
        print(self.height)
        self.CanvasGraph = Graph(self.FrameRight, width =self.width*0.8, height =self.height)
        self.CanvasGraph.pack(side = "right")

        self.pack()
        # Tkinter loop
        self.win.mainloop()

    def graph(self):
        fig = mpl.figure.Figure()
        self.ax = self.CanvasGraph.draw_constraints(self.constraints, fig)
        fig.set_figheight(self.height/fig.dpi)
        fig.set_figwidth(self.width/fig.dpi)
        fig_x, fig_y = 0, 0
        fig_photo = self.CanvasGraph.draw_figure(fig, loc=(fig_x, fig_y))
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
        #self.solver.solve()


from Presentation.ConstraintCreation import *
from Presentation.FunctionCreation import *
