import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.cm as cm

mpl.rcParams['font.sans-serif'] = ['SimHei'] #配置显示中文，否则乱码
mpl.rcParams['axes.unicode_minus']=False #用来正常显示负号

def f1(x,y,A):#x<25.05,y<-0.89
    rx = -0.0053433*((x-25.05)**2)
    ry = -0.10476123*((y+0.89)**2)
    rz = rx+ry
    return A*np.exp(rz)

def f2(x,y,A):#x<25.05,y>-0.89
    rx = -0.0053433*((x-25.05)**2)
    ry = -3.8461195*((y+0.89)**2)
    rz = rx+ry
    return A*np.exp(rz)

def f3(x,y,A):#x>25.05,y<-0.89
    rx = -0.00969972*((x-25.05)**2)
    ry = -0.10476123*((y+0.89)**2)
    rz = rx+ry
    return A*np.exp(rz)

def f4(x,y,A):#x>25.05,y>-0.89
    rx = -0.00969972*((x-25.05)**2)
    ry = -3.8461195*((y+0.89)**2)
    rz = rx+ry
    return A*np.exp(rz)

if __name__ =='__main__':
    A = 0.41501077
    x1 = np.linspace(0, 25.05, 1000)
    x2 = np.linspace(25.05, 50, 1000)
    y1 = np.linspace(-5, -0.89, 1000)
    y2 = np.linspace(-0.89, 0, 1000)
    xx1 ,yy1 = np.meshgrid(x1,y1)#x<25.05,y<-0.89
    xx2, yy2 = np.meshgrid(x1, y2)  # x<25.05,y>-0.89
    xx3, yy3 = np.meshgrid(x2, y1)  # x>25.05,y<-0.89
    xx4, yy4 = np.meshgrid(x2, y2)  # x>25.05,y>-0.89
    z1 = f1(xx1, yy1, A)
    z2 = f2(xx2, yy2, A)
    z3 = f3(xx3, yy3, A)
    z4 = f4(xx4, yy4, A)
    fig = plt.figure(figsize=(9, 6))
    im1 = plt.imshow(z1,extent=[0,25.05,-5,-0.89],cmap='rainbow',interpolation='bicubic', origin="lower")
    im2 = plt.imshow(z2,extent=[0,25.05,-0.89,0],cmap='rainbow',interpolation='bicubic', origin="lower")
    im3 = plt.imshow(z3,extent=[25.05,50,-5,-0.89],cmap='rainbow',interpolation='bicubic',origin="lower")
    im4 = plt.imshow(z4,extent=[25.05,50,-0.89,0],cmap='rainbow',interpolation='bicubic',origin="lower")
    plt.colorbar(im1,fraction=0.08, pad=0.15, shrink=0.9)  # 添加颜色条标注
    plt.xlabel('temperature(℃)', fontsize=20)
    plt.ylabel('moisture(MPa)', fontsize=20)
    plt.title('extension rate-(temperature and moisture)', fontsize=24)
    plt.tick_params(labelsize=13)
    plt.xlim(0,50)
    plt.ylim(-5,-0.89)
    plt.axis('tight')
    plt.show()