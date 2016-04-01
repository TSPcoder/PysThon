from Abstraction import Constraint

class TableController :

    def __init__(self, main):
        self.main = main

    def  addConstraint(self, *coefs, op):
        c = Constraint(coefs[0], coefs[1], coefs[2], op)
        self.main.constraints.__add__(c)
        self.main.table.addConstraintStepOne(c)
