# coding:utf8
"""
绘制多图
每个子图构成如下：
	x_labels = ['报名量','拉新量'] # 和axDictDate中值列表元素个数一致
	axDictDate = {'type1':[v1,v2],'type2':[v1,v2]} #type1代表一种业务,v1和v2是该业务的报名量、拉新量
	x_labels和axDictDate可以同时增删元素
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# 显示中文标签
plt.rcParams["font.sans-serif"]=["SimHei"]
plt.rcParams["axes.unicode_minus"]=False
plt.rcParams["font.size"] = 15
my_header = {
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110.Safari/537.36',
}



def read_csv(file_path='心愿单活动明细表.csv'):
	try:
		df = pd.read_csv(file_path,encoding='GBK',sep=',')[['城市','业务线','报名量','拉新量']].copy()
	except Exception as e:
		df = pd.read_csv(file_path,encoding='utf-16',sep='\t')[['城市','业务线','报名量','拉新量']].copy()
	df = df[df['城市'].isin(['北京','上海','杭州','南京','苏州','太原','天津','无锡'])].copy()
	return df



# 每个子ax绘图
def draw_sub(ax,ax_name,axDictData,x_labels,width=0.2):
	x = np.arange(len(x_labels))  # the label locations
	type_num = len(axDictData)
	for type_name,type_values in axDictData.items():
		juli = (type_num -1)/2 * width
		x_values  = x - juli
		# x_values代表bar图【中心点】的坐标
		rects = ax.bar(x_values, type_values, width, label=type_name)
		ax.bar_label(rects, padding=1.5)
		type_num -= 2
	ax.set_xticks(x)
	ax.set_xticklabels(x_labels)
	ax.set_ylabel('人数')
	ax.set_title(f'{ax_name}心愿单')
	ax.legend()


if __name__ == "__main__":
	df = read_csv()
	gb = df.groupby(['城市'])
	row_num,col_num = 3,3
	fig, axes = plt.subplots(nrows=row_num,ncols=col_num,figsize=(20,20),dpi=50,sharex=False)
	x_labels = ['报名量','拉新量'] # 和axDictDat中值列表元素个数一致

	row_count,col_count = 0,0
	for ax_name,df_city in gb:
		axDictData = {} #{'type1':[v1,v2],'type2':[v1,v2]} x_labels元素个数和[v1,v2]一致
		gb_yw = df_city.groupby('业务线')
		for yw_name,yw_df in gb_yw:
			values = yw_df[x_labels].sum().tolist()
			axDictData[yw_name] = values
		# 当前ax位置
		ax = axes[row_count,col_count]
		print(axDictData)
		draw_sub(ax=ax,ax_name=ax_name,axDictData=axDictData,x_labels=x_labels)
		col_count += 1
		if col_count > col_num - 1:
			row_count += 1
			col_count = 0

	fig.savefig('心愿单分城.png')
