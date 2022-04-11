import tkinter as tk

class MyMeasurementPanel:
    def __init__(self, root, frame):
        self.root = root
        self.frame = frame

        self.lbl_measurement = tk.Label(self.frame, text = "Measurements: ", font=('Arial', 9, 'bold'))
        self.txt_measurement = tk.Text(self.frame, width = 36, height=15)
        self.lnl_measurement_example1 = tk.Label(self.frame, text="e.g.:", font=('Arial', 7), fg="grey")
        self.lnl_measurement_example2 = tk.Label(self.frame, text="1,L,202,200,-", font=('Arial', 7), fg="grey")
        self.lnl_measurement_example3 = tk.Label(self.frame, text="2,L,1948,1765,150", font=('Arial', 7), fg="grey")
        self.lnl_measurement_example4 = tk.Label(self.frame, text="measurement No., type(L/A), actual, nominal, added", font=('Arial', 7), fg="grey")

        self.lbl_measurement.grid(row=0, column=0, sticky="w", padx=10)
        self.txt_measurement.grid(row=1, column=0, sticky="e", padx=10)
        self.lnl_measurement_example1.grid(row=2, column=0, sticky="w", padx=10)
        self.lnl_measurement_example2.grid(row=3, column=0, sticky="w", padx=10)
        self.lnl_measurement_example3.grid(row=4, column=0, sticky="w", padx=10)
        self.lnl_measurement_example4.grid(row=5, column=0, sticky="w", padx=10)

