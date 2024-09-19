import sys
import subprocess
import importlib

def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def ensure_dependencies():
    required_packages = ['tkinter', 'tkinterdnd2', 'chardet']
    for package in required_packages:
        try:
            importlib.import_module(package)
        except ImportError:
            print(f"Installing {package}...")
            install_package(package)

# Ensure all dependencies are installed before proceeding
ensure_dependencies()

import os
import re
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinterdnd2 import DND_FILES, TkinterDnD
import chardet

class SQLCommentRemover:
    @staticmethod
    def detect_encoding(file_path):
        with open(file_path, 'rb') as file:
            raw_data = file.read()
        result = chardet.detect(raw_data)
        return result['encoding']

    @staticmethod
    def remove_comments(sql_content):
        sql_content = re.sub(r'--.*?$|/\*[\s\S]*?\*/', '', sql_content, flags=re.MULTILINE)
        sql_content = re.sub(r'[ \t]+$', '', sql_content, flags=re.MULTILINE)  
        return sql_content.strip()

    @classmethod
    def process_file(cls, input_file):
        try:
            encoding = cls.detect_encoding(input_file) or 'utf-8'
            
            with open(input_file, 'r', encoding=encoding) as file:
                sql_content = file.read()
            
            sql_without_comments = cls.remove_comments(sql_content)
            
            output_file = os.path.join(os.path.dirname(input_file),
                                       f"{os.path.splitext(os.path.basename(input_file))[0]}_without_comments.sql")
            
            with open(output_file, 'w', encoding='utf-8') as file:
                file.write(sql_without_comments)
            
            return f"Processed: {input_file}\nSaved: {output_file}\n"
        except Exception as e:
            return f"Error processing {input_file}: {str(e)}\n"

class SQLCommentRemoverGUI:
    def __init__(self, master):
        self.master = master
        master.title("SQL Comment Remover v3.0")
        master.geometry("600x400")
        master.resizable(False, False)  # Fija el tamaño de la ventana
        master.configure(bg='black')

        self.files = []
        self.create_widgets()

        self.master.drop_target_register(DND_FILES)
        self.master.dnd_bind('<<Drop>>', self.drop)

    def create_widgets(self):
        self.frame = tk.Frame(self.master, bg='black')
        self.frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        self.title_label = tk.Label(self.frame, text="SQL Comment Remover", fg='green', bg='black', font=("Courier", 18, "bold"))
        self.title_label.pack(pady=5)

        # Ajustamos el tamaño del área de texto para adaptarse mejor a la ventana fija
        self.text_area = tk.Text(self.frame, height=12, width=65, bg='black', fg='green', font=("Courier", 10))
        self.text_area.pack(pady=10)
        self.text_area.insert(tk.END, "Drag and drop SQL files here or click 'Select Files'...\n")

        self.select_button = tk.Button(self.frame, text="Select Files", command=self.select_files, bg='green', fg='black', font=("Courier", 12))
        self.select_button.pack(pady=5)

        self.process_button = tk.Button(self.frame, text="Process Files", command=self.process_files, bg='green', fg='black', font=("Courier", 12))
        self.process_button.pack(pady=5)

    def select_files(self):
        filetypes = (("SQL files", "*.sql"), ("All files", "*.*"))
        files = filedialog.askopenfilenames(filetypes=filetypes)
        self.files.extend(files)
        self.update_text_area()

    def drop(self, event):
        self.files.extend(self.master.tk.splitlist(event.data))
        self.update_text_area()

    def update_text_area(self):
        self.text_area.delete(1.0, tk.END)
        for file in self.files:
            self.text_area.insert(tk.END, f"{file}\n")

    def process_files(self):
        if not self.files:
            messagebox.showwarning("Warning", "No files selected.")
            return

        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, "Processing files...\n")
        self.master.update()

        for file in self.files:
            result = SQLCommentRemover.process_file(file)
            self.text_area.insert(tk.END, result)
            self.master.update()

        self.files = []
        messagebox.showinfo("Process Completed", "All files have been processed.")

def main():
    root = TkinterDnD.Tk()
    SQLCommentRemoverGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
