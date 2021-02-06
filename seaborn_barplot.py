# -*- coding:UTF-8 -*-
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号


df = pd.read_excel('111.xlsx')
ax = sns.barplot(x = 'top1-10', y = 'count',hue ='domains',data=df)
ax.set(title='5i5j.com及竞品top1——10排名分布')
# 添加数据标签
for rect in ax.patches:
    height = int(rect.get_height())
    ax.annotate('{}'.format(height),
                xy=(rect.get_x() + rect.get_width() / 2, height),
                xytext=(0, 0.2),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom')
# plt.show()
plt.savefig('./5.png')
