import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2
from matplotlib.figure import Figure

class GraphFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        f = Figure(figsize = (5, 5), dpi = 100)
        a = f.add_subplot(111)
        xmax = 0
        ymax = 0
        for c in parent.constraints:
            table = c.intersection()
            if table[1] > xmax:
                xmax = table[1]
            if table[2] > ymax:
                ymax = table[2]
        a.axis([0, xmax, 0, ymax])
        for c in parent.constraints:
            coefs = c.coeffsConstraint
            if coefs[0] != 0 and coefs[1] != 0:
                a.plot([0, xmax], [ymax, 0])
            elif coefs[0] == 0 and coefs[1] != 0:
                a.plot([0, xmax],[coefs[2]/coefs[1], coefs[2]/coefs[1]])
            elif coefs[0] != 0 and coefs[1] == 0:
                a.plot([coefs[2]/coefs[0], coefs[2]/coefs[0]], [0,ymax])

        #a.plot([1, 2, 3, 4])

        canvas = FigureCanvasTkAgg (f, self)
        canvas.show()
        canvas.get_tk_widget().pack(padx = 3, pady = 2, fill = tk.BOTH, expand = True)
'''
    def draw_figure(self, figure):
        xmax = 0
        ymax = 0
        for c in self.constraints:
            print(type(c))
            table = c.intersection()
            if table[1]>xmax:
                xmax = table[1]
            if table[2]>ymax:
                ymax = table[2]
        plt.axis([0,xmax, 0, ymax])
        for c in self.constraints:
            coefs = c.coeffsConstraint
            if coefs[0] != 0 and coefs[1] != 0:
                plt.plot([0, xmax], [ymax, 0])
            elif coefs[0] == 0 and coefs[1] != 0:
                plt.plot([0, xmax],[coefs[2]/coefs[1], coefs[2]/coefs[1]])
            elif coefs[0] != 0 and coefs[1] == 0:
                plt.plot([coefs[2]/coefs[0],coefs[2]/coefs[0]], [0,ymax])
        plt.show()
        '''