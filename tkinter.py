import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class StudentSurvey(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Centennial College")
        self.geometry('500x350')
        self['background'] = '#f0f0f0'

        

        
        
        # Initialize variables
        self.fullname = tk.StringVar(value="Joan Suaverdez")
        self.residency_var = tk.StringVar(value="International")
        self.program_var = tk.StringVar(value="AI")
        self.courses_var1 = tk.StringVar(value="Comp100")
        self.courses_var2 = tk.StringVar(value="Comp213")
        self.courses_var3 = tk.StringVar(value="Comp120")

        self.create_widgets()

    def create_widgets(self):
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TLabel', background='#f0f0f0', font=('Arial', 12))
        style.configure('TEntry', font=('Arial', 12), fieldbackground='#ffffff')
        style.configure('TButton', font=('Arial', 12), background='#e1e1e1', borderwidth=1)
        style.configure('TCheckbutton', background='#f0f0f0', font=('Arial', 12))
        style.configure('TRadiobutton', background='#f0f0f0', font=('Arial', 12))
        style.configure('TCombobox', font=('Arial', 12), fieldbackground='#ffffff')
        

        
        # Configure grid weight for resizing behavior
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        for i in range(10):
            self.rowconfigure(i, weight=1)

        ttk.Label(self, text="ICET Student Survey", font=("Arial Bold", 24), background='#f0f0f0').grid(column=0, row=0, columnspan=3, pady=(10, 20))

        ttk.Label(self, text="Full Name").grid(column=0, row=1, sticky=tk.W, padx=10)
        ttk.Entry(self, width=20, textvariable=self.fullname).grid(column=1, row=1, sticky=tk.W, padx=10)

        ttk.Label(self, text="Residency:").grid(row=2, column=0, sticky="w")
        ttk.Radiobutton(self, text="Domestic", variable=self.residency_var, value="Domestic").grid(row=2, column=1, sticky="w", padx=10)
        ttk.Radiobutton(self, text="International", variable=self.residency_var, value="International").grid(row=3, column=1, sticky="w", padx=10)

        program_list = ["AI", "Gaming", "Health", "Software"]
        ttk.Label(self, text="Program").grid(column=0, row=4, sticky=tk.W, padx=10)
        program_combobox = ttk.Combobox(self, textvariable=self.program_var, values=program_list, state='readonly')
        program_combobox.grid(column=1, row=4, sticky=tk.W, padx=10)
        program_combobox.current(0)  # Set the default value

        ttk.Label(self, text="Courses").grid(column=0, row=5, sticky=tk.W, padx=10)
        ttk.Checkbutton(self, text="Programming", variable=self.courses_var1, onvalue="Comp100", offvalue="").grid(column=1, row=5, sticky=tk.W, padx=10)
        ttk.Checkbutton(self, text="Software Engineering", variable=self.courses_var2, onvalue="Comp213", offvalue="").grid(column=1, row=6, sticky=tk.W, padx=10)
        ttk.Checkbutton(self, text="Web Page Design", variable=self.courses_var3, onvalue="Comp120", offvalue="").grid(column=1, row=7, sticky=tk.W, padx=10)

        ttk.Button(self, text="Reset", command=self.reset_survey).grid(column=0, row=9, sticky=tk.W+tk.E, padx=10, pady=20)
        ttk.Button(self, text="OK", command=self.submit_survey).grid(column=1, row=9, sticky=tk.W+tk.E, padx=10, pady=20)
        ttk.Button(self, text="Exit", command=self.exit_survey).grid(column=2, row=9, sticky=tk.W+tk.E, padx=10, pady=20)

    def reset_survey(self):
        self.fullname.set("Joan Suaverdez")
        self.residency_var.set("International")
        self.program_var.set("AI")
        self.courses_var1.set("Comp100")
        self.courses_var2.set("Comp213")
        self.courses_var3.set("Comp120")

    def submit_survey(self):
        survey_info = (f"{self.fullname.get()}\n"
                       f"{self.residency_var.get()}\n"
                       f"{self.program_var.get()}\n"
                       f"{', '.join(filter(None, [self.courses_var1.get(), self.courses_var2.get(), self.courses_var3.get()]))}")
        messagebox.showinfo('Information', survey_info)

    def exit_survey(self):
        self.destroy()

if __name__ == '__main__':
    app = StudentSurvey()
    app.mainloop()
