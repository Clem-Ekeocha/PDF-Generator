"""
The code below shows the step-bystep python programming process
of creating a pdf document with possible headers and footers.
"""

from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")          # Set the style of the pdf document
pdf.set_auto_page_break(auto=False, margin=0)                # This sets the page not to break automatically

df = pd.read_csv("topics.csv")                     # Read the csv file that contains the headers of each pdf page I want

for index, row in df.iterrows():                             # iterate over each row of the Topic.csv document
    pdf.add_page()

    #This code block sets the header of the main page pdf document
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)                        # Set RGB colour of choice
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)   # Assign each row as the text in each page of the pdf.
    pdf.line(10,21, 200,21)                                  # Set the cordinates of the line on the pdf document

    # This code block introduces a footer into the main page
    pdf.ln(265)                                              # Introduce a 265 break line
    pdf.set_font(family="Times", style="I", size=8)          # Set style to italics, size to 8 amd font to TimesNewRoman
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R", ln=1)   # Align footer to the right

    for i in range(row["Pages"]-1):             # This loop adds the requested no. of pages in the Topics.csv file
        pdf.add_page()

        # This code block introduces a footer into the added pages in the nested for loop
        pdf.ln(277)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R", ln=1)

pdf.output("output2.pdf")