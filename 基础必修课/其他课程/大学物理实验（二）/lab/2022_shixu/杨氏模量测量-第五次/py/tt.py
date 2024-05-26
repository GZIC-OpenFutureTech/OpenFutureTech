import scipy.stats as st
import seaborn as sns
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit  # 拟合
from scipy.interpolate import make_interp_spline

# =======================================
# 图片背景设置
plt.style.use('seaborn-darkgrid')
sns.set(style='darkgrid')
import warnings
warnings.filterwarnings('ignore')
plt.rcParams['font.sans-serif'] = ['STSong']

x0 = np.array([-30, -20, -10, 10, 20])
y0 = np.array([769.00, 750.30, 734.63, 731.84, 738.66])
y1 = np.array([769.66,	748.56,	733.56,	731.76,	738.86])
y = np.array([769.45,	748.55,	733.85,	731.85,	738.95])
y = np.array([1049.16,	1057.26,	1062.96,	1064.16,	1061.16])
y = np.array([1050.16,	1056.06,	1062.06,	1063.56,	1059.49])
yx = np.array([1050.76,	1056.76,	1062.46,	1063.56,	1060.66])

# 多项式拟合
degree = 2  # 可以调整多项式的次数
coefficients = np.polyfit(x0, yx, degree)
poly = np.poly1d(coefficients)

# 在给定范围内生成平滑曲线上的点
x_smooth = np.linspace(min(x0), max(x0), 1000)
y_smooth = poly(x_smooth)

# 绘制原始数据点和平滑曲线
plt.scatter(x0, yx, label='Raw data points')
plt.plot(x_smooth, y_smooth, label='Fit curve', color='red')

# 在x=0处添加标注
y_at_x0 = poly(0)
plt.scatter(0, y_at_x0, color='green', marker='o', label=f'x=0, y={y_at_x0:.2f}')
plt.text(0, y_at_x0, f'  {y_at_x0:.2f}', fontsize=10, verticalalignment='bottom')

# 添加标签和标题
plt.xlabel('Distance from the origin/mm')
plt.ylabel('Frequency of Steel/Hz')
plt.title('Measurement of resonant frequency (Steel) - ver3')

# 显示图例
plt.legend()

# 显示图形
plt.show()
