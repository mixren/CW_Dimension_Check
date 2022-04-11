import tkinter as tk
import tkinter.filedialog as fd

class MyScanPanel:
    def __init__(self, root, frame):
        self.root = root
        self.frame = frame

        self.lbl_scan = tk.Label(self.frame, text = "PDF Scan: ")
        self.ent_scan = tk.Entry(self.frame, width = 50)
        self.btn_scan = tk.Button(self.frame, text="Select", command=self.select_scan_pdf)

        self.lbl_scan.grid(row=0, column=0, sticky="w", padx=10)
        self.ent_scan.grid(row=0, column=1, sticky="w", padx=10)
        self.btn_scan.grid(row=0, column=2, sticky="w", padx=10)

    def select_scan_pdf(self):
        path = fd.askopenfilename(title="Select Dimension Check Scan", filetypes=[('PDF File', '*.pdf')])
        if path:
            self.ent_scan.delete(0, tk.END)
            self.ent_scan.insert(0, path)
            self.ent_scan.xview_moveto(1)
        self.root.focus()