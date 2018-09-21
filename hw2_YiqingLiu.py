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
	def plot_two_columns(self,data,x_column,y_column,title):
		fig = plt.figure()
		x = data[x_column]
		y = data[y_column]
		plt.bar(x,y,width=0.8)
		plt.xticks(fontsize=8)
		fig.autofmt_xdate()
		plt.title(title, bbox={'facecolor':'0.8', 'pad':5})
		plt.xlabel(x_column)
		plt.ylabel(y_column)
		fig.set_size_inches(10, 6)
		plt.savefig('/Users/yiqingliu/Google Drive/IS590DV/hw2/'+str(self.index)+'.png')
		self.index=self.index+1
	def contional_plot_two_columns(self,x_column,y_column,title,start_date,end_date):
		data=self.data[self.data[x_column]>=start_date]
		data=data[data[x_column]<=end_date]
		self.plot_two_columns(data,x_column,y_column,title)
	def simple_plot_two_columns(self,x_column,y_column,title):
		data=self.data
		self.plot_two_columns(data,x_column,y_column,title)

def main():
	d=Dataset("gun-violence.csv")
	d.contional_plot_two_columns('date','n_injured','how many people get injured','2013-01-01','2013-02-01')
	d.contional_plot_two_columns('date','n_killed','how many people get killed','2013-01-01','2013-02-01')
	d.simple_plot_two_columns('state','n_injured','how many people get injured')
	d.simple_plot_two_columns('state','n_killed','how many people get killed')
if __name__=='__main__':
	main()