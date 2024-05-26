import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# 读取数据
data = np.array([19.57, 19.48, 19.61, 19.52, 19.42, 19.48, 19.37, 19.43, 19.51])

# 绘制KDE图
fig, ax = plt.subplots()
sns.kdeplot(data, ax=ax)

# 标记异常值
mean = np.mean(data)
std = np.std(data)
threshold = mean + 2 * std
outliers = [x for x in data if x > threshold]
ax.plot(outliers, np.zeros_like(outliers), 'ro', alpha=0.5)

# 显示图形
plt.show()