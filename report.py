import webbrowser
import os
from fpdf import FPDF

class PdfReport:
    """
    Creates a Pdf file that contains data about
    document such as title, date, bodytext, signature.
    """

    def __init__(self, docname):
        self.docname = docname

    def generate(self, document):
        pdf = FPDF(orientation="P", unit="pt", format="A4")
        pdf.add_page()

        # Insert pic
        pdf.image("pic.png", w=0, h=30)

        # Insert date
        pdf.set_font(family="Arial", size=10)
        pdf.cell(w=0, h=15, txt=document.date, border=0, align="R", ln=1)

        # Insert name above address
        pdf.set_font(family="Arial", size=10, style='B')
        pdf.cell(w=100, h=15, txt=document.name, border=0, ln=1)

        # Insert address1
        pdf.set_font(family="Arial", size=10)
        pdf.cell(w=100, h=15, txt=document.address1, border=0, ln=1)

        # Insert address1
        pdf.set_font(family="Arial", size=10)
        pdf.cell(w=100, h=15, txt=document.address2, border=0, ln=1)

        # Insert title
        pdf.set_font(family='Times', size=24)
        pdf.cell(w=0, h=120, txt=document.title, border=0, align="C", ln=1)

        # Insert space
        pdf.set_font(family="Arial", size=10)
        pdf.cell(w=100, h=50, border=0)

        # Insert paragraph
        pdf.set_font(family="Arial", size=10)
        pdf.multi_cell(w=400, h=15, txt=document.paragraph, border=0)

        # Insert space
        pdf.set_font(family="Arial", size=10)
        pdf.cell(w=0, h=80, border=0, align="R", ln=1)

        # Insert signature
        pdf.set_font(family="Arial", size=10)
        pdf.cell(w=500, h=15, txt="Yours sincerely", border=0, align="R", ln=1)

        # Insert signature
        pdf.set_font(family="Arial", size=10, style="B")
        pdf.cell(w=500, h=15, txt=document.name, border=0, align="R")

        # Change directory to files, generate and open the PDF
        pdf.output(self.docname)
        webbrowser.open(self.docname)