import matplotlib as mpl
import tkinter as tk

from Abstraction.Constraint import Constraint
from Abstraction.Goalfunction import GoalFunction
from Abstraction.Solver import Solver
from Abstraction.TableFinale import TableFinale
from Presentation.ConstraintCreationWindow import ConstraintCreationWindow
from Presentation.FunctionCreationWindow import FunctionCreationWindow
from Presentation.GraphFrame import GraphFrame
from Presentation.LeftFrame import LeftFrame

mpl.use("TkAgg")


class Window(tk.Tk):
    def __init__(self):
        """Builds the whole window with two main Frames, the left one contains buttons and the let one contains the graph"""
        tk.Tk.__init__(self)

        self.title("PySThon")
        self.gf = None
        self.constraints = []

        "Creating right frame"
        self.right_frame = GraphFrame(self, None) #pas de controleur pour l'instant
        self.right_frame.pack(side = 'right')

        "Creating left frame"
        self.left_frame = LeftFrame(self)

        self.mainloop()

    def set_gf(self, gf):
        self.gf = gf
        self.left_frame.build_gf_frame_filled()


    "--------------Right Frame-------------------------------------------------"
    "---------------------------Graph Display----------------------------------"

    def solve(self, event):
        self.graph()
        tab = []
        for e in self.constraints :
            tab.append(e.normalize())
        self.table = TableFinale(tab, self.gf.normalize())
        self.solver = Solver(self.table)
        self.solver.solve()
        self.left_frame.update_table()



    def graph(self):
        self.right_frame.destroy()
        self.right_frame = GraphFrame(self, None) #pas de controleur pour l'instant
        self.right_frame.pack(side='right')
