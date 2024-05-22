from fpdf import FPDF           # import the fpdf class of the fpdf module

pdf = FPDF(orientation="P", unit="mm", format="A4") # Set orientation to Portrait, format as A4 paper

pdf.add_page()                  # Create a new page

pdf.set_font(family="Times", style="B", size=12)    # Set font to size 12 Bold TimesNewRoman
pdf.cell(w=0, h=12, txt="Hello There!",             # Set width, height, text, alignemnt to left, breakline and border line weight
         align="L", ln=1, border=1)

pdf.set_font(family="Times", size=12)               # Excluded the bold style to spot the difference
pdf.cell(w=0, h=12, txt="How are you doing?",
         align="L", ln=1, border=1)

pdf.output("output.pdf")


