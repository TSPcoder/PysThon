# Author : Aymeric ALOUGES

from Presentation.Graph import *

# Creation of our window
from tkinter.ttk import Labelframe


class Window(Frame):
    def __init__(self,Boss =None,  width=200, height=150):
        Frame.__init__(self)

        self.configure(width=width, height=height)
        self.width, self.height = width, height
        self.constraints = []
        self.gf = None

        # Top of the GUI
        self.FrameTop = Frame(self, borderwidth=0, relief=GROOVE)
        self.FrameTop.pack(side="top")

        FrameModification = Labelframe(self.FrameTop, borderwidth=0, relief=GROOVE, text="Modification de la Contrainte")
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


        #CanvasGraph = Canvas(self.FrameTop, width =200, height =150, bg="blue")
        #CanvasGraph.pack(side = "left")
        Graphic = Graph (self.FrameTop, width=1000, height=750)
        Graphic.pack(side = "right", padx=5, pady=5)

       # Graphic.traceCourbe()
        FrameTable = LabelFrame(self, borderwidth=0, relief=GROOVE,text="Tableau")
        for ligne in range(5):
           for colonne in range(5):
              Label(FrameTable, text='L%s-C%s' % (ligne, colonne), relief=GROOVE, borderwidth=5).grid(row=ligne, column=colonne)
        FrameTable.pack(side="bottom", padx=5, pady=5)

        # Bottom of the GUI
        self.FrameBottom = Frame(self, borderwidth=0, relief=GROOVE)
        self.FrameBottom.pack(side="bottom")

        FrameButtons = Frame(self.FrameBottom, borderwidth=0, relief=GROOVE)
        Button(FrameButtons, text='Lancer la résolution').pack(side="bottom", padx=5, pady=5)
        f = Button(FrameButtons, text='Fonction objectif')
        f.bind('<Button-1>', self.buttonGF)
        f.pack(side="bottom", padx=5, pady=5)
        b = Button(FrameButtons, text='Ajouter une Contrainte')
        b.bind('<Button-1>', self.buttonConstraint)
        b.pack(side="bottom", padx=5, pady=5)

        FrameButtons.pack(side="left", padx=0, pady=0)

        FrameConstraints = Labelframe(self.FrameBottom, borderwidth=0, relief=GROOVE, text="Constraintes")
        listConstraints = Listbox(FrameConstraints)
        listConstraints.insert(1, "contrainte 1")
        listConstraints.insert(2, "contrainte 2")
        listConstraints.insert(3, "contrainte 3")
        listConstraints.pack()
        FrameConstraints.pack(side="left", padx=5, pady=5)

        FrameResults = Labelframe(self.FrameBottom, borderwidth=0, relief=GROOVE, text="Résultat")
        labelResults = Label(FrameResults, text="Résultats", bg="white")
        labelResults.pack()
        FrameResults.pack(side="left", padx=5, pady=5)




        self.pack()
        # Tkinter loop
        #self.win.mainloop()


    def addConstraint(self, constraint):
        self.constraints.append(constraint)

    def setGF(self, gf):
        self.gf = gf

    def buttonConstraint(self, event):
        ConstraintCreation()

    def buttonGF(self, event):
        FunctionCreation()
        print("GF")

from Presentation.ConstraintCreation import *
from Presentation.FunctionCreation import *