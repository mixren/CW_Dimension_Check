import tkinter as tk
from managers.generated_drawings_manager import GeneratedDrawingsManager
from windows.my_split_scan_window import MySplitScanWindow
from windows.my_about_window import MyAboutWindow

class MyMenuPanel:

    def __init__(self, root, menubar):
        self.root = root
        self.menubar = menubar

        gdm = GeneratedDrawingsManager()

        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Split Scan", command=self.open_split_scan_window)
        self.filemenu.add_command(label="Show Generated List", command=gdm.open_generated_list_txt)
        self.filemenu.add_command(label="About", command=self.open_about_window)
        self.menubar.add_cascade(label="File", menu=self.filemenu)


    def open_split_scan_window(self):
        global w
        try:
            if w.state() == "normal": w.focus()
        except:
            w = tk.Toplevel(self.root)
            MySplitScanWindow(w)
    

    def open_about_window(self):
        #window = tk.Toplevel(self.root)
        #MyAboutWindow(window)
        import os
        try:
            os.startfile(os.path.abspath('README.txt'))
        except Exception as e:
            print(f"Can't open a file. {e}")
