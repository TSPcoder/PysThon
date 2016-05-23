
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
            print(table[0])
            print(table[1])
            print(table[2])
            print(table[3])
            X = np.array([table[0],table[1]])
            Y = np.array([table[2],table[3]])
            ax.plot(X,Y)
        return ax


def draw_figure(canvas,figure, loc=(0, 0)):
    """ Draw a matplotlib figure onto a Tk canvas

        loc: location of top-left corner of figure on canvas in pixels.

        Inspired by matplotlib source: lib/matplotlib/backends/backend_tkagg.py
        """
    figure_canvas_agg = FigureCanvasAgg(figure)
    figure_canvas_agg.draw()
    figure_x, figure_y, figure_w, figure_h = figure.bbox.bounds
    figure_w, figure_h = int(figure_w), int(figure_h)
    photo = tk.PhotoImage(master=canvas, width=figure_w, height=figure_h)

    # Position: convert from top-left anchor to center anchor
    canvas.create_image(loc[0] + figure_w/2, loc[1] + figure_h/2, image=photo)

    # Unfortunatly, there's no accessor for the pointer to the native renderer
    tkagg.blit(photo, figure_canvas_agg.get_renderer()._renderer, colormode=2)

    # Return a handle which contains a reference to the photo object
    # which must be kept live or else the picture disappears
    return photo




'''
# Create a canvas
w, h = 300, 300
window = tk.Tk()
window.title("A figure in a canvas")
canvas = tk.Canvas(window, width=w, height=h)
canvas.pack()

# Generate some example data
#X = np.linspace(0, 2.0*3.14, 50)
#Y = np.sin(X)

X = np.array([0,1])
Y = np.array([0,1])
X1 = np.array([0,1])
Y1 = np.array([1,0])

# Create the figure we desire to add to an existing canvas
fig = mpl.figure.Figure(figsize=(3, 3))
ax = fig.add_axes([0, 0, 1, 1])
#ax.plot(X, Y)
#ax.plot(X1,Y1)
plt.plot(X,Y)
plt.show()


# Keep this handle alive, or else figure will disappear
#fig_photo = draw_figure(canvas, fig)

#fig_w, fig_h = fig_photo.width(), fig_photo.height()

# Add more elements to the canvas, potentially on top of the figure
#canvas.create_line(200, 50, fig_x + fig_w / 2, fig_y + fig_h / 2)
#canvas.create_text(200, 50, text="Zero-crossing", anchor="s")

# Let Tk take over
tk.mainloop()

'''
