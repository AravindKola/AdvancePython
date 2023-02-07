from openpyxl.chart import PieChart,Reference
from openpyxl import Workbook
wb=Workbook()
sheet=wb.active

covid_data=[
    ["country","per_cases"],
    ['india',22],
    ['China',48],
    ['Usa',25],
    ['japan',15]
]
for row in covid_data:
    sheet.append(row)
chart=PieChart()
data=Reference(worksheet=sheet,min_row=1,max_row=5,min_col=1,max_col=2)
chart.add_data(data,titles_from_data=True)
sheet.add_chart(chart,"E2")
wb.save("c:/hcl2/piechart.xlsx")
