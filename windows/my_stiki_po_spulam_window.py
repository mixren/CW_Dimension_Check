import tkinter as tk
from returns.pipeline import is_successful
from panels.scan_split.my_generated_list_panel import MyGeneratedListPanel
from panels.stiki.my_stiki_panel import MyStikiPanel
from managers.excel_manager import ExcelManager
from managers.generated_drawings_manager import GeneratedDrawingsManager

class MyStikiPoSpulamWindow:
    TITLE="Стыки по Спулам"

    def __init__(self, root):
        self.root = root
        self.em = ExcelManager()
        self.gdm = GeneratedDrawingsManager()

        self.root.title(self.TITLE)
        self.root.grid_columnconfigure(0, weight=1)  # the line I've added

        self.frm_stiki_folder = tk.Frame(master=self.root)
        self.frm_stiki_folder.grid(row=0, column=0, pady=20, padx=50, sticky='w')
 
        self.frm_generated_list = tk.Frame(master=self.root)
        self.frm_generated_list.grid(row=1, column=0, pady=6, padx=50, sticky='w')

        self.stiki_panel = MyStikiPanel(self.root, self.frm_stiki_folder)
        self.generated_list_panel = MyGeneratedListPanel(self.root, self.frm_generated_list)

        # Date
        self.frm_date = tk.Frame(master=self.root)
        self.frm_date.grid(row=2, column=0, sticky="w", pady=6, padx=50)

        self.lbl_date = tk.Label(self.frm_date, text = "Date: ")
        self.ent_date = tk.Entry(self.frm_date, width=20)
        self.lbl_date.grid(row=0, column=0, sticky="w", padx=10)
        self.ent_date.grid(row=0, column=1, sticky="e", padx=10)
        

        # "Generate" button
        self.btn_split = tk.Button(master=self.root, width=30, height=2, text="Fill Стыки по Спулам", command=self.fill_stiki_po_spulam)
        self.btn_split.grid(row=3, column=0, pady=14)

        # Result Label
        self.lbl_result = tk.Label(master=self.root, fg="grey", font=('Arial', 10))
        self.lbl_result.grid(row=4, column=0)

        self.initial_setup()


    def initial_setup(self):
        from datetime import date
        date_today = date.today().strftime("%d.%m.%Y")
        self.ent_date.insert(0, date_today)


    def fill_stiki_po_spulam(self):
        import time
        path_stiki_xlsx = self.stiki_panel.ent_stiki.get()
        path_list_names = self.generated_list_panel.ent_generated.get()
        date = self.ent_date.get()

        start = time.time()

        drawing_names = self.gdm.get_list_drawing_names(path_list_names, 0)
        if is_successful(drawing_names):
            res = self.em.fill_stiki_po_spulam_xlsx(path_stiki_xlsx, drawing_names.unwrap(), date)
            if is_successful(res):
                self.lbl_result.config(text=f"Success", fg="green")
            else:
                self.lbl_result.config(text=res.failure(), fg="red")
        else:
            self.lbl_result.config(text=drawing_names.failure(), fg="red")

        end = time.time()
        print(f"Elapsed: {round(end-start,4)} sec")

            