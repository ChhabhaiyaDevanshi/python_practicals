from fpdf import FPDF

# save FPDF() class into
# a variable pdf
pdf = FPDF()

# Add a page
pdf.add_page()

# open the text file in read mode
f = open("marksheet.txt", "r")

pdf.set_font("Arial", size=16, style="B")
pdf.cell(200, 0, txt="MARKSHEET", ln=1, align="C")
pdf.set_font("Arial", size=10)
pdf.cell(200, 10, txt="SEMESTER-3", ln=1, align="C")

pdf.set_font("Arial", size=12, style="B")
pdf.cell(0, 10, txt="", ln=1)
pdf.cell(200, 0, txt="Name: Devanshi Chhabhaiya", ln=2)
pdf.cell(200, 10, txt="Id: 20CE011", ln=2)
pdf.cell(0, 10, txt="", ln=1)

pdf.set_font("Arial", size=12, style="B")
pdf.cell(145, 10, txt=" Course", border=1, ln=0)
pdf.cell(25, 10, txt=" Credits", border=1, ln=0)
pdf.cell(0, 10, txt=" Grades", border=1, ln=1)

pdf.set_font("Arial", size=10)

for x in f:
    arr = x.split(';')
    top = "T"
    if arr[0] == " ":
        top = ""

    pdf.cell(115, 10, txt=arr[0], border="L"+top, ln=0)
    pdf.cell(30, 10, txt=arr[1], border=top, ln=0)
    pdf.cell(25, 10, txt=arr[2], border="L"+top, ln=0)
    pdf.cell(0, 10, txt=arr[3], border="LR"+top, ln=1)

pdf.cell(0, 0, border="T")

pdf.output("DevanshiChhabhaiya.pdf")
