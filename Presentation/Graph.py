
# Autor : Aymeric ALOUGES

from tkinter import *
from Abstraction.Constraint import *

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import sys
if sys.version_info[0] < 3:
    import Tkinter as tk
else:
    import tkinter as tk
import matplotlib.backends.tkagg as tkagg
from matplotlib.backends.backend_agg import FigureCanvasAgg


class Graph(Canvas):
    "Canevas that build the geometric aspect of the problem"
    def __init__(self, boss =None, width=200, height=150):
         # constructor
        Canvas.__init__(self)

        # de la classe parente
        self.configure(width=width, height=height, bg='white')

        # mémorisation
        self.width, self.height = width, height



    def draw_figure(self,figure, loc=(0, 0)):
        """ Draw a matplotlib figure onto a Tk canvas

        loc: location of top-left corner of figure on canvas in pixels.

        Inspired by matplotlib source: lib/matplotlib/backends/backend_tkagg.py
        """
        figure_canvas_agg = FigureCanvasAgg(figure)
        figure_canvas_agg.draw()
        figure_x, figure_y, figure_w, figure_h = figure.bbox.bounds
        figure_w, figure_h = int(figure_w), int(figure_h)
        photo = tk.PhotoImage(master=self, width=figure_w, height=figure_h)

        # Position: convert from top-left anchor to center anchor
        self.create_image(loc[0] + figure_w/2, loc[1] + figure_h/2, image=photo)

        # Unfortunatly, there's no accessor for the pointer to the native renderer
        tkagg.blit(photo, figure_canvas_agg.get_renderer()._renderer, colormode=2)

        # Return a handle which contains a reference to the photo object
        # which must be kept live or else the picture disappears
        return photo

    def draw_constraint(self, constraint,figure):
        table = constraint.intersection()
        figure.plot([table[0], table[1]], [table[2],table[3]], 'r-', lw=2)

    def draw_constraints(self, constraints,figure):
        xmax = 0
        ymax = 0
        for c in constraints:
            print(type(c))
            table = c.intersection()
            if table[1]>xmax :
                xmax = table[1]
            if table[2]>ymax :
                ymax = table[2]
        ax = figure.add_axes([0,0,xmax,ymax])

        for c in constraints :
            table = c.intersection()
            ax.plot(table[0], table[1], table[2],table[3])
        return ax
