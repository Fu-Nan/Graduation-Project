import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import base64
from io import BytesIO


class AppService:
    def __init__(self):
        # 数据加载
        self.df = pd.read_csv(r'D:\Python Work Files\Graduation Project\data\data.csv')
        # 数据清洗
        # 删除重复数据
        self.df = self.df.drop_duplicates()
        self.df["realSize"] = pd.to_numeric(self.df["size"].str[:-1])
        self.df["realSize"] = self.df["realSize"] * 1000 * 1000
        # 初始化图表,设置中文字体和图形颜色集
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False
        self.color = ['red', 'black', 'peru', 'orchid', 'deepskyblue']

    def getAppAnalysis(self):
        # 根据下载次数和推荐指数降序
        dfApp = self.df.sort_values(by=["download", "vote"], ascending=False)
        # 获取排名前10应用,存储图表所需数据
        dfApp = dfApp.head(10)
        # subplots可在一张图片绘制多个图表,fig表示整个图片,ax表示图片中各个图表
        fig, ax = plt.subplots(figsize=(20.4, 4.8))
        indexs = np.arange(len(dfApp["appName"]))
        ax.plot(indexs, dfApp["download"].values, label="下载数量")
        ax.plot(indexs, dfApp["realSize"].values, label="应用大小")
        ax.set_xticklabels(dfApp["appName"].values, {'fontsize': 14})
        ax.legend()
        fontSize = 16
        plt.xlabel('应用名称', fontSize=fontSize)
        plt.ylabel('下载次数和应用大小(MB)', fontSize=fontSize)
        plt.grid(True)
        # 将图表转换为Base64编码的字符串
        buffer = BytesIO()
        plt.savefig(buffer)
        data = buffer.getvalue()
        b64data = base64.b64encode(data)
        pltResult = "data:image/png;base64," + b64data.decode()
        return {
            "list": dfApp,
            "plt": pltResult
        }
