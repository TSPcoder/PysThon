
class Solver:

    def __init__(self, table):
        """
        :param table: initial table of the problem
        :return:
        """
        self.tab = table

    def simplex(self):
        """
        simplex method, modify self.tab
        """
        # A COMPLETER