from tkinter import *

from Abstraction.Constraint import Constraint
from Abstraction.Goalfunction import GoalFunction
from Presentation.ConstraintCreationWindow import ConstraintCreationWindow
from Presentation.FunctionCreationWindow import FunctionCreationWindow


class LeftFrame(Frame) :
    def __init__(self, master = None, bg = "#909090", bd = 1, relief = RIDGE, padx  = 3, pady = 3):

        self.bg = bg
        self.subframes_bg = "#a0a0a0"
        self.bd = 1
        self.cells_height = 1
        self.cells_width = 5

        self.add_button_image = PhotoImage(file = "Images/buttonplus.png")
        self.del_button_image = PhotoImage(file = "Images/buttondel.png")
        self.edit_button_image = PhotoImage(file = "Images/buttonedit.png")

        Frame.__init__(self, master, bg = self.bg, bd = bd, relief = relief)

        "Problem setting frame"
        self.problem_setting_frame = Frame(self, bg = self.subframes_bg, bd = bd, relief = SUNKEN)
        self.build_problem_setting_frame(padx = padx, pady = pady, relief = RAISED)
        self.problem_setting_frame.pack(side = "top", padx = padx, pady = pady)

        "Solve Button Frame"
        self.solve_butt_frame = Frame(self, bg = self.subframes_bg, bd = bd, relief = SUNKEN)
        self.solve_butt_frame.pack(padx = padx, pady = 10, fill = "x")

        self.solve_butt = Button(self.solve_butt_frame, height = 3, text = "SOLVE", bg = "red")#a changer
        self.solve_butt.bind("<Button-1>", self.master.solve_button_action)
        self.solve_butt.pack(padx = padx, pady = 10, fill = "x", expand = True)

        "---Test/Demo Button"
        self.button_test = Button(self.solve_butt_frame, bg = "green", height = 3, text = "DEMO")
        self.button_test.bind('<Button-1>', self.test)
        self.button_test.pack(padx = padx, pady = 10, fill = "x")

        "Table Frame"
        self.create_table_frame()

        self.pack(side = 'left', padx = padx, pady = pady, fill = "y")

    "----------------------------------------Setting Buttons Frame--------------------"

    def build_problem_setting_frame(self, padx = 3, pady = 3, relief = RAISED):
        "Builds the frame that contains the buttons at initialization"

        "Goal funciton frame"
        self.gf_frame = Frame(self.problem_setting_frame, bg = self.bg, bd = self.bd, relief = relief)
        self.build_gf_frame_unfilled(padx, pady)
        self.gf_frame.pack(side = "top", padx = padx, pady = 10, fill = "x")

        "Constraints frame"
        self.constraints_frame = Frame(self.problem_setting_frame, bg = self.bg, bd = self.bd, relief = relief)
        self.build_cons_frame(padx, pady)
        self.constraints_frame.pack(padx = padx, pady = 10, fill= "x")

    "-----------------------------------------Goal Function Frame--------------------"

    def build_gf_frame_unfilled(self, padx = 3, pady = 3):
        self.button_gf = Button(self.gf_frame, text ='Fonction objectif', bg = "#b0b0dd", bd = 2, relief = RAISED)
        self.button_gf.bind('<Button-1>', self.action_button_gf)
        self.button_gf.pack(side = "top", padx = padx, pady = pady, fill = "x")

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
        self.label_gf = Label(self.gf_frame, text = self.master.gf.__str__(), bg = "#a5a5a5", borderwidth = 1, relief = GROOVE)
        self.label_gf.pack(side = "left", padx = 3, pady = 3, fill = "y")
        self.button_edit_gf = Button(self.gf_frame, image = self.edit_button_image, bg = self.bg)
        self.button_edit_gf.bind("<Button-1>", self.edit_gf)
        self.button_edit_gf.pack(side = "right", padx = 3, pady = 3)
        self.build_table_frame()

    def edit_gf(self, event):
        self.label_gf.destroy()
        self.button_edit_gf.destroy()
        self.build_gf_frame_unfilled()

    "--------------------------------------------Constraints Frame-----------------------"

    def build_cons_frame(self, padx = 3, pady = 3):
        self.label_cons = Label(self.constraints_frame, text = "Gestion des contraintes :", bg = self.subframes_bg,
                                bd = 1, relief = SUNKEN, height = 1)
        self.label_cons.pack(side = "top", padx = padx, pady = pady, fill = "x")

        self.cons_buttons_frame = Frame(self.constraints_frame)
        self.build_cons_buttons_frame()
        self.cons_buttons_frame.pack(side = "right", padx = padx, pady = pady)

        self.list_constraints = Listbox(self.constraints_frame, height = 5)
        self.list_constraints.pack(padx = padx, pady = pady, fill = BOTH)

    def build_cons_buttons_frame(self):

        self.button_add_cons = Button(self.cons_buttons_frame, image = self.add_button_image, bg = self.bg)
        self.button_add_cons.bind('<Button-1>', self.add_button_action)
        self.button_add_cons.pack()

        self.button_edit_cons = Button(self.cons_buttons_frame, image = self.edit_button_image, bg = self.bg)
        self.button_edit_cons.bind("<Button-1>", self.edit_cons)
        self.button_edit_cons.pack()

        self.button_del_cons = Button(self.cons_buttons_frame, image = self.del_button_image, bg = self.bg)
        self.button_del_cons.bind('<Button-1>', self.del_button_action)
        self.button_del_cons.pack()

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
        self.master.display_graph()

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
            self.master.display_graph()

    "---------------------Table Frame------------------------------------------"

    def create_table_frame(self):
        self.bottom_frame = Frame(self, bg = self.subframes_bg, bd = 1, relief = SUNKEN)
        self.bottom_frame.pack(side = "bottom", padx = 3, pady = 3, fill = "x")
        self.table_label_frame = Frame(self.bottom_frame, bg = self.bg, bd = 1, relief = RAISED)
        self.table_label_frame.pack(side = "top", padx = 3, pady = 3, fill = "x")
        label = Label(self.table_label_frame, text = "Tableau : ", bg = self.subframes_bg, bd = 1, relief = SUNKEN)
        label.pack(padx = 3, pady = 3, fill = "x")
        self.table_frame = Frame(self.bottom_frame, bg = self.bg, bd = 1, relief = RAISED)
        self.table_frame.pack(side = "bottom", padx = 3, pady = 3)


    def build_table_frame(self):
        if not self.table_frame is None :
            constraints = self.master.constraints
            nb_cons = len(constraints)
            self.bottom_frame.destroy()
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
                    Label(self.table_frame, text = s, bg = "#cccccc", relief = SUNKEN, height = self.cells_height,
                             width = self.cells_width, borderwidth = 2).grid(row = line, column = column, padx = 1, pady = 1)
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
                    Label(self.table_frame, text = s, bg = "#cccccc", relief = SUNKEN, height = self.cells_height,
                             width = self.cells_width, borderwidth = 2).grid(row = line, column = column, padx = 1, pady = 1)

    def update_table(self):
        tabResultat = self.master.solver.tab
        lines = tabResultat.size()
        columns = len (tabResultat[0])
        self.bottom_frame.destroy()
        self.create_table_frame()
        for line in range(lines) :
            for column in range(columns) :
                Label(self.table_frame, text = str(tabResultat[line][column]), bg = "#cccccc", relief = SUNKEN,
                      height = self.cells_height, width = self.cells_width, borderwidth = 2).grid(row = line, column = column)