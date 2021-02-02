# -*- coding:UTF-8 -*-
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# 显示中文标签
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False



# 画图
def draw_pics(list_data_rects,labels,xlabel,ylabel,title,rect_width = 0.4):
    # 数据源的个数
    n = len(list_data_rects)
    one_row_num = 3 # 1行设置的绘图区域个数(列数)
    nrows = int(n/one_row_num) if n % one_row_num==0 else int(n/one_row_num) + 1
    ncols = one_row_num
    # x轴初始刻度位置
    x_init = np.arange(len(labels))
    # bar的宽度
    rect_width = rect_width
    # 画布及画布上分割的绘图区域
    fig, axes = plt.subplots(figsize=(15, 25),nrows=nrows,ncols=ncols)
    # axes的绘图区域位置点
    lis_loc = [(x, y) for x in range(nrows) for y in range(ncols) ]
    # 每个区域绘图
    i = 0
    for x,y in lis_loc:
        print(x,y)
        ax = axes[x,y]
        label_now, y_now = list_data_rects[i] if i+1 <= n else ('',x_init * 0) # 防止数据源个数小区区域个数
        rect_one = ax.bar(x_init,y_now, rect_width, label=label_now)
        auto_label(rect_one,ax)
        ax.set_ylabel(ylabel)
        ax.set_xlabel(xlabel)
        ax.set_title(title)
        ax.set_xticks(x_init)
        ax.set_xticklabels(labels)
        ax.legend()
        i+=1

    fig.tight_layout(pad=7)


# 数据标签添加
def auto_label(rects,ax):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


if __name__ == "__main__":
    # x轴的刻度序列标签;x标签,y标签,title
    dic_lable = {'labels':['20210101', '20210102', '20210103', '20210104', '20210105'],'xlabel':'','ylabel':'首页率',
     'title':'小区词'}

    # 分类的数据
    type1_data1 = ('a', [20, 34, 30, 35, 27])
    type2_data2 = ('b', [25, 32, 34, 20, 25])
    type3_data3 = ('c', [26, 38, 30, 18, 20])
    type4_data4 = ('d', [28, 35, 33, 13, 22])
    type5_data5 = ('e', [25, 31, 31, 14, 20])
    list_data_rects = [type1_data1, type2_data2, type3_data3, type4_data4,type5_data5]

    ax = draw_pics(list_data_rects,**dic_lable)
    plt.show()
