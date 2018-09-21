# homework2
# Filtering, Smoothing/Binning, and Multiplots
# author @ Yiqing Liu

# Question 1: How many people have been killed on each day between Jan 1st, 2013 - Feb 1st, 2013
# Question 2: How many people have been injured on each day between Jan 1st, 2013 - Feb 1st, 2013
# Question 3: How many people have been killed in each state?
# Question 4: How many people have been injured in each state?

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Dataset:
	def __init__(self,filepath):
		self.data=pd.read_csv(filepath)
		self.index=1

	def plot_two_columns(self,plt,data,x_column,y_column,title):
		x = data[x_column]
		y = data[y_column]
		plt.bar(x,y,width=0.8)
		plt.xticks(fontsize=8)
		plt.title(title,fontsize=30, bbox={'facecolor':'0.8', 'pad':8})
		plt.xlabel(x_column)
		plt.ylabel(y_column)

	def contional_plot_two_columns(self,plt,x_column,y_column,title,start_date,end_date):
		data=self.data[self.data[x_column]>=start_date]
		data=data[data[x_column]<=end_date]
		self.plot_two_columns(plt,data,x_column,y_column,title)

	def simple_plot_two_columns(self,plt,x_column,y_column,title):
		data=self.data
		self.plot_two_columns(plt,data,x_column,y_column,title)

def main():

	d=Dataset("gun-violence.csv")
	fig = plt.figure(22)
	fig.suptitle('Multiplots',fontsize=60)
	fig.tight_layout()
	plt.subplots_adjust(wspace =0.2, hspace =0.2)
	plt.subplot(221)
	d.contional_plot_two_columns(plt,'date','n_injured','how many people get injured','2013-01-01','2013-02-01')
	plt.subplot(222)
	d.contional_plot_two_columns(plt,'date','n_killed','how many people get killed','2013-01-01','2013-02-01')
	plt.subplot(223)
	d.simple_plot_two_columns(plt,'state','n_injured','how many people get injured')
	plt.subplot(224)
	d.simple_plot_two_columns(plt,'state','n_killed','how many people get killed')
	fig.set_size_inches(30,25)
	plt.savefig('/Users/yiqingliu/Google Drive/IS590DV/hw2/hw2_YiqingLiu.png')

if __name__=='__main__':
	main()