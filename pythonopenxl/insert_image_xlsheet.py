from openpyxl import load_workbook
from openpyxl.drawing.image import Image

workbook=load_workbook(filename="c:/hcl2/demoopenxlwrite.xlsx")
sheet=workbook.active

logo=Image("c:/hcl2/hcllogo.png")

logo.height=150
logo.width=150

sheet.add_image(logo,"D10")
workbook.save(filename="c:/hcl2/hcllogo.xlsx")