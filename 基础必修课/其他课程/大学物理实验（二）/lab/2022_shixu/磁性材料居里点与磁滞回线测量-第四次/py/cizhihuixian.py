import numpy as np
import matplotlib.pyplot as plt

# 原始数据
x_data = np.array([1230, 482, 20, -292, -455, -617, -1240, -355, 20, 382, 495, 757])
y_data = np.array([244, 190, 144, 66.5, -500, -111, -250, -198, -153, -78.5, -500, 126])

# 将数据分为上下两部分
x_upper = x_data[x_data >= 0]
y_upper = y_data[x_data >= 0]

x_lower = x_data[x_data < 0]
y_lower = y_data[x_data < 0]

# 多项式拟合
degree = 3  # 选择多项式的次数
coeff_upper = np.polyfit(x_upper, y_upper, degree)
coeff_lower = np.polyfit(x_lower, y_lower, degree)

# 生成拟合曲线上的点
x_upper_fit = np.linspace(min(x_upper), max(x_upper), 100)
y_upper_fit = np.polyval(coeff_upper, x_upper_fit)

x_lower_fit = np.linspace(min(x_lower), max(x_lower), 100)
y_lower_fit = np.polyval(coeff_lower, x_lower_fit)

# 绘制原始数据和拟合曲线
plt.scatter(x_upper, y_upper, label='Upper Data')
plt.scatter(x_lower, y_lower, label='Lower Data')
plt.plot(x_upper_fit, y_upper_fit, label='Upper Fit', color='red')
plt.plot(x_lower_fit, y_lower_fit, label='Lower Fit', color='blue')

plt.legend()
plt.show()


