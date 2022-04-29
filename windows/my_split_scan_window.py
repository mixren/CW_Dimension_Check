import tkinter as tk
from returns.pipeline import is_successful
from panels.scan_split.my_scan_panel import MyScanPanel
from panels.scan_split.my_generated_list_panel import MyGeneratedListPanel
from panels.scan_split.my_year_folder_panel import MyYearFolderPanel
from managers.split_scan_manager import SplitScanManager

class MySplitScanWindow:
    TITLE="Split Scan"

    def __init__(self, root):
        self.ssm = SplitScanManager()
        self.root = root

        self.root.title(self.TITLE)
        self.root.grid_columnconfigure(0, weight=1)  # the line I've added

        self.frm_year_folder = tk.Frame(master=self.root)
        self.frm_year_folder.grid(row=0, column=0, pady=20, padx=50, sticky='w')

        self.frm_scan = tk.Frame(master=self.root)
        self.frm_scan.grid(row=1, column=0, pady=6, padx=50, sticky='w')
 
        self.frm_generated_list = tk.Frame(master=self.root)
        self.frm_generated_list.grid(row=2, column=0, pady=6, padx=50, sticky='w')

        self.year_folder_panel = MyYearFolderPanel(self.root, self.frm_year_folder)
        self.scan_panel = MyScanPanel(self.root, self.frm_scan)
        self.generated_list_panel = MyGeneratedListPanel(self.root, self.frm_generated_list)

        # "Generate" button
        self.btn_split = tk.Button(master=self.root, width=30, height=2, text="Split Scan", command=self.split_scan_do)
        self.btn_split.grid(row=3, column=0, pady=14)

        # Result Label
        self.lbl_result = tk.Label(master=self.root, fg="grey", font=('Arial', 10))
        self.lbl_result.grid(row=4, column=0)


    def split_scan_do(self):
        import time
        project_year_path = self.year_folder_panel.ent_year_folder.get()
        path_pdf = self.scan_panel.ent_scan.get()
        list_names = self.generated_list_panel.ent_generated.get()
        is_reversed = self.generated_list_panel.var_reversed.get()
        start = time.time()
        res = self.ssm.do(project_year_path, path_pdf, list_names, is_reversed)
        end = time.time()
        print(f"Elapsed: {round(end-start,4)} sec")
        if is_successful(res):
            self.lbl_result.config(text=f"Success.\n{res.unwrap()}", fg="green")

        else:
            self.lbl_result.config(text=res.failure(), fg="red")

            