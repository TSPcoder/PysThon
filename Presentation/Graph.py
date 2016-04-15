
# Autor : Aymeric ALOUGES

from tkinter import *
from Abstraction.Constraint import *

class Graph(Canvas):
  "Canevas that build the geometric aspect of the problem"
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
