import numpy as np
from scipy.optimize import leastsq
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib as mpl

temp = 25.05

def residuals1(m1,x,y):
    return y-0.41501077*np.exp(m1*(x-temp)**2)

def residuals2(m2,x,y):
    return y-0.41501077*np.exp(m2*(x-temp)**2)

def fitting1():
    m1 = np.random.rand(1)
    res1 = leastsq(residuals1,m1,args=(X1,Y1),maxfev=50000)
    print(res1)
    return res1

def fitting2():
    m2 = np.random.rand(1)
    res2 = leastsq(residuals2, m2, args=(X2, Y2),maxfev=50000)
    print(res2)
    return res2

if __name__=='__main__':
    mpl.rcParams['font.sans-serif'] = ['SimHei']  # 配置显示中文，否则乱码
    mpl.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    dataset = pd.read_csv('./temperature.csv')
    print(dataset)
    col = dataset.columns.values.tolist()
    X = np.array(dataset[col[1]])
    Y = np.array(dataset[col[2]])
    X1 = X[0:208]
    X2 = X[208:400]
    Y1 = Y[0:208]
    Y2 = Y[208:400]
    x1 = np.linspace(0, 25.05, 1000)
    x2 = np.linspace(25.05,50.1,1000)
    res1 = fitting1()[0]
    res2 = fitting2()[0]
    plt.figure(figsize=(9,9))
    plt.plot(x1,0.41501077*np.exp(res1*(x1-temp)**2),color='darkblue',label='a.gal1.s')
    plt.plot(x2,0.41501077*np.exp(res2*(x2-temp)**2),color='darkblue')
    plt.title('extension rate---temperature: ')
    plt.xlim(0,51)
    plt.ylim(0,0.5)
    plt.xlabel('temperature')
    plt.ylabel('extension rate')
    plt.legend(loc='best')
    plt.show()