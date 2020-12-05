from fpdf import FPDF
import json

# Json to Dict
with open('data.json') as jf:
    data_dict = json.load(jf)
print(data_dict)

# Sorting Dict and Saving them in List
sorted_values = dict(sorted(data_dict.items(), key=lambda item: item[1]))
filenames = []
for i in sorted_values:
    filenames.append(f'{i}.txt')

# Merging them in One txt file
with open('result.txt', 'w') as d:
    for i in filenames:
        with open(i) as s:
            d.write(s.read())
        d.write("\n")

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
        self.line(self.l_margin, self.t_margin + 1, self.fw - self.r_margin, self.t_margin + 1)

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
