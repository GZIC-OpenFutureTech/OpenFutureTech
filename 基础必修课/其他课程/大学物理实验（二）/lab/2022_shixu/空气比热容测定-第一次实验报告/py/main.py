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

x = np.array([40,50,60,70,80,90,100,110])  # 第一列数据
y = np.array([0.511,0.490,0.470,0.459,0.434,0.404,0.382,0.357])  # 第二列数据

# 绘制散点图
plt.scatter(x, y, label='Data Points')

# 连线
plt.plot(x, y, label='Connected Line')

# 拟合直线
fit = np.polyfit(x, y, 1)  # 一阶多项式拟合
fit_fn = np.poly1d(fit)
plt.plot(x, fit_fn(x), '--r', label='Fitted Line')

# 设置图例和标题
plt.legend()
plt.title('Scatter Plot with Fitted Line')

# 显示图形
plt.show()

#输出拟合参数
print(fit_fn)       
