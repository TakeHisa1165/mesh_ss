import pandas as pd
import xlwings as xw


file_path = r"D:\デスクトップ\会社関係\CSV仮置き\test.csv"
csv_file = pd.read_csv(file_path, usecols=[1, 2], names=["回数", "最大荷重"], skiprows=1)
# csv_df = csv_file["最大荷重"]


excel_path = r"D:\デスクトップ\会社関係\CSV仮置き\sample.xlsx"
wb1 = xw.Book(excel_path)
ws1 = wb1.sheets(1)
csv_row = len(csv_file) + 1
ws1.range("U1").value = csv_file

print(type(csv_file))
print(csv_file.max())

ws1.range('U:U').api.Delete()

# 文字列と数字を繋いでセルの最終番地までをしてい
x_range = "U2:U" + str(csv_row)
y_range = "V2:V" + str(csv_row)

chart = ws1.charts.add(left=150, top=50, height=400, width=800)
chart.chart_type = 'xy_scatter'
chart.set_source_data(ws1.range((x_range), ws1.range(y_range)))

