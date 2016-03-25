from __future__ import division
# -*-coding:utf-8 -*

from Abstraction.Constraint import *

class Table2 :

    # constructor & special methods


    def __init__(self, *tuple):
        self.tab=list(tuple)


    def __getitem__(self, item):
        return self.tab[item]

    def __setitem__(self, key, value):
        self.tab[key]=value

    def __str__(self):
        return "{}".format(self.tab)


    # print method

    def printTable(self):
        print(' '),
        for i in range(len(self[1])):
            print(i),
            print
        for i, element in enumerate(self):
            print(i, ' '.join(str(element)))

    # method to do line i = alpha * line i - beta * line j

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

    # method to add a constraint

    def addConstraintStepOne(self,a):
        b = a.normalize()
        useless = b.pop()
        del useless
        b.insert(len(b)-1,1)
        self.tab.append(b)


    # method to "normalize" a table ( add variables )

    def addZeros(self,i,nb):
        l = self.tab[i]
        n = len(l)
        for j in range(nb):
            self.tab[i].insert(n-1,0)

    def addGoalFunction(self,a):
        b = a.normalize()
        useless = b.pop()
        del useless
        n = len(self.tab)

        for elt in range(n) :
            b.append(0)

        self.tab.append(b)

    def normalize(self,b):
        n = len(self.tab)

        # add all Zeros
        for elt in range(n):
            self.addZeros(elt,n-1)

        # swap the ones
        for i in range(n):
            self.tab[i][2],self.tab[i][i+2] = self.tab[i][i+2],self.tab[i][2]

        # add the goal function
        self.addGoalFunction(b)

    # method to check if all the coeffs on the last row are neg

    def allNeg(self):
        outPut = True
        i = 0
        n = len(self.tab)
        m = len(self.tab[n-1])

        while i < m and outPut == True :
            outPut= self.tab[n-1][i] <= 0
            i += 1

        return outPut



    # simplex algorithm

    def simplex2(self,b):
        self.normalize(b)
        n = len(self.tab)
        p = len(self.tab[n-1])
        checkValues = []
        while self.allNeg() == False:

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
            l = len(temp2)
            for k in range(l):
                if k != index :
                    piv = temp2[index][j]
                    beta = temp2[k][j]
                    self.op(1,beta/piv,k,index)
            lp = temp2[index]
            co = lp[j]
            nlp = []
            for elt in lp :
                nlp.append(elt/co)
            self.tab[index]=nlp

        # display solutions

        if len(checkValues) == 2 :
            if checkValues[0] == 0 :
                print("x1 = ",self[checkValues[1]][p-1])
                print("x2 = 0 ")
            elif checkValues[0] == 1:
                print("x1 = 0 ")
                print("x2 = ",self[checkValues[1]][p-1])
        else:
            if checkValues[0] == 0 :
                print("x1 = ",self[checkValues[1]][p-1])
                print("x2 = ",self[checkValues[3]][p-1])
            elif checkValues[0] == 1 :
                print("x1 = ",self[checkValues[3][p-1]])
                print("x2 = ",self[checkValues[1][p-1]])


        return -self.tab[n-1][p-1]




















