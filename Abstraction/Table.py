# -*-coding:utf-8 -*
from __future__ import division


from Abstraction.Constraint import *



class Tab:

    def __init__(self, *tuple):
        self.tab=list(tuple)


    def __getitem__(self, item):
        return self.tab[item]

    def addLine(self,line):
        self.tab.append(line)

    def addGoalFunction(self,a):
        b = a.normalize()
        useless = b.pop()
        del useless
        n = len(self.tab)

        for elt in range(n) :
            b.append(0)

        self.addLine(b)


    def addZeros(self,i,nb):
        l = self.tab[i]
        n = len(l)
        for j in range(nb):
            self.tab[i].insert(n-1,0)

    def addAllZeros(self,nb):
        n = len(self.tab)

        for elt in range(n):
            self.addZeros(elt,nb)

    def swapOne(self):

        n = len(self.tab)

        for i in range(n):
            self.tab[i][2],self.tab[i][i+2] = self.tab[i][i+2],self.tab[i][2]


    def addConstraintStepOne(self,a):
        b = a.normalize()
        useless = b.pop()
        del useless
        b.insert(len(b)-1,1)
        self.addLine(b)

    def __setitem__(self, key, value):
        self.tab[key]=value

    def __str__(self):
        return "{}".format(self.tab)

    def getNbColumns(self):
        return len(self.tab[0])



    # return the dimensions of the tab

    def dimensions(self):
        return (len(self.tab),len(self.tab[0]))

    # do line i = alpha * line i - beta * line j

    def printTable(self):
        print(' '),
        for i in range(len(self[1])):
            print(i),
        print
        for i, element in enumerate(self):
            print(i, ' '.join(str(element)))

    def op(self,alpha,beta,i,j):


        li = self.tab[i]
        lj = self.tab[j]

        ti = []
        tj = []

        for elt in li :
            ti.append(elt*alpha)

        for elt in lj :
            tj.append(elt*beta)

        nl = []

        for elt in range(len(ti)):
            nl.append(ti[elt] - tj[elt])

        self.tab[i]=nl


    def checkLastRow(self):
        n = len(self.tab)
        toCheck = self.tab[n-1]

        j,value = 0,0

        if toCheck[0] > toCheck[1]:
            j,value = 0,toCheck[0]

        else:
            j,value = 1,toCheck[1]

        return j

    def step2(self):
        j = self.checkLastRow()
        temp = []

        n = len(self.tab)

        for k in range(n-1):
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

        return index,j


    def pivot(self):
        i,j= self.step2()

        temp = self.tab
        n = len(temp)

        for k in range(n):
            if k != i :
                piv = temp[i][j]
                beta = temp[k][j]
                self.op(1,beta/piv,k,i)

        lp = temp[i]
        co = lp[j]
        nlp = []

        for elt in lp :
            nlp.append(elt/co)

        self.tab[i]=nlp


    def allCoNul(self):
        outPut = True
        i = 0
        n = len(self.tab)
        m = len(self.tab[n-1])

        while i < m and outPut == True :
            outPut= self.tab[n-1][i] <= 0
            i += 1

        return outPut

    def simplex(self):
        while self.allCoNul() == False :
            self.pivot()

        n = len(self.tab)
        p = len(self.tab[n-1])

        return -self.tab[n-1][p-1]




















