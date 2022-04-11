import tkinter as tk
import tkinter.filedialog as fd

class MyTemplatePanel:
    def __init__(self, root, frame):
        self.root = root
        self.frame = frame

        self.lbl_template = tk.Label(self.frame, text = "Excel template: ")
        self.ent_template = tk.Entry(self.frame, width = 50)
        self.btn_template = tk.Button(self.frame, text="Select", command=self.select_template_file)

        self.lbl_template.grid(row=0, column=0, sticky="w", padx=10)
        self.ent_template.grid(row=0, column=1, sticky="w", padx=10)
        self.btn_template.grid(row=0, column=2, sticky="w", padx=10)

    def initial_setup(self, path:str):
        self.ent_template.delete(0, tk.END)
        self.ent_template.insert(0, path)

    
    def select_template_file(self):
        path = fd.askopenfilename(title="Select a Dimension Check template", filetypes=[("Excel files","*.xlsx")])
        if path:
            self.ent_template.delete(0, tk.END)
            self.ent_template.insert(0, path)
            self.ent_template.xview_moveto(1)

