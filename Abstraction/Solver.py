
class Solver:

    def __init__(self, table):
        """
        :param table: initial table of the problem
        :return:
        """
        self.tab = table

    def simplex(self):
        self.tab.normalize()
        n = self.tab.size()
        p = len(self.tab[n-1])
        checkValues = []
        while self.tab.allNeg() == False:

            # step 1 : check the last row (on prend le premier)
            toCheck,j = self.tab[n-1],0
            if toCheck[0] < toCheck[1]:
                j= 1

            # step 2 : pivot choice
            temp= []
            for k in range(n-2):
                m = len(self.tab[0])
                if self.tab[k][j] != 0 :
                    temp.append(self.tab[k][m-1]/self.tab[k][j])
                else :
                    temp.append(100000000000000000000)
            min = temp[0]
            for elt in temp :
                if elt < min :
                    min = elt
            index = temp.index(min)
            checkValues.append(j)
            checkValues.append(index)

            # step 3 : pivot
            temp2 = self.tab
            l = temp2.size()
            for k in range(l):
                if k != index :
                    piv = temp2[index][j]
                    beta = temp2[k][j]
                    self.tab.op(1,beta/piv,k,index)
            lp = temp2[index]
            co = lp[j]
            nlp = []
            for elt in lp :
                nlp.append(elt/co)
            self.tab[index]=nlp

        # display solutions

        if len(checkValues) == 2 :
            if checkValues[0] == 0 :
                print("x1 = ",self.tab[checkValues[1]][p-1])
                print("x2 = 0 ")
            elif checkValues[0] == 1:
                print("x1 = 0 ")
                print("x2 = ",self.tab[checkValues[1]][p-1])
        else:
            if checkValues[0] == 0 :
                print("x1 = ",self.tab[checkValues[1]][p-1])
                print("x2 = ",self.tab[checkValues[3]][p-1])
            elif checkValues[0] == 1 :
                print("x1 = ",self.tab[checkValues[3][p-1]])
                print("x2 = ",self.tab[checkValues[1][p-1]])

        print("The max value is : ",-self.tab[n-1][p-1])
        return -self.tab[n-1][p-1]


    def solve(self):
        self.simplex()