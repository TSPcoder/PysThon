# -*-coding:utf-8 -*

from Abstraction.Goalfunction import *
# from Abstraction.Table import *
from Abstraction.Table2 import *
from Abstraction.TableFinale import *
from Abstraction.Solver import *


def main():

    a = TableFinale([[1,1,6,True],[0,1,3,True],[1,1,1,False]],[1,2,0,True])
    #a = TableFinale([[1, 1, 6, False], [1, 0, 4, False], [0, 1, 3, True]], [5, 7, 0, True])
    #a = TableFinale([[1,1,4],[1,0,3],[0,1,2]],[300,100,0])
    #a.normalizeGen()
    #a.printTable()

    #a.normalizeGen()
    #a.printTable()

    s = Solver(a)
    s.deuxPhases()
    s.printTable()





main()
