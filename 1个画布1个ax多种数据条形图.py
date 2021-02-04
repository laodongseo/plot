# -*- coding:UTF-8 -*-
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# 显示中文标签
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
plt.rcParams['font.size'] = 14



# 画图
def draw_pic(list_data_rects,labels,xlabel,ylabel,title,rect_width = 0.2):
    n = len(list_data_rects)
    # x轴初始刻度位置
    x_init = np.arange(len(labels))
    # the width of the bars
    rect_width = 0.2

    fig, ax = plt.subplots(figsize=(10, 10))
    # 定位左侧的坐标(图形中心为坐标基准)
    x_left = x_init - rect_width / 2 * (n - 1)
    y_left = list_data_rects[0]
    rect_left = ax.bar(x_left, list_data_rects[0][1], rect_width, label=list_data_rects[0][0])
    autolabel(rect_left,ax)

    for i in range(1, n):
        x_now = x_left + rect_width * i
        print(x_now)
        label_now, y_now = list_data_rects[i]
        rect_one = ax.bar(x_now, y_now, rect_width, label=label_now)
        autolabel(rect_one,ax)

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel(ylabel)
    ax.set_xlabel(xlabel)
    ax.set_title(title)
    ax.set_xticks(x_init)
    ax.set_xticklabels(labels)
    ax.legend()
    fig.tight_layout()


# 数据标签添加
def autolabel(rects,ax):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

if __name__ == "__main__":
    # x轴的刻度标签;x标签,y标签,title
    dic_lable = {'labels':['20200101', '20200102', '20200103', '20200104', '20200105'],'xlabel':'哈哈','ylabel':'分数',
     'title':'Scores by group and gender'}

    # 分类数据-a类数据列表对应x轴刻度labels五个点的数据
    type1_data1 = ('a', [20, 34, 30, 35, 27])
    type2_data2 = ('b', [25, 32, 34, 20, 25])
    type3_data3 = ('c', [26, 38, 30, 18, 20])
    type4_data4 = ('d', [28, 35, 33, 13, 22])
    list_data_rects = [type1_data1, type2_data2, type3_data3, type4_data4]


    ax = draw_pic(list_data_rects,**dic_lable)
    plt.show()
