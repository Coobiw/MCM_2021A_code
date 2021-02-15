import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt
def logistic(Lf_max,r0,t):
    Lf_0 = 0.5
    Lf = (Lf_max/(1+(Lf_max/Lf_0)*np.exp(-r0*t)))
    return Lf

def double(inivalue,_):
    Lf_max1 = 30.5
    Lf_max2 = 92.72
    Lf_max3 = 42.7
    r01 = 0.067
    r02 = 0.086
    r03 = 0.072
    w = 1.1
    a1 = 0.25
    d1 = 0.250263344
    a2 = 0.76
    d2 = -0.177229442
    Y = np.zeros(3)
    X = inivalue
    Y[0] = r01*X[0]*(1-X[0]/Lf_max1-w*(a2*X[1]/Lf_max2+a3*X[2]/Lf_max3)+d1*X[0]/Lf_max1)
    Y[1] = r02*X[1]*(1-X[1]/Lf_max2-w*(a1*X[0]/Lf_max1+a3*X[2]/Lf_max3)+d2*X[1]/Lf_max2)
    Y[1] = r03*X[2]*(1-X[2]/Lf_max3-w*(a1*X[0]/Lf_max1+a2*X[1]/Lf_max2)+d3*X[2]/Lf_max3)
    return Y


Lf_0 = 0.5
Lf_max1 = 30.5
Lf_max2 = 92.72
Lf_max3 = 42.7
r01 = 0.067
r02 = 0.086
r03 = 0.072
Lfc1 = Lf_max1/2
Lfc2 = Lf_max2/2
Lfc3 = Lf_max3/2
tc = 61
w=1.1
a1=0.25
d1=0.250263344
a2=0.76
d2=-0.177229442
a3=0.35
d3=0.071675284
INI = (Lfc1,Lfc2,Lfc3) # INI为初始状态下的数组
t1 = np.linspace(0,60.5,1000)
t2 = np.arange(61,400)
RES = spi.odeint(double, INI, t2)
plt.plot(t1,logistic(30.5,0.067,t1),color = '#1f77b4',label='a.gal1.s',linewidth=5)
plt.plot(t2,RES[:,0],color = '#2ca02c',linewidth=5)
plt.plot(t1, logistic(92.72, 0.086, t1), color='#d62728',label='a.gal9.n',linewidth=5)
plt.plot(t2,RES[:,1],color='#ff7f0e',linewidth=5)
plt.plot(t1, logistic(42.7, 0.072, t1), color='pink',label='a.gal10.n',linewidth=5)
plt.plot(t2,RES[:,2],color = 'purple',linewidth=5)
plt.title('3 fungus',fontsize = 25)
plt.legend(loc='best')
plt.xlabel('time(day)',fontsize=15)
plt.ylabel('hypal length(mm)',fontsize=15)
plt.tick_params(labelsize=13)
plt.show()

