import matplotlib as mpl
import tkinter as tk

from Abstraction.Constraint import Constraint
from Abstraction.Goalfunction import GoalFunction
from Abstraction.Solver import Solver
from Abstraction.TableFinale import TableFinale
from Presentation.ConstraintCreationWindow import ConstraintCreationWindow
from Presentation.FunctionCreationWindow import FunctionCreationWindow
from Presentation.GraphFrame import GraphFrame

mpl.use("TkAgg")


class Window(tk.Tk):
    def __init__(self):
        """Builds the whole window with two main Frames, the left one contains buttons and the let one contains the graph"""
        tk.Tk.__init__(self)

        self.title("PySThon")
        self.gf = None
        self.constraints = []
        self.cells_height = 1
        self.cells_width = 5

        "Creating right frame"
        self.right_frame = GraphFrame(self, None) #pas de controleur pour l'instant
        self.right_frame.pack(side = 'right')

        "Creating left frame"
        self.left_frame = tk.Frame(self)
        self.build_left_frame()
        self.left_frame.pack(side = 'left')

        self.mainloop()

    def set_gf(self, gf):
        self.gf = gf
        self.build_gf_frame_filled()

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
        self.solve_butt_frame.pack(pady = 10, fill = tk.BOTH, expand = True)

        "Table Frame"
        self.create_table_frame()

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
        self.button_test = tk.Button(self.gf_frame, text = "Démo")
        self.button_test.bind('<Button-1>', self.test)
        self.button_test.pack(side = "top", pady = 10)
        self.button_gf = tk.Button(self.gf_frame, text ='Fonction objectif')
        self.button_gf.bind('<Button-1>', self.action_button_gf)
        self.button_gf.pack(side = "top", pady = 10)

    def test(self, event):
        self.add_constraint(Constraint([1, 1, 4], "<="))
        self.add_constraint(Constraint([1, 0, 3], "<="))
        self.add_constraint(Constraint([0, 1, 2], "<="))
        self.set_gf(GoalFunction([300, 100, 0], True))

    def action_button_gf(self, event):
        FunctionCreationWindow(self)

    def build_gf_frame_filled(self):
        self.button_gf.destroy()
        self.button_test.destroy()
        self.label_gf = tk.Label(self.gf_frame, text = self.gf.__str__(), relief = tk.GROOVE)
        self.label_gf.pack(side = "left")
        self.button_edit_gf = tk.Button(self.gf_frame, text = "Edit")
        self.button_edit_gf.bind("<Button-1>", self.edit_gf)
        self.button_edit_gf.pack(side = "right")
        self.build_table_frame()

    def edit_gf(self, event):
        self.label_gf.destroy()
        self.button_edit_gf.destroy()
        self.build_gf_frame_unfilled()

    "--------------------------------------------Constraints Frame-----------------------"

    def build_cons_frame(self):
        self.label_cons = tk.Label(self.constraints_frame, text = "Contraintes")
        self.label_cons.pack(side = "top")

        self.cons_buttons_frame = tk.Frame(self.constraints_frame)
        self.build_cons_buttons_frame()
        self.cons_buttons_frame.pack(side = "right", padx = 2)

        self.list_constraints = tk.Listbox(self.constraints_frame, height = 5)
        self.list_constraints.pack()

    def build_cons_buttons_frame(self):

        self.button_add_cons = tk.Button(self.cons_buttons_frame, text = "Add")
        self.button_add_cons.bind('<Button-1>', self.add_button_action)
        self.button_add_cons.pack(pady = 1, fill = tk.BOTH, expand = True)

        self.button_edit_cons = tk.Button(self.cons_buttons_frame, text = "Edit")
        self.button_edit_cons.bind("<Button-1>", self.edit_cons)
        self.button_edit_cons.pack(pady = 1, fill = tk.BOTH, expand = True)

        self.button_del_cons = tk.Button(self.cons_buttons_frame, text = "Del")
        self.button_del_cons.bind('<Button-1>', self.del_button_action)
        self.button_del_cons.pack(pady = 1, fill = tk.BOTH, expand = True)

    def add_button_action(self, event):
        ConstraintCreationWindow(self)

    def add_constraint(self, constraint):
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
        size = self.list_constraints.size()
        if size > 4 :
            self.list_constraints.configure(height = size)
        self.build_table_frame()
        self.table_frame.pack()
        self.graph()

    def edit_cons(self, event):
        ind = self.list_constraints.curselection().__getitem__(0)
        if isinstance(ind, int) and ind >= 0 :
            self.list_constraints.delete(ind)
            self.constraints.pop(ind)
            ConstraintCreationWindow(self)

    def del_button_action(self, event):
        ind = self.list_constraints.curselection().__getitem__(0)
        if isinstance(ind, int) and ind >= 0 :
            print (ind)
            self.list_constraints.delete(ind)
            self.constraints.pop(ind)
            if len(self.constraints) == 0 :
                self.table_frame.destroy()
                self.create_table_frame()
            else :
                self.build_table_frame()
            self.graph()

    "--------------------Solve Button Frame------------------------------------"

    def build_solve_button_frame(self):
        self.solve_butt = tk.Button(self.solve_butt_frame, text = "Solve", bg = "red", width = 27)#a changer
        self.solve_butt.bind("<Button-1>", self.solve)
        self.solve_butt.pack(fill = tk.BOTH, expand = True)

    "---------------------Table Frame------------------------------------------"

    def create_table_frame(self):
        self.table_frame = tk.LabelFrame(self.left_frame, borderwidth = 0,
                                         relief = tk.GROOVE, text = "Tableau")
        self.table_frame.pack()

    def build_table_frame(self):
        if not self.table_frame is None :
            self.table_frame.destroy()
            self.create_table_frame()
            print(len(self.constraints))
            line = 0
            for cons in self.constraints :
                a, b, c, = cons.coeffsConstraint
                for column in range(3 + len(self.constraints)):
                    s = "0"
                    if column == 0 :
                        s = str(a)
                    elif column == 1 :
                        s = str(b)
                    elif column == 2 + len(self.constraints) :
                        s = str(c)
                    elif line == column - 2 :
                        s = "1"
                    tk.Label(self.table_frame, text = s, relief = tk.GROOVE, height = self.cells_height,
                             width = self.cells_width, borderwidth = 5).grid(row = line, column = column)
                line += 1
            if not self.gf == None :
                for column in range(3 + len(self.constraints)):
                    s = "0"
                    a, b, c, = self.gf.coFunction
                    if column == 0 :
                        s = str(a)
                    elif column == 1 :
                        s = str(b)
                    elif column == len(self.constraints) + 2 :
                        s = str(c)
                    tk.Label(self.table_frame, text = s, relief = tk.GROOVE, height = self.cells_height,
                             width = self.cells_width, borderwidth = 5).grid(row = line, column = column)



    "--------------Right Frame-------------------------------------------------"
    "---------------------------Graph Display----------------------------------"

    def solve(self, event):
        self.graph()
        tab = []
        for e in self.constraints :
            tab.append(e.normalize())
        self.table = TableFinale(tab, self.gf.normalize())
        self.solver = Solver(self.table)
        self.solver.solve()
        tabResultat = self.solver.tab
        print (type(tabResultat))
        lines = tabResultat.size()
        columns = len (tabResultat[0])
        self.table_frame.destroy()
        self.create_table_frame()
        for line in range(lines) :
            for column in range(columns) :
                tk.Label(self.table_frame, text = str(tabResultat[line][column]), relief = tk.GROOVE, height = self.cells_height,
                             width = self.cells_width, borderwidth = 5).grid(row = line, column = column)



    def graph(self):
        self.right_frame.destroy()
        self.right_frame = GraphFrame(self, None) #pas de controleur pour l'instant
        self.right_frame.pack(side='right')
