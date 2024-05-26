import scipy.stats as st
import seaborn as sns
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit#拟合
#=======================================
#图片背景设置
plt.style.use('seaborn-darkgrid')
sns.set(style = 'darkgrid')
import  warnings
warnings.filterwarnings('ignore')
plt.rcParams['font.sans-serif'] = ['STSong']
#=========================================
#读入文件
file1 = pd.read_excel('./data2.xlsx')

#=========================================

x0 = file1['a']
y0 = file1['b']

#拟合多项式
coefficients= np.polyfit(x0, y0, 1)#拟合一次函数得到的系数
p1=np.poly1d(coefficients)#合成的一次多项式
y1=p1(x0)#拟合的y值

#拟合任意一元函数的方法
fun = lambda x, a0, a1: a1*x + a0 #自定义函数，可以是指数函数等别的类型函数
a,pcov=curve_fit(fun, x0, y0)#a是最小二乘法得到的系数，pcov是参数的估计协方差
y1=fun(x0,a[0],a[1])

#作图
plt.figure()
plt.plot(x0, y0, '*', label='original values')
plt.plot(x0, y1, 'r--', label='poly_fit values')
plt.xlabel('Square of the cosine of the angle difference')
plt.ylabel('Light intensity(10^(-7)A)')
plt.legend(loc="lower right")
plt.title('Verification of Marius\' Law')#格式化输出
plt.show()
#plt.savefig('fig12.png')
print(a)
print(pcov)
# >>> p1(1997)
# 233.42857142858702
# >>> p1(1998)
# 253.92857142858702
#
# >>> fun(1997,a0,a1)
# 233.42857142858702
# >>> fun(1998,a0,a1)
# 253.92857142858702