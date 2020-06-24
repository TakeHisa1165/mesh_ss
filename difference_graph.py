import xlwings as xw
from tqdm import tqdm


excel_path = r"D:\デスクトップ\会社関係\CSV仮置き\sample.xlsx"
wb = xw.Book(excel_path)
ws = wb.sheets(1)


max_row = ws.range(100000, 22).end("up").row

for i in tqdm(range(2, max_row)):
    data1 = ws.range(i, 22).value
    data2 = ws.range(i + 1, 22).value
    ws.range(i, 23).value = data1- data2

wb.save()

# x_range = "U2:U" + str(max_row)
# y_range = "x2:x" + str(max_row)

# chart = ws.charts.add(left=150, top=50, height=400, width=800)
# chart.chart_type = 'xy_scatter'
# chart.set_source_data(ws.range((x_range), ws.range(y_range)))
