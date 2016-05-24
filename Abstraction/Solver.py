
class Solver:

    def __init__(self, table):
        """
        :param table: initial table of the problem
        :return:
        """
        self.tab = table

    def printTable(self):
        print(' '),
        for i in range(len(self.tab[1])):
            print(i),
            print
        for i, element in enumerate(self.tab):
            print(i, ' '.join(str(element)))

    def algo(self):
        #----- premiere étape -----
        # check de b
        b = self.tab.get_second_membre()
        cpt = 0
        i = 0
        temp = True
        while i < len(b):
            if(b[i] < 0):
                cpt += 1
                temp = False
        if temp:
            self.simplex()
        else:
            newTab = self.tab.copy()
            newTab.normalize_deux_phases()




    def simplex(self):

        tabChang = []

        comptdep = 0
        for i in range(self.tab.size()-1):
            if self.tab[i][len(self.tab[i])-1] == False :
                comptdep = comptdep+1


           # self.tab.normalize()

        #self.tab.normalizeGen()



        self.tab.normalize()
        n = self.tab.size()
        checkValues = []
        while not self.tab.allNeg():

            # step 1 : check the last row (on prend le premier)
            # toCheck,j = self.tab[n-1],0
            #if toCheck[0] < toCheck[1]:
            #   j= 1

            m=len(self.tab[0])
            n=self.tab.size()
            j=0
            max=-1000000
            for i in range (m-1):
                if self.tab[n-1][i]>max :
                    max=self.tab[n-1][i]
                    j=i





            # step 2 : pivot choice
            temp= []
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

            tabChang.append([index, j])

        self.printTable()
        print(self.tab)

        """

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
        return -self.tab[n-1][p-2]
        """


    def deuxPhases(self):

        n = self.tab.size()
        goalf = self.tab[n-1].copy()


        comptdep = 0
        for i in range(self.tab.size() - 1):
            if self.tab[i][len(self.tab[i]) - 1] == False:
                comptdep = comptdep + 1

        self.tab.normalizeGen()

        tabChang = self.simplex()





        n=self.tab.size()
        for i in range (comptdep) :
            for j in range (n) :
                m = len(self.tab[j])
                del self.tab[j][m-2]



        tabPos = []
        tabPos.append(-1)
        tabPos.append(-1)

        for i in range (len(tabChang)) :
            tabPos[tabChang[i][0]] = tabChang[i][1]

        ck = []
        n=self.tab.size()
        m=len(self.tab[0])
        for i in range(n-1):
            ck.append(0)

        for i in range (len(tabPos)) :
            if i>=0 :
                ck[tabPos[i]] = goalf[i]





        for c in range (m):
            somme = 0
            for i in range (n-1):
                somme = somme + ck[i] * (self.tab[i][c])
            self.tab[n - 1][c] = (-1)*somme

        self.tab[n-1][0]=0
        self.tab[n - 1][1] = 0





        self.simplex()












    def solve(self):
        return self.simplex()

