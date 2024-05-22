from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")          # Set the style of the pdf document

df = pd.read_csv("topics.csv")                     # Read the csv file that contains the headers of each pdf page I want

for index, row in df.iterrows():                             # iterate over each row of the Topic.csv document
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)                        # Set RGB colour of choice
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)   # Assign each row as the text in each page of the pdf.
    pdf.line(10,21, 200,21)                                  # Set the cordinates of the line on the pdf document

pdf.output("output2.pdf")