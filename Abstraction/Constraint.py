# -*-coding:utf-8 -*

import matplotlib.pyplot as plt


class Constraint :

    def __init__(self, myCoeffs = [1,1,1], myOperator = "<="):
        self.coeffsConstraint = myCoeffs
        self.operatorConstraint = myOperator

    def toString(self):
        return "{}*x1 + {}*x2 {} {}".format(self.coeffsConstraint[0], self.coeffsConstraint[1],
                                            self.operatorConstraint, self.coeffsConstraint[2])

    def normalize(self):
        outPut = []
        temp = self.coeffsConstraint
        for elt in temp:
            outPut.append(elt)

        if self.operatorConstraint == ">=":
            outPut.append(False)

        if self.operatorConstraint == "<=":
            outPut.append(True)



        return outPut

    def intersection(self):
        outPut =[]
        if self.coeffsConstraint[0] != 0 and self.coeffsConstraint[1] != 0 :
            x = self.coeffsConstraint[2]/self.coeffsConstraint[0]
            outPut.append(0)
            outPut.append(x)
            y = self.coeffsConstraint[2]/self.coeffsConstraint[1]
            outPut.append(y)
            outPut.append(0)
        elif self.coeffsConstraint[0] == 0 :
            y = self.coeffsConstraint[2]/self.coeffsConstraint[1]
            outPut.append(1)
            outPut.append(y)
            outPut.append(0)
            outPut.append(y)

        elif self.coeffsConstraint[1] == 0 :
            x = self.coeffsConstraint[2]/self.coeffsConstraint[0]
            outPut.append(x)
            outPut.append(0)
            outPut.append(x)
            outPut.append(1)
        return outPut