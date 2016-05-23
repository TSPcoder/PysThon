import matplotlib as mpl
import tkinter as tk

from Abstraction.Constraint import Constraint
from Abstraction.Solver import Solver
from Abstraction.TableFinale import TableFinale
from Presentation.ConstraintCreation import ConstraintCreation
from Presentation.FunctionCreation import FunctionCreation
from Presentation.GraphFrame import GraphFrame

mpl.use("TkAgg")


class WindowBis(tk.Tk):
    def __init__(self):
        """Builds the whole window with two main Frames, the left one contains buttons and the let one contains the graph"""
        tk.Tk.__init__(self)

        self.gf = None
        self.constraints = []

        "Creating right frame"
        self.right_frame = GraphFrame(self, None) #pas de controleur pour l'instant
        self.build_right_frame()
        self.right_frame.pack(side = 'right')

        "Creating left frame"
        self.left_frame = tk.Frame(self)
        self.build_left_frame()
        self.left_frame.pack(side = 'left')

        self.mainloop()

    def set_gf(self, gf):
        self.gf = gf

    "---------------Main Frames---------------------------------------------------------"

    def build_left_frame(self):
        "Builds the left frame at initialization"

        "Problem setting frame"
        self.button_frame = tk.Frame(self.left_frame)
        self.build_button_frame()
        self.button_frame.pack()

        "Solve Button Frame"
        self.solve_butt_frame = tk.Frame(self.left_frame)
        self.build_solve_button_frame()
        self.solve_butt_frame.pack(pady = 10, fill = tk.BOTH)

        "Table Frame"
        self.table_frame = tk.LabelFrame(self.left_frame, borderwidth = 0,
                                         relief = tk.GROOVE, text = "Tableau")
        self.build_table_frame()
        self.table_frame.pack()


    def build_right_frame(self):
        """Builds the right frame of the window that contains the graph"""

        #!!!!!!!!!!!!faut créer le Canvas ici
        pass


    "------------------------------Left Frame-----------------------------------------"
    "----------------------------------------Setting Buttons Frame--------------------"

    def build_button_frame(self):
        "Builds the frame that contains the buttons at initialization"

        "Goal funciton frame"
        self.gf_frame = tk.Frame(self.button_frame)
        self.build_gf_frame_unfilled()
        self.gf_frame.pack(side = "top")

        "Constraints frame"
        self.constraints_frame = tk.Frame(self.button_frame)
        self.build_cons_frame()
        self.constraints_frame.pack()

    "-----------------------------------------Goal Function Frame--------------------"

    def build_gf_frame_unfilled(self):
        self.button_gf = tk.Button(self.gf_frame, text='Fonction objectif')
        self.button_gf.bind('<Button-1>', self.action_button_gf)
        self.button_gf.pack(side = "top")

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
        ind = self.list_constraints.curselection().__getitem__(0)
        if isinstance(ind, int) :
            print (ind)
            self.list_constraints.delete(ind)
            self.constraints.pop(ind)

    "--------------------Solve Button Frame------------------------------------"

    def build_solve_button_frame(self):
        self.solve_butt = tk.Button(self.solve_butt_frame, text = "Solve", bg = "red", width = 27)#a changer
        self.solve_butt.bind("<Button-1>", self.solve)
        self.solve_butt.pack()

    "---------------------Table Frame------------------------------------------"

    def build_table_frame(self):
        for line in range(5):
            for column in range(5):
                tk.Label(self.table_frame, text = 'L%s-C%s' % (line, column), relief = tk.GROOVE,
                         borderwidth = 5).grid(row = line, column = column)



    "--------------Right Frame-------------------------------------------------"
    "---------------------------Graph Display----------------------------------"

    def solve(self, event):
        self.graph()
        self.table = TableFinale(self.constraints, self.gf)
        self.solver = Solver(self.table)
        self.solver.solve()


    def graph(self):
        fig = mpl.figure.Figure()
        self.ax = self.canvasGraph.draw_constraints(self.constraints, fig)
        fig.set_figheight(self.height/fig.dpi)
        fig.set_figwidth(self.width/fig.dpi)
        fig_x, fig_y = 0, 0
        fig_photo = self.right_frame.draw_figure(fig, loc=(fig_x, fig_y))
        fig_w, fig_h = fig_photo.width(), fig_photo.height()
