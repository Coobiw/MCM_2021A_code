import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
def logistic(Lf_max,r0,t):
    Lf_0 = 0.5
    Lf = (Lf_max/(1+(Lf_max/Lf_0)*np.exp(-r0*t)))
    return Lf
def logistic_diff(Lf_max,r0,t):
    Lf_0=0.5
    Lf_diif = r0*logistic(Lf_max,r0,t)*(1-(logistic(Lf_max,r0,t)/Lf_max))
    return Lf_diif
def fun(Lf_max,r0,Tm,t):
    Rde0 = 0.027858622786354044
    k1 = 0.0139021
    k2 = 0.00087979
    Lf_0 = 0.5
    x1 = (Rde0+k2*Tm)*t
    x2 = k1*logistic(Lf_max,r0,t)-k1*Lf_0
    return -x1-x2

if __name__ =='__main__':
    mpl.rcParams['font.sans-serif'] = ['SimHei']
    mpl.rcParams['axes.unicode_minus'] = False
    plt.figure(figsize=(9,6))
    t_test=np.linspace(0.,300,1000)
    # plt.plot(t_test,100+fun(30.5,0.067,0.250263344,t_test),color = '#1f77b4',label='a.gal1.s',linewidth=5)
    # plt.plot(t_test,100+fun(42.7, 0.072, 0.071675284, t_test), color='#ff7f0e', label='a.gal10.n', linewidth=5)
    # plt.plot(t_test,100+ fun(59.78, 0.078, 0.785145889, t_test), color='#2ca02c', label='a.gal6.n', linewidth=5)
    # plt.plot(t_test,100+ fun(92.72, 0.086, -0.177229442, t_test), color='#d62728', label='a.gal9.n', linewidth=5)
    f1=fun(30.5,0.067,0.250263344,t_test)
    f2=fun(42.7, 0.072, 0.071675284, t_test)
    f3=fun(59.78, 0.078, 0.785145889, t_test)
    f4=fun(92.72, 0.086, -0.177229442, t_test)
    y=100+f1+f2+f3+f4
    plt.plot(t_test,y,color='lightblue',linewidth=5,label='mentioned 4 fungus')
    plt.title('four fungus decomposition',fontsize=25)
    plt.xlim(0,300)
    # plt.ylim(-0.09,0.02)
    plt.xlabel('time(day)',fontsize = 15)
    plt.ylabel('4 fungus total instantaneous decomposition (%)',fontsize = 15)
    plt.tick_params(labelsize = 13)
    plt.legend(loc='best')
    plt.show()