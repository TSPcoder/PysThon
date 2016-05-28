from Abstraction.Solver import *


class Table:
        def __init__(self, constraints, gf):
            self.tab = list(constraints)
            self.tab.append(gf)

        """
        :param constraints: an array with the constraints of the problem
        :param gf: the goal function of the problem
        :return: the matrix of the problem
        """

        def __getitem__(self, item):
            return self.tab[item]

        def __setitem__(self, key, value):
            self.tab[key] = value

        def __str__(self):
            return "{}".format(self.tab)

        def size(self):
            return len(self.tab)

        def print_table(self):
            print(' '),
            for i in range(len(self[1])):
                print(i),

            for i, element in enumerate(self):
                print(i, ' '.join(str(element)))

        # normalisation of the constraints
        def add_zeros(self, i, nb):
            l = self.tab[i]
            n = len(l)
            for j in range(nb):
                self.tab[i].insert(n-1,0)

        def normalize(self):
            # add the 1
            n = len(self.tab)
            for i in range(n):
                line = self.tab[i]
                m = len(line)
                del line[n-1]

            for i in range(n-1):
                self.tab[i].append(1)

            # add the 0 on the first n-1 lines
            for i in range(n-1):
                self.add_zeros(i, n - 2)

            # swap the ones
            for i in range(n-1):
                line = self.tab[i]
                l = len(line)
                line[2], line[l - 1] = line[l-1], line[2]
                line[2], line[i+2] = line[i+2], line[2]
            # add the zeros on gf

            for i in range(n-1):
                self.tab[n-1].append(0)

        def normalize_gen(self):
            # add the 1
            n = len(self.tab)
            m = len(self.tab[0])
            cmpt = []
            for i in range(n - 1):
                line = self.tab[i]
                m = len(line)
                if not line[m-1]:
                    line.append(-1)
                    cmpt.append(i)
                else:
                    line.append(1)

            # add the 0 on the first n-1 lines
            for i in range(n - 1):
                    self.add_zeros(i, n - 1 + len(cmpt) - 1)

            # remove the boolean
            for i in range(n):
                del self.tab[i][3]

            # swap the ones
            for i in range(n - 1):
                line = self.tab[i]
                l = len(self.tab[i])
                line[2], line[l - 1] = line[l - 1], line[2]
                line[2], line[i + 2] = line[i + 2], line[2]

            #add the ones on the second diagonal
            for i in range(len(cmpt)) :
                self.tab[cmpt[i]] [2 + (n-1) + i] = 1

            # add the zeros on gf
            n = len(self.tab)
            m = len(self.tab[0])
            for i in range(m-3):
               self.tab[n - 1].append(0)

            nbreVarArt = len(cmpt)
            ck = []
            for i in range(n-1) :
                ck.append(0)
            for i in range(len(cmpt)) :
                ck[cmpt[i]] = 1

            #set the goal function

            for c in range (m) :
                somme = 0
                for i in range (n-1) :
                    somme = somme + ck[i]*(self.tab[i][c])
                self.tab[n-1][c] = somme

            for c in range (len(cmpt)) :
                self[n-1][2+(n-1)+c]=0

        def normalize_deux_phases(self):
            self.normalize()
            cpt = 0
            n = len(self.tab)
            m = len(self.tab[0])
            for i in range(n-1):
                line = self.tab[i]
                if line[m-1] < 0:
                    line.append(1)
                    cpt += 1
                else:
                    line.append(0)
            for j in range(n-1):
                for i in range(cpt-1):
                    self.tab[j].append(0)

        def all_neg(self):
            output = True
            i = 0
            n = len(self.tab)
            m = len(self.tab[n-1])
            while i < m and output:
                output = self.tab[n-1][i] <= 0
                i += 1
            return output

        def get_second_membre(self):
            res = []
            i = 0
            n = len(self.tab)
            m = len(self.tab[0])
            while i < m:
                res.append(self.tab[i][m-1])
            return res

        def op(self,alpha,beta,i,j):
            li, lj = self.tab[i], self.tab[j]
            ti, tj, nl = [], [], []
            for elt in li :
                ti.append(elt * alpha)
            for elt in lj :
                tj.append(elt * beta)
            for elt in range(len(ti)):
                nl.append(ti[elt] - tj[elt])
            self.tab[i] = nl

        def copy(self):
            res = []
            for i in range(len(self.tab)):
                line = self.tab[i]
                temp = []
                for j in range(len(line)):
                    temp.append(line[j])
                res.append(temp)
            return res








