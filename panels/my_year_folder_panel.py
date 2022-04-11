import tkinter as tk
import tkinter.filedialog as fd
from managers.generated_drawings_manager import GeneratedDrawingsManager

class MyYearFolderPanel:
    def __init__(self, root, frame):
        self.root = root
        self.frame = frame

        self.var_reversed = tk.IntVar()

        self.lbl_year_folder = tk.Label(self.frame, text = "Project Year Folder: ")
        self.ent_year_folder = tk.Entry(self.frame, width = 50)
        self.btn_year_folder = tk.Button(self.frame, text="Select", command=self.select_folder)

        self.lbl_year_folder.grid(row=0, column=0, sticky="w", padx=10)
        self.ent_year_folder.grid(row=0, column=1, sticky="w", padx=10)
        self.btn_year_folder.grid(row=0, column=2, sticky="w", padx=10)

        self.init_setup()
        

    def init_setup(self):
        import os
        path = "Z:\CWT Documents\\2021"
        if os.path.exists(path):
            self.ent_year_folder.delete(0, tk.END)
            self.ent_year_folder.insert(0, path)
            self.ent_year_folder.xview_moveto(1)
        

    def select_folder(self):
        path = fd.askdirectory(title="Select Project Year Folder")
        if path:
            self.ent_year_folder.delete(0, tk.END)
            self.ent_year_folder.insert(0, path)
            self.ent_year_folder.xview_moveto(1)
        self.root.focus()