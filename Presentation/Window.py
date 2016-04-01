# Author : Aymeric ALOUGES

from Presentation.ConstraintCreation import *

# Creation of our window
from tkinter.ttk import Labelframe


class Window:
    def __init__(self):
        self.win = Tk()

        # set the window fulscreen
        # window.attributes('-fullscreen', 1)

        # Top of the GUI
        FrameTop = Frame(self.win, borderwidth=0, relief=GROOVE)
        FrameTop.pack(side="top")

        FrameModification = Labelframe(FrameTop, borderwidth=0, relief=GROOVE, text="Modification de la Contrainte")
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

        FrameGraphic = Labelframe(FrameTop, borderwidth=0, relief=GROOVE, text="Interpretation Géometrique")
        Canvas(FrameGraphic, bg='dark grey', height=700, width=1500).pack()
        FrameGraphic.pack(side="left", padx=5, pady=5)

        # Bottom of the GUI
        FrameBottom = Frame(self.win, borderwidth=0, relief=GROOVE)
        FrameBottom.pack(side="bottom")

        FrameButtons = Frame(FrameBottom, borderwidth=0, relief=GROOVE)
        Button(FrameButtons, text='Lancer la résolution').pack(side="bottom", padx=5, pady=5)
        Button(FrameButtons, text='Fonction objectif').pack(side="bottom", padx=5, pady=5)
        b = Button(FrameButtons, text='Ajouter une Contrainte')
        b.bind('<Button-1>', self.addConstraint)
        b.pack(side="bottom", padx=5, pady=5)

        FrameButtons.pack(side="left", padx=0, pady=0)

        FrameConstraints = Labelframe(FrameBottom, borderwidth=0, relief=GROOVE, text="Constraintes")
        listConstraints = Listbox(FrameConstraints)
        listConstraints.insert(1, "contrainte 1")
        listConstraints.insert(2, "contrainte 2")
        listConstraints.insert(3, "contrainte 3")
        listConstraints.pack()
        FrameConstraints.pack(side="left", padx=5, pady=5)

        FrameResults = Labelframe(FrameBottom, borderwidth=0, relief=GROOVE, text="Résultat")
        labelResults = Label(FrameResults, text="Résultats", bg="white")
        labelResults.pack()
        FrameResults.pack(side="left", padx=5, pady=5)

        # Tkinter loop
        self.win.mainloop()

    def addConstraint(self, event):
        #print("ajouter une contrainte")
        ConstraintCreation()


w = Window()
