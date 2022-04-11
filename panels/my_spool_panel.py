import tkinter as tk

class MySpoolPanel:
    def __init__(self, root, frame):
        self.root = root
        self.frame = frame

        # Spool frame
        self.lbl_spool = tk.Label(self.frame, text = "Spool: ", font=('Arial', 9, 'bold'))
        self.ent_spool = tk.Entry(self.frame, width = 20)
        self.lnl_spool_example = tk.Label(self.frame, text="e.g.: 05-AI-040-1-001", font=('Arial', 7), fg="grey")

        self.lbl_spool.grid(row=0, column=0, sticky="e", padx=10)
        self.ent_spool.grid(row=0, column=1, sticky="e", padx=10)
        self.lnl_spool_example.grid(row=1, column=1, sticky="w", padx=10)