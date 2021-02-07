# -*- coding:UTF-8 -*-
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号



def draw_pic(x_col,y_col,hue_col,df_,title,pic_name):
	ax = sns.barplot(x =x_col, y = y_col,hue =hue_col,data=df_)
	ax.set(title=title)
	# 添加数据标签
	for rect in ax.patches:
	    height = int(rect.get_height())
	    ax.annotate('{}%'.format(height),
	                xy=(rect.get_x() + rect.get_width() / 2, height),
	                xytext=(0, 1.2),  # 3 points vertical offset
	                textcoords="offset points",
	                ha='center', va='bottom')
	# plt.show()
	plt.figure() # 连续保存多个图片用否则会错乱
	fig = ax.get_figure()
	ax.figure.savefig(f'{save_path}{pic_name}.png')
	# plt.savefig(f'{save_path}{pic_name}.png')
