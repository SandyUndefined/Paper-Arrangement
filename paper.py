from fpdf import FPDF

# 5 Text files into 1 Text
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

with open("result.txt", 'w') as d:
    d.write(data)

# Convert text file into pdf

title = "Siliguri Institute of Technology"
sub_title = "Simpsoft Solutions"


class PDF(FPDF):
    # Page Header
    def header(self):
        # Logo
        self.image(name='Logo.jpg', x=14, y=4, h=18, w=18)
        # Arial bold 15
        self.set_font('Arial', 'B', 21)
        self.set_text_color(r=5, g=57, b=107)
        # Title
        self.text(62, 15, title)
        self.line(self.l_margin, self.t_margin, self.fw - self.r_margin, self.t_margin)
        self.line(self.l_margin, self.t_margin+1, self.fw - self.r_margin, self.t_margin+1)

    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')


pdf = PDF()
pdf.set_margins(left=15, top=25, right=15)
pdf.add_page()

pdf.set_font("Arial", size=12)

f = open("result.txt", "r")
for x in f:
    pdf.cell(200, 10, txt=x, ln=1, align='L')

pdf.output("paper.pdf")
