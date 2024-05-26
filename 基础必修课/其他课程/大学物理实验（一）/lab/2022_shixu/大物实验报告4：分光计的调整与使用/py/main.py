import numpy as np
import matplotlib.pyplot as plt
# 定义数据
#data = [47.2,	47.3,	47.283,	46.867,	47.167,	47.283]
data = np.array([1.61,	1.611,	1.611,	1.61,	1.611])
mean = np.mean(data)
std = np.std(data)
print(mean,std)

