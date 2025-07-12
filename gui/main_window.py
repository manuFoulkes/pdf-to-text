import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from services.pdf_to_text_pipeline import process_pdf_to_text
import os

class OCRApp:
    def __init__(self, root):
        self.root = root
        self.root.title("OCR y Corrección Ortográfica")
        self.root.geometry("500x300")

        self.label = tk.Label(root, text="Seleccioná un PDF para procesar:")
        self.label.pack(pady=10)

        self.select_button = tk.Button(root, text="Seleccionar PDF", command=self.seleccionar_pdf)
        self.select_button.pack(pady=5)

        self.filename_label = tk.Label(root, text="", wraplength=400)
        self.filename_label.pack(pady=5)

        self.process_button = tk.Button(root, text="Procesar PDF", command=self.procesar_pdf)
        self.process_button.pack(pady=10)
        
        self.progress_var = tk.IntVar()
        self.progress_bar = ttk.Progressbar(root, variable=self.progress_var, maximum=100)
        self.progress_bar.pack(pady=10, fill='x')
        
        self.open_folder_button = tk.Button(root, text="Ver carpeta de salida", command=self.open_output_folder)
        self.open_folder_button.pack(pady=5)
        self.pdf_path = None

    def select_pdf(self):
        path = filedialog.askopenfilename(filetypes=[("Archivos PDF", "*.pdf")])
        if path:
            self.pdf_path = path
            self.filename_label.config(text=os.path.basename(path))

    def process_pdf(self):
        if not self.pdf_path:
            messagebox.showwarning("Advertencia", "Primero seleccioná un archivo PDF.")
            return

        output_path = process_pdf_to_text(self.pdf_path, on_progress_update=self.update_progress)
        
        if output_path:
            messagebox.showinfo("Éxito", f"Archivo generado:\n{output_path}")
        else:
            messagebox.showerror("Error", "Ocurrió un error durante el procesamiento.")
            
    def update_progress(self, percent):
        self.progress_var.set(percent)
        self.root.update_idletasks()
        
    def open_output_folder(self):
        output_dir = os.path.abspath("output")
        
        if not os.path.exists(output_dir):
            messagebox.showwarning("Carpeta no encontrada")
        
        os.startfile(output_dir)

def run_app():
    root = tk.Tk()
    app = OCRApp(root)
    root.mainloop()