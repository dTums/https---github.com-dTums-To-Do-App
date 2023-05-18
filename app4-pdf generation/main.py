from fpdf import FPDF

import pandas as pd

pdf = FPDF(orientation="p", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)


df = pd.read_csv('topics.csv')

for index, row in df.iterrows():
    # set the header
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    # add lines to master pages
    for y in range (21, 289, 10):
        pdf.line(10, y, 200, y)


    # set the footer for the master page
    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=10)
    pdf.set_text_color(150, 150, 150)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")




    for i in range(row["Pages"]-1):
        pdf.add_page()

        # set the footer for the other pages
        pdf.ln(277)
        pdf.set_font(family="Times", style="I", size=10)
        pdf.set_text_color(150, 150, 150)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")
        pdf.line(10, 289, 200, 289)

        # add lines to other pages
        for y in range(21, 289, 10):
            pdf.line(10, y, 200, y)

pdf.output("output.pdf")
