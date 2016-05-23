from Presentation.Window import *
from Presentation.ConstraintCreation import *
from Abstraction.Constraint import *

class ConstraintControl:

    def __init__(self, win):
        self.win = win
        self.cons_crea = ConstraintCreation(win)

    def validate(self, event):
        c = Constraint(self.cons_crea.getCoefs(), self.cons_crea.getOp())
        self.win.add_constraint(c)