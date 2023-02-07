from openpyxl.chart import LineChart,Reference
from openpyxl import Workbook
wb=Workbook()
sheet=wb.active

sales_data=[
    ["Year","Sales"],
    [2010,10000],
    [2011,90000],
    [2012,20000],
    [2013,30000],
    [2014,60000],
    [2015,55000]
]
for row in sales_data:
    sheet.append(row)

chart=LineChart()
data=Reference(worksheet=sheet,min_row=1,max_row=7,min_col=1,max_col=2)
chart.add_data(data,titles_from_data=True)
sheet.add_chart(chart,"E2")
wb.save("c:/hcl2/linechart.xlsx")
