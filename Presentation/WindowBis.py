import matplotlib as mpl
import tkinter as tk
mpl.use("TkAgg")


class WindowBis(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.build_right_frame()
        self.build_left_frame()

    def build_right_frame(self):
        pass

    def build_left_frame(self):
        self.left_frame = tk.Frame(self)
        self.build_button_frame()
        self.build_table_frame()
        self.left_frame.pack(side = 'left')

    def build_button_frame(self):
        self.frame_constraints = tk.Frame(self.left_frame, borderwidth=0, text="Constraintes")
        self.list_constraints = tk.Listbox(self.frame_constraints)
        self.list_constraints.pack()
        self.frame_constraints.pack(side="left", padx=5, pady=5)

    def build_table_frame(self):
        pass
