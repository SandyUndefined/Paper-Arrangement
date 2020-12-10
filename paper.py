# Github: https://github.com/SandyUndefined/Paper-Arrangement
# This programe is create by Sandeep Kumar Sharma
"""
Created by : Sandeep Kumar Sharma
Date : 02/12/2020
Github : https://github.com/SandyUndefined/Paper-Arrangement
LinkedIn : https://www.linkedin.com/in/sandeep-kumar-sharma-b44a92129/
"""

from fpdf import FPDF
import json

#  Convert Json file to dictionary
with open('data.json') as jf:
    data_dict = json.load(jf)

# Sorting dictionary and Saving them in List
sorted_values = dict(sorted(data_dict.items(), key=lambda item: item[1]))
filenames = []
for i in sorted_values:
    filenames.append(f'{i}.txt')

# Main
title = "Siliguri Institute of Technology"


class PDF(FPDF):
    # Header of the PDF
    def header(self):
        # Logo
        self.image(name='Logo.jpg', x=14, y=4, h=18, w=18)
        self.set_font('Arial', 'B', 21)
        self.set_text_color(r=5, g=57, b=107)
        # Title
        self.text(62, 15, title)
        # Underline
        self.line(self.l_margin, self.t_margin, self.fw - self.r_margin, self.t_margin)
        self.line(self.l_margin, self.t_margin+1, self.fw - self.r_margin, self.t_margin+1)
        self.cell(0, 20, '', ln=1)

    # Footer of the PDF
    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        # Page Number
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')

    # Section name from the List
    def section(self, name):
        self.set_top_margin(25)
        self.set_font('Arial', 'B', 16)
        self.cell(0, 6, name[:-4], 0, 0, 'C', 0)
        self.cell(0, 12, '', ln=1)
        self.ln(4)

    # Data of the text file
    def question(self, name):
        # Reading data from a file
        with open(name, 'r') as fh:
            txt = fh.read()
        self.set_font("Arial", '', size=12)
        self.multi_cell(0, 6, txt)
        self.ln()

    # Using this function to print one page at a time
    def print_paper(self, name):
        self.add_page()
        self.section(name)
        self.question(name)


# Instantiation of inherited class
pdf = PDF()
# Setting the initial margin
pdf.set_margins(left=15, top=25, right=15)
for x in filenames:
    # passing data from the list to a function
    pdf.print_paper(x)
# Saving output in PDF
pdf.output("paper.pdf")
