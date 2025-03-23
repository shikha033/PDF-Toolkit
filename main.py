import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfMerger, PdfReader, PdfWriter

# Functions for merging and splitting PDFs
def merge_pdfs():
    files = filedialog.askopenfilenames(title="Select PDFs to Merge", filetypes=[("PDF Files", "*.pdf")])
    if not files:
        return
    save_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
    if not save_path:
        return
    
    merger = PdfMerger()
    for pdf in files:
        merger.append(pdf)
    
    merger.write(save_path)
    merger.close()
    messagebox.showinfo("Success", "PDFs Merged Successfully!")

def split_pdf():
    file = filedialog.askopenfilename(title="Select PDF to Split", filetypes=[("PDF Files", "*.pdf")])
    if not file:
        return
    output_folder = filedialog.askdirectory(title="Select Output Folder")
    if not output_folder:
        return
