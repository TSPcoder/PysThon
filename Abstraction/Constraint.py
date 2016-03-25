# -*-coding:utf-8 -*


class Constraint :
   #yo testestekkkkkkkkkkkk etstest222
    """
    Defining of a constraint

    Variables : - coeffs list
                - constant
                - operateur ( a String )

    """

    def __init__(self, myCoeffs=[1,1,1], myOperator= "<"):
        self.coeffsConstraint=myCoeffs
        self.operatorConstraint=myOperator



    def normalize(self):
        outPut = []
        temp = self.coeffsConstraint
        if self.operatorConstraint == "<=" or self.operatorConstraint == "<" or self.operatorConstraint == "=":
            for elt in temp :
                outPut.append(elt)

            if self.operatorConstraint == "=":
                outPut.append(False)

            else:
                outPut.append(True)


        else:
            if self.operatorConstraint == ">=" or self.operatorConstraint == ">":
                for elt in temp :
                    outPut.append(-elt)

            outPut.append(True)



        return outPut








