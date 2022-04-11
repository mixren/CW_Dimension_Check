import tkinter as tk
from panels.my_template_panel import MyTemplatePanel
from panels.my_pipe_line_panel import MyPipeLinePanel
from panels.my_drawing_panel import MyDrawingPanel
from panels.my_spool_panel import MySpoolPanel
from panels.my_measurement_panel import MyMeasurementPanel
from panels.my_rest_panel import MyRestPanel
from panels.my_menu_panel import MyMenuPanel
from managers.generator_manager import GeneratorManager
from my_pipeline import MyPipeline

class MyTkWindow:
    TITLE="CWT Dimension Check file generator"

    def __init__(self):
        self.root = tk.Tk()
        self.root.title(self.TITLE)
        
        self.frm_template = tk.Frame(master=self.root)
        self.frm_template.grid(row=0, column=0, pady=6, padx=50)

        self.frm_pipe_line_folder = tk.Frame(master=self.root)
        self.frm_pipe_line_folder.grid(row=1, column=0, pady=6, padx=50)

        self.frm_spool_drawing = tk.Frame(master=self.root)
        self.frm_spool_drawing_left = tk.Frame(master=self.frm_spool_drawing)
        self.frm_spool_drawing_right = tk.Frame(master=self.frm_spool_drawing)
        self.frm_spool_drawing.grid(row=2, columnspan=2, pady=10, padx=10)
        self.frm_spool_drawing_left.grid(row=0, column=0, sticky="e", padx=10)
        self.frm_spool_drawing_right.grid(row=0, column=1, sticky="e", padx=10)
        
        self.frm_measurement_and_rest = tk.Frame(master=self.root)
        self.frm_measurement = tk.Frame(master=self.frm_measurement_and_rest)
        self.frm_rest = tk.Frame(master=self.frm_measurement_and_rest)
        self.frm_measurement_and_rest.grid(row=3, columnspan=2, pady=10)
        self.frm_measurement.grid(row=0, column=0, sticky="e", padx=10)
        self.frm_rest.grid(row=0, column=1, sticky="e", padx=10, pady=6)

        # "Generate" button
        self.btn_generate = tk.Button(master=self.root, width=30, height=2, text="Generate xml + pdf", command=self.generate)
        self.btn_generate.grid(row=4, column=0, pady=14)

        # Result Label
        self.lbl_result = tk.Label(master=self.root, width=30, fg="grey", font=('Arial', 10))
        self.lbl_result.grid(row=5, column=0)

        self.template_panel = MyTemplatePanel(self.root, self.frm_template)
        self.pipe_line_panel = MyPipeLinePanel(self.root, self.frm_pipe_line_folder)
        self.drawing_panel = MyDrawingPanel(self.root, self.frm_spool_drawing_left)
        self.spool_panel = MySpoolPanel(self.root, self.frm_spool_drawing_right)
        self.measurement_panel = MyMeasurementPanel(self.root, self.frm_measurement)
        self.rest_panel = MyRestPanel(self.root, self.frm_rest)

        # Menu
        self.menubar = tk.Menu(self.root)
        self.filemenu = MyMenuPanel(self.root, self.menubar)
        self.root.config(menu=self.menubar)


    def start(self):
        self.root.mainloop()


    def initial_setup(self):
        from datetime import date
        import os

        excel_template = os.path.join("repo","template_DimChecklist.xlsx")
        signature = os.path.join("repo", "DS signature blue.png")
        date_today = date.today().strftime("%d.%m.%Y")
        name = "Dmitrijs Strezs"

        self.template_panel.initial_setup(excel_template if os.path.isfile(excel_template) else '')
        self.rest_panel.initial_setup(date_today, name, signature if os.path.isfile(signature) else '')


    def generate(self):
        from returns.pipeline import is_successful

        template_path = self.template_panel.ent_template.get()
        pipe_line_folder = self.pipe_line_panel.ent_pipe_line_folder.get()
        pipe_line = self.pipe_line_panel.ent_pipe_line.get()
        spool = self.spool_panel.ent_spool.get()
        drawing_short = self.drawing_panel.ent_drawing.get()
        measurements = self.measurement_panel.txt_measurement.get("1.0", tk.END)
        date = self.rest_panel.ent_date.get()
        name = self.rest_panel.ent_name.get()
        path_signature = self.rest_panel.ent_signature.get()

        pipeline = MyPipeline()
        processed_input = pipeline.process(
            template_path,
            pipe_line_folder,
            pipe_line,
            spool,
            drawing_short,
            measurements,
            date,
            name,
            path_signature)

        if not is_successful(processed_input):
            self.lbl_result.config(text=f"Failed to generate file\n{processed_input.failure()}", fg="red")
            return

        res = GeneratorManager.generate_files(
            processed_input.unwrap()[0],
            processed_input.unwrap()[1],
            processed_input.unwrap()[2],
            processed_input.unwrap()[3],
            processed_input.unwrap()[4],
            processed_input.unwrap()[5],
            processed_input.unwrap()[6],
            processed_input.unwrap()[7],
            processed_input.unwrap()[8]
        )
       
        '''res = GeneratorManager.generate(
            template_path,
            pipe_line_folder,
            pipe_line,
            spool,
            drawing_short,
            measurements,
            date,
            name,
            path_signature)'''

        if is_successful(res):
            self.lbl_result.config(text=f"{pipe_line}-{drawing_short}.00 successfully generated", fg="green")
            self.measurement_panel.txt_measurement.delete("1.0", tk.END)
            self.drawing_panel.ent_drawing.focus_set()
            print(f"Success. {pipe_line}-{drawing_short}.00")

        else:
            self.lbl_result.config(text=f"Failed to generate file\n{res.failure()}", fg="red")