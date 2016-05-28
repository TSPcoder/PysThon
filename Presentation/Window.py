from tkinter import *
from Abstraction.Constraint import Constraint
from Abstraction.Solver import Solver
from Abstraction.Table import Table
from Presentation.GraphFrame import GraphFrame
from Presentation.LeftFrame import LeftFrame


class Window(Tk):
    def __init__(self):
        """Builds the whole window with two main Frames, the left one contains buttons and the let one contains the graph"""
        Tk.__init__(self)

        self.bg_color = "#909090"
        self.padx = 3
        self.pady = 3

        self.configure(bg = self.bg_color)
        self.title("PySThon")
        self.gf = None
        self.constraints = []

        "Creating right frame"
        self.right_frame = GraphFrame(self, None, bg = self.bg_color) #pas de controleur pour l'instant
        self.right_frame.pack(side = 'right', padx = self.padx, pady = self.pady)

        "Creating left frame"
        self.left_frame = LeftFrame(self, bg = self.bg_color, bd = 1, relief = RIDGE, padx = self.padx, pady = self.pady)

        self.mainloop()

    def set_gf(self, gf):
        self.gf = gf

    "---------------------------Graph Display----------------------------------"

    def solve_button_action(self, event):
        self.display_graph()
        tab = []
        for e in self.constraints :
            tab.append(e.normalize())
        self.table = Table(tab, self.gf.normalize())
        self.solver = Solver(self.table)
        self.solver.solve()
        self.left_frame.update_table()



    def display_graph(self):
        self.right_frame.destroy()
        self.right_frame = GraphFrame(self, None) #pas de controleur pour l'instant
        self.right_frame.pack(side = 'right')
