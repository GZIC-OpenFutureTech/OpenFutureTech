import numpy as np
import matplotlib.pyplot as plt

# 读取数据
#data = np.array([19.57, 19.48, 19.61, 19.52, 19.42, 19.48, 19.37, 19.43, 19.51])
data = np.array([25.75, 25.91, 25.83, 25.74, 25.77, 25.53, 25.72, 25.58, 25.59])

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
