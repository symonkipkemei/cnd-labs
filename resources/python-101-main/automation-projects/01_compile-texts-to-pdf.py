
import pathlib
from fpdf import FPDF

path = str(pathlib.Path.cwd())


pdf = FPDF()
pdf.add_page()
pdf.set_font("helvetica", "12")
pdf.cell(200,10,txt = "Hello Symon, you are doing great!", ln= 1,align = "C")
pdf.output(path + "sample.pdf")