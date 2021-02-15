import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib as mpl

def plot1(data,target,model):
    # 定义图像和三维格式坐标轴
    fig=plt.figure(figsize=(9,9))
    ax = Axes3D(fig)
    ax.scatter3D(data[:,0],data[:,1],target,color='darkblue')
    x=np.linspace(0,20,100)
    y=np.linspace(-1,1,100)
    xx, yy = np.meshgrid(x, y)
    z=model.coef_[0]*xx+model.coef_[1]*yy+model.intercept_
    surf=ax.plot_surface(xx, yy, z, rstride=1, cstride=1, cmap='rainbow')
    fig.colorbar(surf, ax=ax,fraction=0.08, pad=0.05,shrink=0.5)
    ax.set_xlabel(xlabel='extension rate',fontsize=15)
    ax.set_ylabel(ylabel='moisture tolerance',fontsize=15)
    ax.set_zlabel(zlabel='Decomposition rate',fontsize=15)
    plt.title('regression analysis',fontsize=25)
    plt.tick_params(labelsize=13)
    ax.set_ylim(-1,1)
    ax.set_xlim(0,20)
    plt.show()

def plot2(data,model):
    fig = plt.figure(figsize=(10,10))
    ax1 = fig.add_subplot(211)
    ax2 = fig.add_subplot(212)
    #取耐湿度为0
    x1=np.linspace(0,11,100)
    y1=model.coef_[0]*x1+model.intercept_
    ax1.plot(x1,y1,color='red',linewidth=1,label='22℃')
    ax1.set_xlabel(xlabel='extension rate')
    ax1.set_ylabel(ylabel='Decomposition rate')
    ax1.set(title='when moisture tolerance = 0')
    ax1.set_xlim(0,11)
    ax1.fill_between(x1,y1+0.18,y1-0.19,color='tan')
    ax1.legend(loc='upper left')

    #取延展率为0
    x2=np.linspace(-1,1,100)
    y2=model.coef_[1]*x2+model.intercept_
    ax2.plot(x2,y2,color='red',label='22℃')
    ax2.set_xlabel(xlabel='moisture tolerance')
    ax2.set_ylabel(ylabel='Decomposition rate')
    ax2.set(title='when extension rate = 0')
    ax2.fill_between(x2, y2 + 0.46, y2-0.46, color='tan')
    ax2.set_xlim(-1,1)
    ax2.legend(loc='upper left')
    plt.tick_params(labelsize=13)
    plt.show()


if __name__ == '__main__':
    mpl.rcParams['font.sans-serif'] = ['SimHei']  # 配置显示中文，否则乱码
    mpl.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    dataset = pd.read_csv('./Fungal_trait_data000.csv')
    col = dataset.columns.values.tolist()
    data = np.array(dataset[col[3:5]])
    target = np.array(dataset[col[5]])/122
    model = LinearRegression()
    model.fit(data, target)
    print(model.predict(data[:4, :]))
    print(target[:4])
    print(model.coef_)  # 如果y=0.1x+0.3   则此行输出的结果为0.1
    print(model.intercept_)  # 此行输出的结果为0.3
    print(model.get_params())  # 模型定义时定义的参数，如果没有定义则返回默认值
    print(model.score(data, target))  # 给训练模型打分，注意用在LinearR中使用R^2 conefficient of determination打分
    # plot1(data,target,model)
    plot2(data,model)
