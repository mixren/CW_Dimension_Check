import tkinter as tk

class MyDrawingPanel:
    def __init__(self, root, frame):
        self.root = root
        self.frame = frame

        # Drawing frame
        self.lbl_drawing = tk.Label(self.frame, text = "Drawing: ", font=('Arial', 9, 'bold'))
        self.ent_drawing = tk.Entry(self.frame, width = 20)
        self.lnl_drawing_example = tk.Label(self.frame, text="e.g.: 38.01", font=('Arial', 7), fg="grey")

        self.lbl_drawing.grid(row=1, column=0, sticky="e", padx=10)
        self.ent_drawing.grid(row=1, column=1, sticky="e", padx=10)
        self.lnl_drawing_example.grid(row=2, column=1, sticky="w", padx=10)