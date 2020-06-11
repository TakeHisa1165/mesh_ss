# 　圧縮カーブを自動描写　１枚にまとめる
# matplotlib オブジェクト指向バージョン
# import glob
# import pandas as pd
# import numpy as np
import PySimpleGUI as sg
# import matplotlib.pyplot as plt
# import japanize_matplotlib
# import sys
# import plot_max
# from tqdm import tqdm
# import cal_correlation
# import cal_correlation2
import make_s_s_graph2


# フォルダ選択画面を描画

class MainWindow:
    def __init__(self):
        pass

    def main_window(self):
        sg.theme('systemdefault')

        frame1 = [
            [sg.Text("S-S曲線有り無し選択")],
            [sg.Radio('有り', key="-有り-", group_id=1)],
            [sg.Radio('無し', key="-無し-", group_id=1)],
        ]
        layout = [
            [sg.Text("フォルダ選択", font=('メイリオ', 14)), sg.InputText(size=(30, 1), font=('メイリオ', 14), key="-f_path"),
             sg.FolderBrowse(button_text="開く", font=("メイリオ", 14))],
            [sg.Text("荷重レンジ", font=('メイリオ', 14)), sg.InputText(size=(5, 1), font=('メイリオ', 14), key="-kaju-"),
             sg.Text("変位レンジ", font=('メイリオ', 14)), sg.InputText(size=(5, 1), font=('メイリオ', 14), key="-heni-"),
             sg.Text("載荷量", font=('メイリオ', 14)), sg.InputText(size=(5, 1), font=('メイリオ', 14), key="-saika-")],
            [sg.Text('グラフタイトル', font=('メイリオ', 14)), sg.InputText(size=(29, 1), font=('メイリオ', 14), key="-g_title-")],
            [sg.Frame("グラフ選択", frame1)],
            [sg.Submit(button_text='スタート', font=('メイリオ', 14), pad=((240, 0), (0, 0)))]
        ]

        window = sg.Window('圧縮データ集計', layout)

        while True:
            event, values = window.read()
            if event is None:
                print('Exit')
                break

            if event == "スタート":
                # フォルダパスを取得
                f_path = values["-f_path"]
                # 荷重レンジを取得
                kaju = values["-kaju-"]
                # 変位レンジを取得
                heni = values["-heni-"]
                # 載荷量を取得
                saika = values["-saika-"]
                saika = float(saika)
                # グラフタイトルを取得
                g_title = values["-g_title-"]
                if values['-有り-']:
                    graph = "有り"
                elif values["-無し-"]:
                    graph = "無し"
                make_s_s_graph2.Make_graph(f_path, kaju, heni, saika, g_title, graph)




        window.close()


if __name__ == "__main__":
    app = MainWindow()
    app.main_window()