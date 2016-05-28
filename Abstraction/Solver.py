
class Solver:

    def __init__(self, table):
        """
        :param table: initial table of the problem
        :return:
        """
        self.tab = table

    def print_table(self):
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
            new_tab = self.tab.copy()
            new_tab.normalize_deux_phases()

    def simplex(self):
        tab_chang = []
        comptdep = 0
        for i in range(self.tab.size() - 1):
            if not self.tab[i][len(self.tab[i])-1] :
                comptdep += 1
            # self.tab.normalize()
        #self.tab.normalizeGen()

        self.tab.normalize()
        n = self.tab.size()
        check_values = []
        while not self.tab.all_neg():
            # step 1 : check the last row (on prend le premier)
            # toCheck,j = self.tab[n-1],0
            #if toCheck[0] < toCheck[1]:
            #   j= 1

            m = len(self.tab[0])
            n = self.tab.size()
            j = 0
            max = -1000000
            for i in range (m-1):
                if self.tab[n-1][i] > max :
                    max = self.tab[n-1][i]
                    j = i

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
            check_values.append(j)
            check_values.append(index)

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
            self.tab[index] = nlp

            tab_chang.append([index, j])

        self.print_table()
        print(self.tab)

        """
        # display solutions


        if len(check_values) == 2 :
            if check_values[0] == 0 :
                print("x1 = ",self.tab[check_values[1]][p-1])
                print("x2 = 0 ")
            elif check_values[0] == 1:
                print("x1 = 0 ")
                print("x2 = ",self.tab[check_values[1]][p-1])
        else:
            if check_values[0] == 0 :
                print("x1 = ",self.tab[check_values[1]][p-1])
                print("x2 = ",self.tab[check_values[3]][p-1])
            elif check_values[0] == 1 :
                print("x1 = ",self.tab[check_values[3][p-1]])
                print("x2 = ",self.tab[check_values[1][p-1]])

        print("The max value is : ",-self.tab[n-1][p-1])
        return -self.tab[n-1][p-2]
        """

    def deux_phases(self):
        n = self.tab.size()
        goal_func = self.tab[n-1].copy()
        comptdep = 0
        for i in range(self.tab.size() - 1):
            l = self.tab[i]
            if not l [len(l) - 1]:
                comptdep += 1
        self.tab.normalize_gen()
        tabChang = self.simplex()

        n = self.tab.size()
        for i in range (comptdep) :
            for j in range (n) :
                m = len(self.tab[j])
                del self.tab[j][m-2]

        tab_pos = []
        tab_pos.append(-1)
        tab_pos.append(-1)

        for i in range (len(tabChang)) :
            tab_pos[tabChang[i][0]] = tabChang[i][1]

        ck = []
        n = self.tab.size()
        m = len(self.tab[0])
        for i in range(n-1):
            ck.append(0)

        for i in range (len(tab_pos)) :
            if i >= 0 :
                ck[tab_pos[i]] = goal_func[i]

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

