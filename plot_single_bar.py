# coding:utf8
"""
单图任意多个柱形图对比
x_labels长度==DictData数据源中列表的长度
"""
from matplotlib.figure import Figure
import numpy as np

# 显示中文标签
plt.rcParams["font.sans-serif"]=["SimHei"]
plt.rcParams["axes.unicode_minus"]=False
plt.rcParams["font.size"] = 12

# 数据源
DictData = {
'衣服':[20, 34, 30, 35, 27],
'裤子':[25, 32, 34, 20, 25],
'鞋子':[22, 11, 20, 28, 19],
'围巾':[30, 25, 28, 41, 14]
}
type_num = len(DictData)


x_labels = ['1月', '2月', '3月', '4月', '5月']
x = np.arange(len(x_labels))  # the label locations
width = 0.2 # the width of the bars

fig, ax = plt.subplots()
for type_name,type_values in DictData.items():
       juli = (type_num -1)/2 * width
       x_values  = x - juli
       # x_values代表bar图【中心点】的坐标
       rects = ax.bar(x_values, type_values, width, label=type_name)
       ax.bar_label(rects, padding=3)
       type_num -= 2

ax.set_xticks(x)
ax.set_xticklabels(x_labels)
ax.set_ylabel('Scores')
ax.set_title('Scores by group')
ax.legend()

fig.dpi = 80 # 每英尺多少像素
fig.set_size_inches(15,10) # 英尺
plt.show()
fig.savefig('11.png')
