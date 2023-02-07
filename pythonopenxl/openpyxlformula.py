import openpyxl
from openpyxl.utils import FORMULAE
wb=openpyxl.load_workbook("c:/hcl2/demoopenxlwrite.xlsx")
sheet=wb.active
sheet["A7"]='=SUM(A1:A6)'
wb.save("c:/hcl2/newsheet.xlsx")