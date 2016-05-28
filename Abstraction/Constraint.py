# -*-coding:utf-8 -*

import matplotlib.pyplot as plt


class Constraint :

    def __init__(self, myCoeffs = [1,1,1], myOperator = "<="):
        self.coeffs = myCoeffs
        self.operator = myOperator

    def __repr__(self):
        return "{}*x1 + {}*x2 {} {}".format(self.coeffs[0], self.coeffs[1],
                                            self.operator, self.coeffs[2])

    def normalize(self):
        output = []
        temp = self.coeffs
        for elt in temp:
            output.append(elt)

        if self.operator == ">=":
            output.append(False)

        if self.operator == "<=":
            output.append(True)



        return output

    def intersection(self):
        output =[]
        if self.coeffs[0] != 0 and self.coeffs[1] != 0 :
            x = self.coeffs[2] / self.coeffs[0]
            output.append(0)
            output.append(x)
            y = self.coeffs[2] / self.coeffs[1]
            output.append(y)
            output.append(0)
        elif self.coeffs[0] == 0 :
            y = self.coeffs[2] / self.coeffs[1]
            output.append(1)
            output.append(y)
            output.append(0)
            output.append(y)

        elif self.coeffs[1] == 0 :
            x = self.coeffs[2] / self.coeffs[0]
            output.append(x)
            output.append(0)
            output.append(x)
            output.append(1)
        return output