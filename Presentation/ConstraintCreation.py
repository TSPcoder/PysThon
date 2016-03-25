# Autor : Aymeric ALOUGES
import string
from tkinter import *

#Creation of our window

window = Tk()

Label(window, text = 'Nouvelle Contrainte').grid(row =1, column =1, columnspan =2, padx =10, pady =5)
nom = StringVar()
nom.set("Nom de la contrainte")
Entry(window, textvariable=nom, width=30).grid(row =2, column =1, columnspan =2, padx =10, pady =5)

Label(window, text = 'Coéficient de x').grid(row =3, column =1, padx =10, pady =5,stick = E)
coef1 = StringVar()
coef1.set("")
Entry(window, width=10).grid(row =3, column =2, padx =10, pady =5)

Label(window, text = 'Coéficient de y').grid(row =4, column =1, padx =10, pady =5,stick = E)
coef2 = StringVar()
coef2.set("")
Entry(window, width=10).grid(row =4, column =2, padx =10, pady =5)

Label(window, text = 'opérateur').grid(row =5, column =1, padx =10, pady =5,stick = E)
operator = StringVar()
operator.set("")
Entry(window, width=10).grid(row =5, column =2, padx =10, pady =5)

Label(window, text = 'constante').grid(row =6, column =1, padx =10, pady =5,stick = E)
constant = StringVar()
constant.set("")
Entry(window, width=10).grid(row =6, column =2, padx =10, pady =5)

Button(window, text ='Valider').grid(row =7, column =1, padx =10, pady =5)
Button(window, text ='Annuler').grid(row =7, column =2, padx =10, pady =5)
# Tkinter loop
window.mainloop()