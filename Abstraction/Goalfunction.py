# -*-coding:utf-8 -*

class GoalFunction:

    """
    Defining of the Goal function
    Variables  : - coeff list
                 - boolean (true if max , false if min)

    E.g : if z = 3x1 + 4x2 + 5
          if we want to maximize z
          then coeffs = [3,4,5]
          minOrMax = true

    """


    # CONSTRUCTOR
    def __init__(self, myCoeffs=[0,0,0], myMinOrMax=True):
        self.coFunction=myCoeffs
        self.minOrMax=myMinOrMax


    def __str__(self):
        """returns a readable expression of the goal funcutron"""
        op = "min"
        if not self.minOrMax :
            op = "max"
        return " Goal Function :      {} ({}*x1 + {}*x2) ".format(op, self.coFunction[0], self.coFunction[1])

    # e.g , with the example above , normalize returns [3,4,5,True]
    def normalize(self):
        output = []
        temp = self.coFunction
        if self.minOrMax:
            for elt in temp:
                output.append(elt)
        else:
            for elt in temp :
                output.append(-elt)
        output.append(0)

        return output











