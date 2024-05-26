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

x = np.array([50 , 100 , 150 , 200 , 250 , 300 , 350 , 400])  # 第一列数据
y = np.array([19.825 , 18.764 , 16.720 , 15.115 , 13.531 , 11.952 , 10.307 , 8.685])  # 第二列数据

# 绘制散点图
plt.scatter(x, y, label='Data Points')

# 连线
plt.plot(x, y, label='Connected Line')

# 拟合直线
fit = np.polyfit(x, y, 1)  # 一阶多项式拟合
slope, intercept = fit
print(f"Slope: {slope}, Intercept: {intercept}")
fit_fn = np.poly1d(fit)
plt.plot(x, fit_fn(x), '--r', label='Fitted Line')

# 设置图例和标题
plt.legend()
plt.title('Scatter Plot with Fitted Line')
print(y.var())
# 显示图形
#plt.show()