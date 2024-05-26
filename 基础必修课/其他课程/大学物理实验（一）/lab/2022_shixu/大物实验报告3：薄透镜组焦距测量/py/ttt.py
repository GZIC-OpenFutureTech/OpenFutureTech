import numpy as np
import matplotlib.pyplot as plt

# 读取数据
#data = np.array([19.57, 19.48, 19.61, 19.52, 19.42, 19.48, 19.37, 19.43, 19.51])
data = np.array([25.75, 25.91, 25.83, 25.74, 25.77, 25.53, 25.72, 25.58, 25.59])

# 计算平均值和标准差
mean = np.mean(data)
std = np.std(data)

# 计算异常值阈值
threshold = mean +  std
down = mean -  std
# 绘制散点图
fig, ax = plt.subplots()
ax.scatter(range(len(data)), data)

# 标记异常值
outliers = [x for x in data if x > threshold or x<down]
ax.plot([i for i in range(len(data)) if data[i] in outliers], outliers, 'ro', alpha=0.5)

# 添加阴影
x = np.linspace(0, len(data)-1, 100)
y1 = mean - std
y2 = mean + std
ax.fill_between(x, y1, y2, alpha=0.2, color='green')

# 设置图形属性
ax.set_title('Standard Deviation Analysis')
ax.set_xlabel('Index')
ax.set_ylabel('Values')

# 显示图形
plt.show()
