import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from scipy.optimize import least_squares
file1 = pd.read_excel('./data/data2.xlsx')

x = file1['a']
y = file1['b']
params = np.array([1,1])
def funcinv(x, a, b):
    return b + a/x

def residuals(params, x, data):
    a, b = params
    func_eval = funcinv(x, a, b)
    return (data - func_eval)
res = least_squares(residuals, params, args=(x, y))
a=res.x[0]
b=res.x[1]
print(a,b)
yvals1  = b + a/x
plt.plot(x, y, '*',label='original values')
plt.plot(x, yvals1,'r--',label='poly_fit values')
plt.show()