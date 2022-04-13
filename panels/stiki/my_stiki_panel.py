import tkinter as tk
import tkinter.filedialog as fd

class MyStikiPanel:
    def __init__(self, root, frame):
        self.root = root
        self.frame = frame

        self.lbl_stiki = tk.Label(self.frame, text = "Стыки по Спулам Excel: ")
        self.ent_stiki = tk.Entry(self.frame, width = 50)
        self.btn_stiki = tk.Button(self.frame, text="Select", command=self.select_stiki_excel)

        self.lbl_stiki.grid(row=0, column=0, sticky="w", padx=10)
        self.ent_stiki.grid(row=0, column=1, sticky="w", padx=10)
        self.btn_stiki.grid(row=0, column=2, sticky="w", padx=10)

    def select_stiki_excel(self):
        path = fd.askopenfilename(title="Стыки по Спулам", filetypes=[('Excel File', '*.xlsx')])
        if path:
            self.ent_stiki.delete(0, tk.END)
            self.ent_stiki.insert(0, path)
            self.ent_stiki.xview_moveto(1)
        self.root.focus()