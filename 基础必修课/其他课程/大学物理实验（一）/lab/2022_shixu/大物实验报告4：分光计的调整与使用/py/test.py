import numpy as np
import matplotlib.pyplot as plt

# 读取数据
data = np.array([1.61,	1.611,	1.611,	1.61,	1.611])
#data = np.array([47.2,	47.3,	47.283,	46.867,	47.167,	47.283])

# 绘制箱线图
fig, ax = plt.subplots()
ax.boxplot(data)

# 标记异常值
q1 = np.percentile(data, 25)
q3 = np.percentile(data, 75)
iqr = q3 - q1
upper_bound = q3 + 1.5 * iqr
lower_bound = q1 - 1.5 * iqr
outliers = [x for x in data if x < lower_bound or x > upper_bound]
ax.plot(np.ones(len(outliers)), outliers, 'ro', alpha=0.5)

# 显示图形
plt.show()
