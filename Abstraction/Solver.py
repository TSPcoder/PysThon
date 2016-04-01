# -*-coding:utf-8 -*
from Constraint import *
from Goalfunction import *
from Table import *
from Interaction import *

class Solver :

    def __init__(self,a):
        self.tabBegin=a
        self.tabUsed =a




    def op(self,alpha,beta,i,j):


        li = self.tabUsed[i]
        lj = self.tabUsed[j]

        ti = []
        tj = []

        for elt in li :
            ti.append(elt*alpha)

        for elt in lj :
            tj.append(elt*beta)

        nl = []

        for elt in range(len(ti)):
            nl.append(ti[elt] - tj[elt])

        self.tabUsed[i]=nl


    def checkLastRow(self):
        n = len(self.tabUsed)
        toCheck = self.tabUsed[n]

        j,value = 0,0

        if toCheck[0] > toCheck[1]:
            j,value = 0,toCheck[0]

        else:
            j,value = 1,toCheck[1]

        return j,value

    def step2(self):
        j,value = self.checkLastRow()
        temp = []
        theTab=self.tabUsed
        n = len(theTab)

        for k in range(n):
            m = len(theTab[j])
            temp.append(theTab[m]/theTab[k])

        min = temp[0]

        for elt in temp :
            if elt < min :
                min = elt

        index = temp.index(min)

        return index,j


    def pivot(self):
        i,j= self.step2()

        temp = self.tabUsed
        n = len(temp)

        for k in range(n):
                piv = temp[i][j]
                beta = temp[k][j]
                self.op(1,beta/piv,k,i)

        lp = temp[i]
        co = lp[j]
        nlp = []

        for elt in lp :
            nlp.append(elt/co)

        self.tabUsed[i]=nlp


    def allCoNul(self):
        outPut = True
        i = 0
        n = len(self.tabUsed)
        m = len(self.tabUsed[n])

        while i < n and outPut == True :
            outPut = self.tabUsed[n][i] <= 0
            i += 1

        return outPut

    def simplex(self):
        while self.allCoNul() == False :
            self.pivot()

        n = len(self.tabUsed)
        m = len(self.tabUsed[n])

        return -self.tabUsed[n][m]











