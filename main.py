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
