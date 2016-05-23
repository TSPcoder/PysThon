import matplotlib as mpl
import tkinter as tk

from Abstraction.Constraint import Constraint
from Presentation.ConstraintCreation import ConstraintCreation
from Presentation.FunctionCreation import FunctionCreation

mpl.use("TkAgg")


class WindowBis(tk.Tk):
    def __init__(self):
        """Builds the whole window with two main Frames, the left one contains buttons and the let one contains the graph"""
        tk.Tk.__init__(self)

        self.gf = None
        self.constraints = []

        "Creating right frame"
        self.build_right_frame()

        "Creating left frame"
        self.left_frame = tk.Frame(self)
        self.left_frame.pack(side = 'left')
        self.build_left_frame()

        self.mainloop()

    def set_gf(self, gf):
        self.gf = gf

    "---------------Main Frames---------------------------------------------------------"

    def build_right_frame(self):
        """Builds the right frame of the window that contains the graph"""
        pass

    def build_left_frame(self):
        "Builds the left frame at initialization"
        self.button_frame = tk.Frame(self.left_frame)
        self.button_frame.pack()
        self.build_button_frame()

        self.build_table_frame()

    "------------------------------Left Frame-----------------------------------------"

    def build_button_frame(self):
        "Builds the frame that contains the buttons at initialization"

        "Goal finciton frame"
        self.gf_frame = tk.Frame(self.button_frame)
        self.gf_frame.pack(side = "top")
        self.build_gf_frame_unfilled()

        "Constraints frame"
        self.constraints_frame = tk.Frame(self.button_frame)
        self.constraints_frame.pack()
        self.build_cons_frame()

        "Table Frame"
        self.table_frame = tk.LabelFrame(self.button_frame, borderwidth = 0,
                                         relief = tk.GROOVE, text = "Tableau")
        self.table_frame.pack()
        self.build_table_frame()

    "-----------------------------------------Goal Function Frame--------------------"

    def build_gf_frame_unfilled(self):
        self.button_gf = tk.Button(self.gf_frame, text='Fonction objectif')
        self.button_gf.bind('<Button-1>', self.action_button_gf)
        self.button_gf.pack(side = "top")
        self.left_frame.pack(side = "top")

    def action_button_gf(self, event):
        FunctionCreation(self)

    def build_gf_frame_filled(self):
        self.button_gf.destroy()
        self.label_gf = tk.Label(self.gf_frame, text = self.gf.__str__())
        self.label_gf.pack(side = "left")
        self.button_edit_gf = tk.Button(self.gf_frame, text = "Edit")
        self.button_edit_gf.bind("<Button-1>", self.edit_gf)
        self.button_edit_gf.pack(side = "right")

    def edit_gf(self, event):
        self.label_gf.destroy()
        self.button_edit_gf.destroy()
        self.build_gf_frame_unfilled()

    "--------------------------------------------Constraints Frame-----------------------"

    def build_cons_frame(self):
        self.label_cons = tk.Label(self.constraints_frame, text = "Contraintes")
        self.label_cons.pack(side = "top")

        self.cons_buttons_frame = tk.Frame(self.constraints_frame)
        self.cons_buttons_frame.pack(side = "right")
        self.build_cons_buttons_frame()

        self.list_constraints = tk.Listbox(self.constraints_frame)
        self.list_constraints.pack()

    def build_cons_buttons_frame(self):
        self.button_add_cons = tk.Button(self.cons_buttons_frame, text = "Add")
        self.button_add_cons.bind('<Button-1>', self.add_button_action)
        self.button_add_cons.pack()

        self.button_del_cons = tk.Button(self.cons_buttons_frame, text = "Del")
        self.button_del_cons.bind('<Button-1>', self.del_button_action)
        self.button_del_cons.pack()

    def add_button_action(self, event):
        ConstraintCreation(self)

    def add_constraint(self, constraint):
        print(constraint.toString())
        n = len(self.constraints) + 1
        self.list_constraints.insert(n, constraint.toString())
        if constraint.operatorConstraint == '=':
            constraint1 = Constraint(constraint.coeffsConstraint, '<=').normalize()
            constraint2 = Constraint(constraint.coeffsConstraint, '>=').normalize()
            self.constraints.append(constraint1)
            self.constraints.append(constraint2)
        else:
            #constraint = constraint.normalize()
            self.constraints.append(constraint)

    def del_button_action(self, event):
        ind = self.list_constraints.curselection()
        self.list_constraints.delete(ind, ind)
        self.constraints.remove(ind)

    "------------------------------------------Table Fraùe----------------------------"

    def build_table_frame(self):
        for line in range(5):
            for column in range(5):
                tk.Label(self.table_frame, text = 'L%s-C%s' % (line, column), relief = tk.GROOVE,
                         borderwidth = 5).grid(row = line, column = column)
