#　圧縮カーブを自動描写　１枚にまとめる
# matplotlib オブジェクト指向バージョン


import glob
import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog as fd
import matplotlib.pyplot as plt
import japanize_matplotlib
import sys
# import plot_max
from tqdm import tqdm
import cal_correlation
import PySimpleGUI as sg

class Make_graph:
    def __init__(self, f_path, kaju, heni, saika, g_titile, graph):
        """

        :param f_path: csvファイルのフォルダパス
        :param kaju: 荷重レンジの値
        :param heni: 変位レンジの値
        :param saika: 載荷量の値
        :param g_titile: グラフタイトル
        :param graph: S-S曲線の有無
        """
        self.f_path = f_path
        self.kaju = kaju
        self.heni = heni
        self.saika = saika
        self.g_title = g_titile
        self.x_data_list = []
        self.y_data_list = []
        self.graph = graph
        if graph == '有り':
            self.make_graph()
        if graph == "無し":
            self.no_graph()

    def make_graph(self):
        # CSVファイルのファイル名とファイル数を取得
        csv_dir_path = self.f_path + "/*"
        csv_file_names = glob.glob(csv_dir_path)
        csv_file_names.sort()

        # print(csv_file_names)
        no_of_files = len(csv_file_names)


        # csvフォルダ内のCVSを順番に開いてプロット

        if self.kaju == "50" or self.kaju == "25" or self.kaju == "10" or self.kaju == "2.5":
            kaju_range = 5
        elif self.kaju == "1" or self.kaju == "0.25":
            kaju_range = 0.1
        elif self.kaju == "0.1":
            kaju_range = 0.05
        else:
            sg.popup_error("荷重レンジが間違っています")
            sys.exit()

        if self.heni == "400":
            heni_range = 40
        elif self.heni == "40":
            heni_range = 4
        elif self.heni == "4":
            heni_range = 0.4
        else:
            sg.popup_error("変位レンジが間違っています")
            sys.exit()

        # グラフ描画用の枠を作成
        fig, ax = plt.subplots(figsize=(12,8))
        ax.grid()
        ax.set_title(self.g_title)
        ax.set_xlabel("変位")
        ax.set_ylabel('加重')

# ch1=荷重データ、ch2=変位データ　データロガーの配置通りの指定にしている
        sample_no = 1
        for csv_name in tqdm(csv_file_names):
            csv_file = pd.read_csv(csv_name, skiprows=14, usecols=[1,2], names=["ch1", "ch2"])
            df = pd.DataFrame(csv_file)

            df1 = df["ch1"] * kaju_range
            df2 = df["ch2"] * heni_range
            cal_df = pd.concat([df2, df1], axis=1)
            kaju_max_index = cal_df["ch1"].idxmax()
            kaju_max_index = int(kaju_max_index)
            heni_max = cal_df.at[kaju_max_index, 'ch2']

            hosei_value = heni_max - self.saika
            df2 = cal_df["ch2"] - hosei_value
            comp_cal_df = pd.concat([df2, df1], axis=1)
            # print(comp_cal_df.max())
            # print(x)

            # 変位データのリスト化
            self.x_data = comp_cal_df["ch2"].values.tolist()
            # 荷重データのリスト化
            self.y_data = comp_cal_df["ch1"].values.tolist()

            # print('補正値は{}'.format(hosei_value))

            sample_no = str(sample_no)
            # plt.plot(x_data, y_data, antialiased=True, label=sample_no)
            # plt.legend()

            ax.plot(self.x_data, self.y_data, label=sample_no)
            ax.legend(loc=0)

            sample_no = int(sample_no)

            cal_csv_name = self.f_path + "/" + "cal" + str(sample_no) + ".csv"

            comp_cal_df.to_csv(cal_csv_name)

            # plot_max へ渡す　リストを作成
            kaju_data = cal_df["ch1"].max()
            # heni_data = cal_df["ch2"].max()
            # x_data_list.append(heni_data)
            self.y_data_list.append(kaju_data)

            # ファイルネームのカウントアップ
            sample_no += 1


        fig.tight_layout()
        plt.show()

        # plot_maxにリストを渡す
        cal_correlation.cal_Cor(self.y_data_list)
        # plot_max.plot_max(y_data_list)
        # cal_correlation2.cal_Cor(y_data_list)

# pyinstallerはスペックシートで

    def no_graph(self):
        # CSVファイルのファイル名とファイル数を取得
        csv_dir_path = self.f_path + "/*"
        csv_file_names = glob.glob(csv_dir_path)
        csv_file_names.sort()

        # print(csv_file_names)
        no_of_files = len(csv_file_names)


        # csvフォルダ内のCVSを順番に開いてプロット

        if self.kaju == "50" or self.kaju == "25" or self.kaju == "10" or self.kaju == "2.5":
            kaju_range = 5
        elif self.kaju == "1" or self.kaju == "0.25":
            kaju_range = 0.1
        elif self.kaju == "0.1":
            kaju_range = 0.05
        else:
            sg.popup_error("荷重レンジが間違っています")
            sys.exit()

        if self.heni == "400":
            heni_range = 40
        elif self.heni == "40":
            heni_range = 4
        elif self.heni == "4":
            heni_range = 0.4
        else:
            sg.popup_error("変位レンジが間違っています")
            sys.exit()

# ch1=荷重データ、ch2=変位データ　データロガーの配置通りの指定にしている
        sample_no = 1
        for csv_name in tqdm(csv_file_names):
            csv_file = pd.read_csv(csv_name, skiprows=14, usecols=[1,2], names=["ch1", "ch2"])
            df = pd.DataFrame(csv_file)

            df1 = df["ch1"] * kaju_range
            df2 = df["ch2"] * heni_range
            cal_df = pd.concat([df2, df1], axis=1)
            kaju_max_index = cal_df["ch1"].idxmax()
            kaju_max_index = int(kaju_max_index)
            heni_max = cal_df.at[kaju_max_index, 'ch2']

            hosei_value = heni_max - self.saika
            df2 = cal_df["ch2"] - hosei_value
            comp_cal_df = pd.concat([df2, df1], axis=1)
            # print(comp_cal_df.max())
            # print(x)

            # 変位データのリスト化
            self.x_data = comp_cal_df["ch2"].values.tolist()
            # 荷重データのリスト化
            self.y_data = comp_cal_df["ch1"].values.tolist()

            # print('補正値は{}'.format(hosei_value))

            sample_no = str(sample_no)
            sample_no = int(sample_no)

            cal_csv_name = self.f_path + "/" + "cal" + str(sample_no) + ".csv"

            comp_cal_df.to_csv(cal_csv_name)

            # plot_max へ渡す　リストを作成
            kaju_data = cal_df["ch1"].max()
            # heni_data = cal_df["ch2"].max()
            # x_data_list.append(heni_data)
            self.y_data_list.append(kaju_data)

            # ファイルネームのカウントアップ
            sample_no += 1

        # plot_maxにリストを渡す
        cal_correlation.cal_Cor(self.y_data_list)
        # plot_max.plot_max(y_data_list)
        # cal_correlation2.cal_Cor(y_data_list)
