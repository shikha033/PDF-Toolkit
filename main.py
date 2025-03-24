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
    
    reader = PdfReader(file)
    for i in range(len(reader.pages)):
        writer = PdfWriter()
        writer.add_page(reader.pages[i])
        output_filename = os.path.join(output_folder, f"page_{i + 1}.pdf")
        with open(output_filename, "wb") as output_file:
            writer.write(output_file)
    
    messagebox.showinfo("Success", "PDF Split Successfully!")

# GUI Setup
root = tk.Tk()
root.title("PDF Toolkit - Merge & Split")
root.geometry("450x400")
root.configure(bg="#2c3e50")  # Dark background

# Set the app icon
icon_path = "assets/icon.png"
try:
    icon = tk.PhotoImage(file=icon_path)
    root.iconphoto(True, icon)
except Exception as e:
    print("Error loading icon:", e)

# Stylish Header
header = tk.Label(root, text="📄 PDF TOOLKIT 📄", font=("Arial", 20, "bold"), fg="white", bg="#2c3e50")
header.pack(pady=15)

# Buttons with improved styling
btn_style = {"font": ("Arial", 14), "fg": "white", "bg": "#e74c3c", "width": 20, "height": 2, "bd": 3, "relief": "ridge"}

merge_btn = tk.Button(root, text="🔗 Merge PDFs", command=merge_pdfs, **btn_style)
merge_btn.pack(pady=10)

split_btn = tk.Button(root, text="✂ Split PDF", command=split_pdf, **btn_style)
split_btn.pack(pady=10)

exit_btn = tk.Button(root, text="❌ Exit", command=root.quit, **btn_style)
exit_btn.pack(pady=10)

root.mainloop()
