from Abstraction.Solver import *
class TableFinale:


        def __init__(self, constraints, gf):
            self.tab = constraints
            self.tab.append(gf)

        """
        :param constraints: an array with the constraints of the problem
        :param gf: the goal function of the problem
        :return: the matrix of the problem
        """

        def __getitem__(self, item):
            return self.tab[item]

        def __setitem__(self, key, value):
            self.tab[key]=value

        def __str__(self):
            return "{}".format(self.tab)

        def size(self):
            return len(self.tab)

        def printTable(self):
            print(' '),
            for i in range(len(self[1])):
                print(i),

            for i, element in enumerate(self):
                print(i, ' '.join(str(element)))


        # normalisation of the constraints
        # A COMPLETER
        def addZeros(self,i,nb):
            l = self.tab[i]
            n = len(l)
            for j in range(nb):
                self.tab[i].insert(n-1,0)

        def normalize(self):
            # add the 1
            n = len(self.tab)
            for i in range(n-1):
                self.tab[i].append(1)

            # add the 0 on the first n-1 lines
            for i in range(n-1):
                self.addZeros(i,n-2)

            # swap the ones

            for i in range(n-1):
                self.tab[i][2],self.tab[i][len(self.tab[i])-1]= self.tab[i][len(self.tab[i])-1],self.tab[i][2]
                self.tab[i][2],self.tab[i][i+2] = self.tab[i][i+2],self.tab[i][2]
            # add the zeros on gf

            for i in range(n-1):
                self.tab[n-1].append(0)

        def normalize_deux_phases(self):
            cpt = 0
            n = len(self.tab)
            m = len(self.tab[0])
            for i in range(n-1):
                if self.tab[i][m-1] < 0:
                    for j in range(cpt):
                        self.tab[i].append(0)
                    self.tab[i].append(1)
                    if(i>0):
                        for j in range(0,i-1):
                            self.tab[j].append(0)
                    cpt += 1
                else:
                    for j in range(cpt):
                        self.tab[i].append(0)

        def allNeg(self):
            outPut = True
            i = 0
            n = len(self.tab)
            m = len(self.tab[n-1])

            while i < m and outPut == True :
                outPut=self.tab[n-1][i] <= 0
                i += 1

            return outPut

        def get_second_membre(self):
            res = []
            i = 0
            n = len(self.tab)
            m = len(self.tab[0])
            while i < m:
                res.append(self.tab[i][m-1])
            return res


        def op(self,alpha,beta,i,j):
            li,lj = self.tab[i],self.tab[j]
            ti,tj,nl = [],[],[]
            for elt in li :
                ti.append(elt*alpha)
            for elt in lj :
                tj.append(elt*beta)
            for elt in range(len(ti)):
                nl.append(ti[elt] - tj[elt])
            self.tab[i]=nl

        def copy(self):
            res = []
            for i in range(len(self.tab)):
                temp = []
                for j in range(len(self.tab[i])):
                    temp.append(self.tab[i][j])
                res.append(temp)
            return res
def main():
    a = [[1,1,4],[1,0,3],[0,1,2]]
    b = [300,100,0]
    ex = TableFinale(a,b)
    sol = Solver(ex)
    sol.simplex()
    sol.tab.printTable()




main()







