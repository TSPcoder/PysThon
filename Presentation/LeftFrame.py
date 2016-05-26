from tkinter import *

from Abstraction.Constraint import Constraint
from Abstraction.Goalfunction import GoalFunction
from Presentation.ConstraintCreationWindow import ConstraintCreationWindow
from Presentation.FunctionCreationWindow import FunctionCreationWindow


class LeftFrame(Frame) :
    def __init__(self, master = None):
        Frame.__init__(self, master)

        self.cells_height = 1
        self.cells_width = 5

        "Problem setting frame"
        self.button_frame = Frame(self)
        self.build_button_frame()
        self.button_frame.pack()

        "Solve Button Frame"
        self.solve_butt_frame = Frame(self)
        self.build_solve_button_frame()
        self.solve_butt_frame.pack(pady = 10, fill = BOTH, expand = True)

        "Table Frame"
        self.create_table_frame()

        self.pack(side = 'left')

    "----------------------------------------Setting Buttons Frame--------------------"

    def build_button_frame(self):
        "Builds the frame that contains the buttons at initialization"

        "Goal funciton frame"
        self.gf_frame = Frame(self.button_frame)
        self.build_gf_frame_unfilled()
        self.gf_frame.pack(side = "top")

        "Constraints frame"
        self.constraints_frame = Frame(self.button_frame)
        self.build_cons_frame()
        self.constraints_frame.pack()

    "-----------------------------------------Goal Function Frame--------------------"

    def build_gf_frame_unfilled(self):
        self.button_test = Button(self.gf_frame, text = "Démo")
        self.button_test.bind('<Button-1>', self.test)
        self.button_test.pack(side = "top", pady = 10)
        self.button_gf = Button(self.gf_frame, text ='Fonction objectif')
        self.button_gf.bind('<Button-1>', self.action_button_gf)
        self.button_gf.pack(side = "top", pady = 10)

    def test(self, event):
        self.add_constraint(Constraint([1, 1, 4], "<="))
        self.add_constraint(Constraint([1, 0, 3], "<="))
        self.add_constraint(Constraint([0, 1, 2], "<="))
        self.master.set_gf(GoalFunction([300, 100, 0], True))

    def action_button_gf(self, event):
        FunctionCreationWindow(self)

    def build_gf_frame_filled(self):
        self.button_gf.destroy()
        self.button_test.destroy()
        self.label_gf = Label(self.gf_frame, text = self.master.gf.__str__(), relief = GROOVE)
        self.label_gf.pack(side = "left")
        self.button_edit_gf = Button(self.gf_frame, text = "Edit")
        self.button_edit_gf.bind("<Button-1>", self.edit_gf)
        self.button_edit_gf.pack(side = "right")
        self.build_table_frame()

    def edit_gf(self, event):
        self.label_gf.destroy()
        self.button_edit_gf.destroy()
        self.build_gf_frame_unfilled()

    "--------------------------------------------Constraints Frame-----------------------"

    def build_cons_frame(self):
        self.label_cons = Label(self.constraints_frame, text = "Contraintes")
        self.label_cons.pack(side = "top")

        self.cons_buttons_frame = Frame(self.constraints_frame)
        self.build_cons_buttons_frame()
        self.cons_buttons_frame.pack(side = "right", padx = 2)

        self.list_constraints = Listbox(self.constraints_frame, height = 5)
        self.list_constraints.pack()

    def build_cons_buttons_frame(self):

        self.button_add_cons = Button(self.cons_buttons_frame, text = "Add")
        self.button_add_cons.bind('<Button-1>', self.add_button_action)
        self.button_add_cons.pack(pady = 1, fill = BOTH, expand = True)

        self.button_edit_cons = Button(self.cons_buttons_frame, text = "Edit")
        self.button_edit_cons.bind("<Button-1>", self.edit_cons)
        self.button_edit_cons.pack(pady = 1, fill = BOTH, expand = True)

        self.button_del_cons = Button(self.cons_buttons_frame, text = "Del")
        self.button_del_cons.bind('<Button-1>', self.del_button_action)
        self.button_del_cons.pack(pady = 1, fill = BOTH, expand = True)

    def add_button_action(self, event):
        ConstraintCreationWindow(self)

    def add_constraint(self, constraint):
        cons = self.master.constraints
        cons_listbox = self.list_constraints
        n = len(cons) + 1
        cons_listbox.insert(n, constraint.toString())
        if constraint.operatorConstraint == '=':
            constraint1 = Constraint(constraint.coeffsConstraint, '<=').normalize()
            constraint2 = Constraint(constraint.coeffsConstraint, '>=').normalize()
            cons.append(constraint1)
            cons.append(constraint2)
        else:
            #constraint = constraint.normalize()
            cons.append(constraint)
        size = cons_listbox.size()
        if size > 4 :
            cons_listbox.configure(height = size)
        self.build_table_frame()
        self.table_frame.pack()
        self.master.graph()

    def edit_cons(self, event):
        ind = self.list_constraints.curselection().__getitem__(0)
        if isinstance(ind, int) and ind >= 0 :
            self.list_constraints.delete(ind)
            self.master.constraints.pop(ind)
            ConstraintCreationWindow(self)

    def del_button_action(self, event):
        cons = self.master.constraints
        list_cons = self.list_constraints
        ind = list_cons.curselection().__getitem__(0)
        if isinstance(ind, int) and ind >= 0 :
            list_cons.delete(ind)
            cons.pop(ind)
            if len(cons) == 0 :
                self.table_frame.destroy()
                self.create_table_frame()
            else :
                self.build_table_frame()
            self.master.graph()

    "--------------------Solve Button Frame------------------------------------"

    def build_solve_button_frame(self):
        self.solve_butt = Button(self.solve_butt_frame, text = "Solve", bg = "red", width = 27)#a changer
        self.solve_butt.bind("<Button-1>", self.master.solve)
        self.solve_butt.pack(fill = BOTH, expand = True)

    "---------------------Table Frame------------------------------------------"

    def create_table_frame(self):
        self.table_frame = LabelFrame(self, borderwidth = 0,
                                         relief = GROOVE, text = "Tableau")
        self.table_frame.pack()

    def build_table_frame(self):
        if not self.table_frame is None :
            constraints = self.master.constraints
            nb_cons = len(constraints)
            self.table_frame.destroy()
            self.create_table_frame()
            line = 0
            for cons in constraints :
                a, b, c, = cons.coeffsConstraint
                for column in range(3 + nb_cons):
                    s = "0"
                    if column == 0 :
                        s = str(a)
                    elif column == 1 :
                        s = str(b)
                    elif column == 2 + nb_cons :
                        s = str(c)
                    elif line == column - 2 :
                        s = "1"
                    Label(self.table_frame, text = s, relief = GROOVE, height = self.cells_height,
                             width = self.cells_width, borderwidth = 5).grid(row = line, column = column)
                line += 1
            if not self.master.gf == None :
                for column in range(3 + nb_cons):
                    s = "0"
                    a, b, c, = self.master.gf.coFunction
                    if column == 0 :
                        s = str(a)
                    elif column == 1 :
                        s = str(b)
                    elif column == nb_cons + 2 :
                        s = str(c)
                    Label(self.table_frame, text = s, relief = GROOVE, height = self.cells_height,
                             width = self.cells_width, borderwidth = 5).grid(row = line, column = column)

    def update_table(self):
        tabResultat = self.master.solver.tab
        lines = tabResultat.size()
        columns = len (tabResultat[0])
        self.table_frame.destroy()
        self.create_table_frame()
        for line in range(lines) :
            for column in range(columns) :
                Label(self.table_frame, text = str(tabResultat[line][column]), relief = GROOVE, height = self.cells_height,
                        width = self.cells_width, borderwidth = 5).grid(row = line, column = column)