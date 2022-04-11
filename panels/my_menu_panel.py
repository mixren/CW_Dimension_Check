import tkinter as tk
from managers.generated_drawings_manager import GeneratedDrawingsManager
from windows.my_split_scan_window import MySplitScanWindow

class MyMenuPanel:

    def __init__(self, root, menubar):
        self.root = root
        self.menubar = menubar

        gdm = GeneratedDrawingsManager()

        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Generated list", command=gdm.open_generated_list_txt)
        self.filemenu.add_command(label="Split scan", command=self.split_scan_window)
        self.filemenu.add_command(label="About", command=self.show_about)
        self.menubar.add_cascade(label="File", menu=self.filemenu)


    def split_scan_window(self):
        global w
        try:
            if w.state() == "normal": w.focus()
        except:
            w = tk.Toplevel(self.root)
            MySplitScanWindow(w)
    

    def show_about():
        pass
