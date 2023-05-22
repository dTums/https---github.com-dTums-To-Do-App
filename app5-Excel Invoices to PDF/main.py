import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

pdf = FPDF(orientation="p", unit="mm", format="A4")

filepaths = glob.glob("Invoices/*.xlsx")


for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    pdf = FPDF(orientation="p", unit="mm", format="A4")
    pdf.add_page()
    filename = Path(filepath).stem
    Invoice_No = filename.split("-")[0]
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Invoice Number {Invoice_No}")
    pdf.output(f"PDF_Outputs {filename}.pdf")
