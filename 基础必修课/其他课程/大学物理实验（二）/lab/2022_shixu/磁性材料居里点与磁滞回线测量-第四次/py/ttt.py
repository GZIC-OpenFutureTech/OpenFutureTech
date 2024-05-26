import scipy.stats as st
import seaborn as sns
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit#拟合
from scipy.interpolate import make_interp_spline
#=======================================
#图片背景设置
plt.style.use('seaborn-darkgrid')
sns.set(style = 'darkgrid')
import  warnings
warnings.filterwarnings('ignore')
plt.rcParams['font.sans-serif'] = ['STSong']
x0 = np.array([20, 345, 445, 595, 757, 895, 1070, 1230])
y0 = np.array([0.5, 44.5, 92, 127, 167, 194, 217, 244])

# 多项式拟合
degree = 3  # 可以调整多项式的次数
coefficients = np.polyfit(x0, y0, degree)
poly = np.poly1d(coefficients)

# 在给定范围内生成平滑曲线上的点
x_smooth = np.linspace(min(x0), max(x0), 1000)
y_smooth = poly(x_smooth)

# 绘制原始数据点和平滑曲线
plt.scatter(x0, y0, label='Raw data points')
plt.plot(x_smooth, y_smooth, label='fit curve', color='red')

# 添加标签和标题
plt.xlabel('Ux/mV')
plt.ylabel('Uy/mV')
plt.title('the basic magnetic field of ferrite')

# 显示图例
plt.legend()

# 显示图形
plt.show()