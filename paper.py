from fpdf import FPDF
import json

# Json to Dict
with open('data.json') as jf:
    data_dict = json.load(jf)

# Sorting Dict and Saving them in List
sorted_values = dict(sorted(data_dict.items(), key=lambda item: item[1]))
filenames = []
for i in sorted_values:
    filenames.append(f'{i}.txt')

# Convert text file into pdf
title = "Siliguri Institute of Technology"
sub_title = "Simpsoft Solutions"


class PDF(FPDF):
    def header(self):
        self.image(name='Logo.jpg', x=14, y=4, h=18, w=18)
        self.set_font('Arial', 'B', 21)
        self.set_text_color(r=5, g=57, b=107)
        self.text(62, 15, title)
        self.line(self.l_margin, self.t_margin, self.fw - self.r_margin, self.t_margin)
        self.line(self.l_margin, self.t_margin+1, self.fw - self.r_margin, self.t_margin+1)
        self.cell(0, 20, '', ln=1)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')

    def section(self, name):
        self.set_top_margin(25)
        self.set_font('Arial', 'B', 16)
        self.cell(0, 6, name[:-4], 0, 0, 'C', 0)
        self.cell(0, 12, '',ln=1)
        self.ln(4)

    def question(self, name):
        with open(name, 'r') as fh:
            txt = fh.read()
        self.set_font("Arial", '', size=12)
        self.multi_cell(0, 6, txt)
        self.ln()

    def print_paper(self, name):
        self.add_page()
        self.section(name)
        self.question(name)


pdf = PDF()
pdf.set_margins(left=15, top=25, right=15)
for x in filenames:
    pdf.print_paper(x)
pdf.output("paper.pdf")
