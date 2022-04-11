import tkinter as tk
import tkinter.filedialog as fd
import os

class MyPipeLinePanel:
    def __init__(self, root, frame):
        self.root = root
        self.frame = frame

        self.lbl_pipe_line_folder = tk.Label(self.frame, text = "Pipe line folder: ")
        self.ent_pipe_line_folder = tk.Entry(self.frame, width = 50)
        self.btn_pipe_line_folder = tk.Button(self.frame, text="Select", command=self.select_pipe_line_folder)
        self.lbl_pipe_line = tk.Label(self.frame, text = "Pipe line: ")
        self.ent_pipe_line = tk.Entry(self.frame, width = 20)
        self.lnl_pipe_line_example = tk.Label(self.frame, text="e.g.: MP21-77", font=('Arial', 7), fg="grey")

        self.lbl_pipe_line_folder.grid(row=0, column=0, sticky="w", padx=10)
        self.ent_pipe_line_folder.grid(row=0, column=1, sticky="w", padx=10)
        self.btn_pipe_line_folder.grid(row=0, column=2, sticky="w", padx=10)
        self.lbl_pipe_line.grid(row=1, column=0, sticky="e", padx=10)
        self.ent_pipe_line.grid(row=1, column=1, sticky="w", padx=10)
        self.lnl_pipe_line_example.grid(row=2, column=1, sticky="w", padx=10)

    def select_pipe_line_folder(self):
        path = fd.askdirectory(title="Select a Pipe Line folder")
        if path:
            self.ent_pipe_line_folder.delete(0, tk.END)
            self.ent_pipe_line_folder.insert(0, path)
            self.ent_pipe_line_folder.xview_moveto(1)
            dir = os.path.basename(path)
            self.ent_pipe_line.delete(0, tk.END)
            self.ent_pipe_line.insert(0, self.__extract_pipe_line(dir))

    def __extract_pipe_line(self, s: str) -> str:
        import re
        return re.split(r'[_ ]+', s)[0]