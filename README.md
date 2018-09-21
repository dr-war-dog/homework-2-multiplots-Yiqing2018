![](https://ws1.sinaimg.cn/large/006tNbRwly1fvh59oez3dj304t04uaap.jpg)
# Homework 2 Multiplots

|Author|Yiqing Liu|
|---|---
|E-mail|yiqing5@:corn:.edu

### :star: Answer
![](https://ws1.sinaimg.cn/large/006tNbRwly1fvhkl94129j31kw0sgqb3.jpg)



### :star: Question1
How many people have been injured on each day between Jan 1st, 2013 - Feb 1st, 2013?

![](https://ws1.sinaimg.cn/large/006tNbRwly1fvh0wa8bmij30rs0goaa9.jpg)

****
### :star: Question2
How many people have been killed on each day between Jan 1st, 2013 - Feb 1st, 2013?

![](https://ws2.sinaimg.cn/large/006tNbRwly1fvh0wt833wj30rs0gomxc.jpg)
****
### :star: Question3
How many people have been injured in each state?

![](https://ws4.sinaimg.cn/large/006tNbRwly1fvh0wwrcglj30rs0godgh.jpg)
****
### :star: Question4
How many people have been killed in each state?

![](https://ws4.sinaimg.cn/large/006tNbRwly1fvh0x0fv3bj30rs0goq3k.jpg)
****

### :white_check_mark: Problem Solved
![](https://ws2.sinaimg.cn/large/006tNbRwly1fvh4f12a75j31kw0y5mzc.jpg)
The font size of x-axis sticks is small, but considering the size of figure, we have to set it to small. I tried using <pre><code>fig.autofmt_xdate()</code></pre>  However, it only works for last two pictures.  

In fact, we could set attributes of sticks to make the rotation! it works for all pictures <pre><code>plt.xticks(fontsize=20,rotation=30)</code></pre>


