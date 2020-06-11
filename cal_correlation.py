import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


def cal_Cor(y_value):
    
    x_data_list = []
    for shot_No in range(len(y_value)):
        shot_numbrs = shot_No + 1
        x_data_list.append(shot_numbrs)
        x_value = x_data_list

    x = pd.Series(x_value)
    y = pd.Series(y_value)
    df = pd.concat([x, y], axis=1)

    global ans
    anser = x.corr(y)
    ans = "相関係数={}".format(anser)
    print(ans)

    dirname = r"D:\デスクトップ\会社関係\CSV仮置き"

    f_path = dirname + "/" + "test.csv"

    df.to_csv(f_path)

    csv_file = pd.read_csv(f_path, names=["No", "Strength"], skiprows=1)
    df2 = pd.DataFrame(csv_file)
    print(df2)

    lr = LinearRegression()

    # 一次元で渡す事を明確に　n_data_x = n_data_x.reshape(-1, 1)
    n_data_x = df2["No"].values
    n_data_x = n_data_x.reshape(-1, 1)
    strength_data_y = df2["Strength"].values
    strength_data_y = strength_data_y.reshape(-1, 1)


    lr.fit(n_data_x, strength_data_y)

    print("回帰変数{}".format(lr.coef_))
    print("切片{}".format(lr.intercept_))
    r2 = lr.score(n_data_x, strength_data_y)
    print("決定係数{}".format(r2))


    fig, ax = plt.subplots(figsize=(12,8))
    ax.grid()
    ax.text(20.0, 0.4, ans)
    ax.set_title('変位ー荷重　散布図')
    ax.set_xlabel('繰り返し数')
    ax.set_ylim(0, 1)
    ax.set_ylabel('荷重[KN]')
    ax.scatter(n_data_x, strength_data_y)
    ax.plot(n_data_x, lr.predict(n_data_x), color='red')
    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    pass
