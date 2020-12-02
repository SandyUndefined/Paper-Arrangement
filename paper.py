from fpdf import FPDF

data = data2 = data3 = data4 = data5 = ""

with open('Section 1.txt') as p:
    data = p.read()
with open('Section 2.txt') as p:
    data2 = p.read()
with open('Section 3.txt') as p:
    data3 = p.read()
with open('Section 4.txt') as p:
    data4 = p.read()
with open('Section 5.txt') as p:
    data5 = p.read()

data += "\n"
data = data + data2 + data3 + data4 + data5

with open("result.txt",'w') as d:
    d.write(data)

pdf = FPDF()

pdf.add_page()


pdf.set_font("Arial", size=15)

f = open("result.txt", "r")
for x in f:
    pdf.cell(200,10,txt=x,ln=1,align='C')

pdf.output("paper.pdf")
