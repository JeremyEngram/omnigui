#!/usr/bin/env python3

import os
import subprocess
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

class ScriptManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Script Manager")
        self.script_directories = ["/opt", "/usr/local/bin"]

        # Create widgets
        self.create_widgets()

        # Load script list
        self.load_scripts()

    def create_widgets(self):
        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky="NSEW")

        self.script_listbox = tk.Listbox(self.main_frame, width=50, height=15)
        self.script_listbox.grid(row=0, column=0, columnspan=3, padx=(0, 10), pady=(0, 10))

        self.execute_button = ttk.Button(self.main_frame, text="Execute", command=self.execute_script)
        self.execute_button.grid(row=1, column=0, sticky="W")

        self.open_button = ttk.Button(self.main_frame, text="Open", command=self.open_script)
        self.open_button.grid(row=1, column=1)

        self.refresh_button = ttk.Button(self.main_frame, text="Refresh", command=self.load_scripts)
        self.refresh_button.grid(row=1, column=2, sticky="E")

    def load_scripts(self):
        self.script_listbox.delete(0, tk.END)
        scripts = self.find_scripts()
        for script in scripts:
            self.script_listbox.insert(tk.END, script)

    def find_scripts(self):
        scripts = []
        for directory in self.script_directories:
            try:
                for entry in os.scandir(directory):
                    if entry.is_file() and os.access(entry.path, os.X_OK):
                        scripts.append(entry.path)
            except FileNotFoundError:
                pass

        return scripts

    def execute_script(self):
        selected_script = self.script_listbox.get(self.script_listbox.curselection())
        if not selected_script:
            messagebox.showerror("Error", "No script selected.")
            return

        try:
            subprocess.Popen([selected_script], stderr=subprocess.PIPE, stdout=subprocess.PIPE)
            messagebox.showinfo("Success", f"Script '{selected_script}' executed.")
        except Exception as e:
            messagebox.showerror("Error", f"Error executing script: {str(e)}")

    def open_script(self):
        selected_script = self.script_listbox.get(self.script_listbox.curselection())
        if not selected_script:
            messagebox.showerror("Error", "No script selected.")
            return

        editor = os.environ.get("EDITOR", "xdg-open")
        subprocess.Popen([editor, selected_script])

if __name__ == "__main__":
    root = tk.Tk()
    app = ScriptManager(root)
    root.mainloop()
