# Autor : Aymeric ALOUGES

from tkinter import *
from Abstraction.Goalfunction import *
from tkinter.messagebox import *

#Creation of our window


class FunctionCreationWindow(Tk):
    def __init__(self, win, bg = "#909090", bd = 1):

        self.win = win
        self.check_button_image = PhotoImage(file = "Images/buttoncheck.png")
        self.del_button_image = PhotoImage(file = "Images/buttondel.png")

        Tk.__init__(self)
        self.configure(bg = bg)

        self.frame = Frame(self, bg = "#a0a0a0", bd = bd, relief = SUNKEN)
        self.frame.pack(fill = "x", padx = 3, pady = 3)
        Label(self.frame, text = 'Fonction objectif : ', bg = "#a0a0a0", bd = bd, relief = SUNKEN).\
            pack(side = "top", padx = 3, pady = 3, fill = "x")
        self.middle_frame = Frame(self.frame, bg = bg)
        self.middle_frame.pack()
        self.label_frame = Frame(self.middle_frame, bg = bg, bd = bd, relief = RAISED)
        self.label_frame.pack(side = "left", fill = "y", padx = 3, pady = 3)
        self.entry_frame = Frame(self.middle_frame, bg = bg, bd = bd, relief = RAISED)
        self.entry_frame.pack(side = "right", fill = "y", padx = 3, pady = 3)
        self.button_frame = Frame(self.frame, bg = bg, bd = bd, relief = RAISED)
        self.button_frame.pack(side = "bottom", padx = 3, pady = 3)

        Label(self.label_frame, text = 'Coéficient de x1 :', bg = "#a0a0a0", bd = bd, relief = SUNKEN).pack(padx = 3, pady = 3)
        coef1 = StringVar()
        coef1.set("")
        self.c1 = Entry(self.entry_frame, bd = bd, relief = SUNKEN, textvariable=coef1,width=10)
        self.c1.pack(padx = 3, pady = 3)

        Label(self.label_frame, text = 'Coéficient de x2 :', bg = "#a0a0a0", bd = bd, relief = SUNKEN).pack(padx = 3, pady = 3)
        coef2 = StringVar()
        coef2.set("")
        self.c2 = Entry(self.entry_frame, textvariable = coef2,width=10)
        self.c2.pack(padx = 3, pady = 3)

        Label(self.label_frame, text = 'Constante :', bg = "#a0a0a0", bd = bd, relief = SUNKEN).pack(padx = 3, pady = 3, fill = "x")
        constant = StringVar()
        constant.set("")
        self.cst = Entry(self.entry_frame, textvariable = constant,width=10)
        self.cst.pack(padx = 3, pady = 3)

        Label(self.label_frame, text = 'Opérateur :', bg = "#a0a0a0", bd = bd, relief = SUNKEN).pack(padx = 3, pady = 3, fill = "x")
        operator = StringVar()
        operator.set("")
        self.op = Entry(self.entry_frame, textvariable = operator, width=10)
        self.op.pack(padx = 3, pady = 3)
        self.build_buttons()
        self.mainloop()

    def build_buttons(self):
        self.v_button = Button(self.button_frame, text = "Ajouter", bg = "#a0a0a0")
        self.v_button.pack(side = "left", padx = 3, pady = 3)
        self.v_button.bind('<Button-1>', self.validate)
        self.v_button.bind('<Return>', self.validate)

        self.x_button = Button(self.button_frame, text = "Annuler", bg = "#a0a0a0",
               command = self.destroy)
        self.x_button.pack(side = "right", padx = 3, pady = 3)
        # Tkinter loop

    def str_to_int(self, a):
        try:
            return int(a)
        except:
            print("l'argument n'est pas du bon type")
            return a

    def str_to_float(self, a):
        try:
            return float(a)
        except:
            print("l'argument n'est pas du bon type")
            return a

    def validate(self, event):
        temp = self.op.get()
        if type(self.str_to_int(self.c1.get())) != int:
            # message d'alerte : c1 mal saisi
            showwarning('Attention !', 'Le premier coefficient est mal saisi.')
            print("c1 est mal saisi")
        elif type(self.str_to_int(self.c2.get())) != int:
            # message d'alerte : c2 est mal saisi
            showwarning('Attention !', 'Le deuxième coefficient est mal saisi.')
            print("c2 esl mal saisi")
        elif temp != "min" and temp != "max":
            # message d'alerte : op est mal saisi
            showwarning('Attention !', "L'opérateur est mal saisi.")
            print("op est mal saisi")
        elif type(self.str_to_int(self.cst.get())) != int:
            # message d'alerte : cst est mal saisi
            showwarning('Attention !', 'La constante est mal saisie.')
            print("cst est mal saisi")
        else:
            gf = GoalFunction([self.str_to_int(self.c1.get()), self.str_to_float(self.c2.get()), self.str_to_float(self.cst.get())],
                              self.op.get())
            self.win.set_gf(gf)
            self.win.left_frame.build_gf_frame_filled()
            self.destroy()