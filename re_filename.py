# ファイルネーム順にソートし、ファイルネームを連番に置き換える

import glob
import os
import tkinter as tk
from tkinter import filedialog as fd

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        master.geometry("500x120")
        self.pack(expand=1, fill=tk.BOTH)
        master.title("ファイル名を連番に変更")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.lb1 = tk.Label(self, text="フォルダ選択")
        self.lb1.place(x=10, y=20)
        self.en1 = tk.Entry(self, width=60)
        self.en1.place(x=80, y=20)
        self.bt1 = tk.Button(self, text="開く", command=self.open_dialog)
        self.bt1.place(x=450, y=15)
        self.bt2 = tk.Button(self, text='スタート', command=self.process_start)
        self.bt2.place(x=230,y=50)



    def open_dialog(self):
        global f_path
        f_path = fd.askdirectory()
        if f_path:
            self.en1.insert(tk.END, f_path)
            print(f_path)
    
    def process_start(self):
        root.quit()


root = tk.Tk()
app = Application(master=root)
root.geometry("500x120+300+250")

root.mainloop()



dirname = f_path
file_name_list = glob.glob(dirname + "/*")
file_name_list.sort()
print(file_name_list)

i = 1
for file_name in file_name_list:

    zero_i = "{0:010d}".format(i)

    new_file_name = zero_i + ".CSV"
    os.rename(file_name, dirname + "/" + new_file_name)

    i = int(i)

    i += 1

new_file = glob.glob(dirname)
print(file_name_list)