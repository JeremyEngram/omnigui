import os
import subprocess
import tkinter as tk
from tkinter import ttk, filedialog

class OmnisintGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Omnisint GUI")

        # Create widgets
        self.create_widgets()

    def create_widgets(self):
        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky="NSEW")

        self.username_label = ttk.Label(self.main_frame, text="Username to search (Sherlock):")
        self.username_label.grid(row=0, column=0, sticky="W")

        self.username_entry = ttk.Entry(self.main_frame, width=40)
        self.username_entry.grid(row=0, column=1, columnspan=2, pady=5)

        self.email_label = ttk.Label(self.main_frame, text="Email or username to search (Userecon):")
        self.email_label.grid(row=1, column=0, sticky="W")

        self.email_entry = ttk.Entry(self.main_frame, width=40)
        self.email_entry.grid(row=1, column=1, columnspan=2, pady=5)

        self.domain_label = ttk.Label(self.main_frame, text="Domain or IP address (EagleEye):")
        self.domain_label.grid(row=2, column=0, sticky="W")

        self.domain_entry = ttk.Entry(self.main_frame, width=40)
        self.domain_entry.grid(row=2, column=1, columnspan=2, pady=5)

        self.domain_metagoofil_label = ttk.Label(self.main_frame, text="Domain for Metagoofil:")
        self.domain_metagoofil_label.grid(row=3, column=0, sticky="W")

        self.domain_metagoofil_entry = ttk.Entry(self.main_frame, width=40)
        self.domain_metagoofil_entry.grid(row=3, column=1, columnspan=2, pady=5)

        self.filetype_label = ttk.Label(self.main_frame, text="File type to search for (Metagoofil):")
        self.filetype_label.grid(row=4, column=0, sticky="W")

        self.filetype_entry = ttk.Entry(self.main_frame, width=40)
        self.filetype_entry.grid(row=4, column=1, columnspan=2, pady=5)

        self.output_directory_label = ttk.Label(self.main_frame, text="Output directory for Metagoofil:")
        self.output_directory_label.grid(row=5, column=0, sticky="W")

        self.output_directory_entry = ttk.Entry(self.main_frame, width=40)
        self.output_directory_entry.grid(row=5, column=1, columnspan=2, pady=5)

        self.social_domain_label = ttk.Label(self.main_frame, text="Domain for SocialRecon:")
        self.social_domain_label.grid(row=6, column=0, sticky="W")

        self.social_domain_entry = ttk.Entry(self.main_frame, width=40)
        self.social_domain_entry.grid(row=6, column=1, columnspan=2, pady=5)

        self.run_button = ttk.Button(self.main_frame, text="Run Omnisint", command=self.run_omnisint)
        self.run_button.grid(row=7, column=0, pady=10)

        self.output_text = tk.Text(self.main_frame, wrap="word", height=10, width=80)
        self.output_text.grid(row=8, column=0, columnspan=3, padx=(0, 10), pady=(0, 10))

    def run_omnisint(self):
        username = self.username_entry.get()
        email_or_username = self.email_entry.get()
        domain_or_ip = self.domain_entry.get()
        domain_metagoofil = self.domain_metagoofil_entry.get()
        filetype = self.filetype_entry.get()
        output_directory = self.output_directory_entry.get()
        social_domain = self.social_domain_entry.get()

        command = f"./omnisint_script.sh '{username}' '{email_or_username}' '{domain_or_ip}' '{domain_metagoofil}' '{filetype}' '{output_directory}' '{social_domain}'"
        try:
            process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            stdout, stderr = process.communicate()
            output = f"Command: {command}\n\nStandard Output:\n{stdout}\n\nStandard Error:\n{stderr}"
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, output)
        except Exception as e:
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, f"Error executing Omnisint script: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = OmnisintGUI(root)
    root.mainloop()

