# -*-coding:utf-8 -*

import matplotlib.pyplot as plt


class Constraint :
   #yo testestekkkkkkkkkkkk etstest222
    """
    Defining of a constraint

    Variables : - coeffs list
                - constant
                - operateur ( a String )

    """

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
