

from fpdf import FPDF



#header and footer method

class PDF(FPDF):
    def header(self):
        #logo
        #self.image("Formode.png",10,8, 25)
        #font
        self.set_font("helvetica", "B", 20)
        #Title
        self.cell(0,10, "CLIENT'S BRIEF", border = True, ln=1, align="C")
        # line break
        self.ln(20)


# PART 1

# Create a fpdf object and specify
#layout, unit and format
pdf = PDF("P", "mm", "A4")

#set auto page break
pdf.set_auto_page_break(auto=True, margin = 40)

# add page
pdf.add_page()

# specify font  and type and size
pdf.set_font("helvetica", "", 16)
#pdf.set_text_color(220, 50, 50)

# add text (single cell or multiple cell)
#cell(width , height, text)

#cursor move to the next line
# move to the next line, cursor move to the next line ( LN = True)
# border argument
#pdf.cell(120,100, "Hello world", ln=True, border=True)



for x in range(1,41):
    pdf.cell(0,10, f"This is line {x} :D ", ln=True)



# the next line

pdf.output("sample2.pdf")



# PART 2

