
# Autor : Aymeric ALOUGES

from tkinter import *
from Abstraction.Constraint import *


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



def draw_figure(canvas, figure, loc=(0, 0)):
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
w, h = 300, 200
window = tk.Tk()
window.title("A figure in a canvas")
canvas = tk.Canvas(window, width=w, height=h)
canvas.pack()

# Generate some example data
X = np.linspace(0, 2.0*3.14, 50)
Y = np.sin(X)

# Create the figure we desire to add to an existing canvas
fig = mpl.figure.Figure(figsize=(2, 1))
ax = fig.add_axes([0, 0, 1, 1])
ax.plot(X, Y)

# Keep this handle alive, or else figure will disappear
fig_x, fig_y = 100, 100
fig_photo = draw_figure(canvas, fig, loc=(fig_x, fig_y))
fig_w, fig_h = fig_photo.width(), fig_photo.height()

# Add more elements to the canvas, potentially on top of the figure
canvas.create_line(200, 50, fig_x + fig_w / 2, fig_y + fig_h / 2)
canvas.create_text(200, 50, text="Zero-crossing", anchor="s")

# Let Tk take over
tk.mainloop()

'''
'''
  def __init__(self, boss =None, width=200, height=150):
    #build the axis

    # constructor
    Canvas.__init__(self)

    # de la classe parente
    self.configure(width=width, height=height, bg='white')

    # mémorisation
    self.width, self.height = width, height
    # tracé des axes de référence :
    # axe X
    self.create_line(10, height-5, width-10, height-5, arrow=LAST)
    # axe Y
    self.create_line(10, height-5, 10, 5, arrow=LAST)
    # tracé d'une échelle avec 8 graduations :
    step_x = (width-25)/8.      # intervalles de l'échelle horizontale
    for t in range(1, 9):
        stx = 10 + t*step_x	    # +10 pour partir de l'origine
        self.create_line(stx, height-2.5, stx, height-7.5)
    step_y = (height-25)/8.
    for t in range(1, 9):
        sty = 10 + t*step_y	    # +10 pour partir de l'origine
        self.create_line(7.5, sty, 12.5, sty)

  def drawLine(self, c1 = 2, c2 = 2, cte = 2):
     # draw the straigt line corresponding to the constraint c1*X1 + c2*x2 =< cte
    if c1*c2 != 0 :
        self.create_line(cte / c1, self.height - 5, cte/c2, 5)
'''