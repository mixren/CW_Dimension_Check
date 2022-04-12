import tkinter as tk
import tkinter.filedialog as fd
from managers.generated_drawings_manager import GeneratedDrawingsManager

class MyGeneratedListPanel:
    def __init__(self, root, frame):
        self.root = root
        self.frame = frame

        self.var_reversed = tk.IntVar()

        self.lbl_generated = tk.Label(self.frame, text = "Generated list: ")
        self.ent_generated = tk.Entry(self.frame, width = 50)
        self.btn_generated = tk.Button(self.frame, text="Select", command=self.select_generated_list)
        self.cb_reverse  = tk.Checkbutton(self.frame, text="Reverse order", variable=self.var_reversed)

        self.lbl_generated.grid(row=0, column=0, sticky="w", padx=10)
        self.ent_generated.grid(row=0, column=1, sticky="w", padx=10)
        self.btn_generated.grid(row=0, column=2, sticky="w", padx=10)
        self.cb_reverse.grid(row=0, column=3, sticky="w", padx=20)

        self.init_setup()
        

    def init_setup(self):
        from returns.pipeline import is_successful
        self.cb_reverse.select()
        gdm=GeneratedDrawingsManager()
        res_path=gdm.get_path_if_exists()
        self.ent_generated.delete(0, tk.END)
        if is_successful(res_path):
            self.ent_generated.insert(0, res_path.unwrap())
        

    def select_generated_list(self):
        path = fd.askopenfilename(title="Select Generated Drawings List", filetypes=[('Text File', '*.txt')])
        if path:
            self.ent_generated.delete(0, tk.END)
            self.ent_generated.insert(0, path)
            self.ent_generated.xview_moveto(1)
        self.root.focus()