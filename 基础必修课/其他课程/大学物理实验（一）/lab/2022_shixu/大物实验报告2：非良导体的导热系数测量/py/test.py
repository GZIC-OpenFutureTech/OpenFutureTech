import seaborn as sns
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
#=======================================
#Image background settings
plt.style.use('seaborn-darkgrid')
sns.set(style = 'darkgrid')
import  warnings
warnings.filterwarnings('ignore')
plt.rcParams['font.sans-serif'] = ['STSong']
#=======================================
#Calculating tangents
def numerical_diff(f, x):
    h = 1e-7
    return (f(x + h) - f(x - h)) / (2 * h)
#Constructed tangents
def tangent_line(f, x):
    d = numerical_diff(f, x)
    y = f(x) - d * x
    print(y,d)
    return lambda t: d * t + y
#Read data
file1 = pd.read_excel('./data/data2.xlsx')
#=========================================
x = file1['a']
y = file1['b']
z1 = np.polyfit(x, y, 3)
p1 = np.poly1d(z1)
yvals1 = p1(x)
p2 = tangent_line(p1,183.6)
yvals2 = p2(x)
plt.plot(x, y, '*',label='original values')
plt.plot(x, yvals1,'r--',label='poly_fit values')
plt.plot(x, yvals2,'r-',label='Cut Line')
plt.legend(loc="upper right")
plt.title('Temperature versus time curve')
plt.xlabel('Time interval (/second)')
plt.ylabel('Temperature')
plt.show()
plt.savefig('fig12.png')
