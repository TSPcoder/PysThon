import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2
from matplotlib.figure import Figure

class GraphFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        f = Figure()
        a = f.add_subplot(111)
        a.plot([1, 2, 3, 4])

        canvas = FigureCanvasTkAgg (f, self)