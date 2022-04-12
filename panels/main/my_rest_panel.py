import tkinter as tk
import tkinter.filedialog as fd

class MyRestPanel:
    def __init__(self, root, frame):
        self.root = root
        self.frame = frame

        self.lbl_date = tk.Label(self.frame, text = "Date: ")
        self.ent_date = tk.Entry(self.frame, width=20)
        self.lbl_name = tk.Label(self.frame, text = "Name: ")
        self.ent_name = tk.Entry(self.frame, width=20)
        self.lbl_signature = tk.Label(self.frame, text = "Signature: ")
        self.ent_signature = tk.Entry(self.frame, width=20)
        self.btn_signature = tk.Button(self.frame, text="Select", command=self.select_signature)

        self.lbl_date.grid(row=0, column=0, sticky="w", padx=10)
        self.ent_date.grid(row=1, column=0, sticky="e", padx=10)
        self.lbl_name.grid(row=2, column=0, sticky="w", padx=10)
        self.ent_name.grid(row=3, column=0, sticky="e", padx=10)
        self.lbl_signature.grid(row=4, column=0, sticky="w", padx=10)
        self.ent_signature.grid(row=5, column=0, sticky="e", padx=10)
        self.btn_signature.grid(row=5, column=1, sticky="w", padx=10)

    def initial_setup(self, date, name, signature_path):
        self.ent_date.delete(0, tk.END)
        self.ent_name.delete(0, tk.END)
        self.ent_signature.delete(0, tk.END)
        self.ent_date.insert(0, date)
        self.ent_name.insert(0, name)
        self.ent_signature.insert(0, signature_path)

    def select_signature(self):
        path = fd.askopenfilename(title="Select a Dimension Check template", filetypes=[("PNG","*.png", "")])
        if path:
            self.ent_signature.delete(0, tk.END)
            self.ent_signature.insert(0, path)
            self.ent_signature.xview_moveto(1)

