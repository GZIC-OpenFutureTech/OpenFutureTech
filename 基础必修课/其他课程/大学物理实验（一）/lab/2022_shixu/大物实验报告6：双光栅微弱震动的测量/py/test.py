import scipy.stats as st
import seaborn as sns
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from scipy import interpolate
from scipy.optimize import curve_fit#拟合
from scipy.interpolate import UnivariateSpline
#=======================================
#图片背景设置
plt.style.use('seaborn-darkgrid')
sns.set(style = 'darkgrid')
import  warnings
warnings.filterwarnings('ignore')
plt.rcParams['font.sans-serif'] = ['STSong']
# 读取数据
x = [10,
20,
30,
40,
50,
60,
70,
80,
90,
100
]  # 存储 x 值
y = [0.0254203,
0.04575654,
0.05592466,
0.09659714,
0.11184932,
0.13726962,
0.14743774,
0.1525218,
0.1525218,
0.15760586
]  # 存储 y 值
spline = UnivariateSpline(x, y, s=0.5)  # 调整平滑程度，s的值越小，曲线越平滑

# 生成插值曲线数据
x_new = np.linspace(min(x), max(x), 1000)
y_new = spline(x_new)
# 绘制插值曲线和原始数据
plt.plot(x_new, y_new, label='Interpolated curve')
plt.plot(x, y, '*', label='Original data')
plt.xlabel('Power')
plt.ylabel('Amplitude')
plt.title('Power versus amplitude')
plt.legend()
plt.grid(True)
plt.show()