import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus']=False
def logistic(Lf_max,r0,t):
    Lf_0 = 0.5
    Lf = (Lf_max/(1+(Lf_max/Lf_0)*np.exp(-r0*t)))
    return Lf

def logistic_diff(Lf_max,r0,t):
    Lf_0=0.5
    Lf_diif = r0*logistic(Lf_max,r0,t)*(1-(logistic(Lf_max,r0,t)/Lf_max))
    return Lf_diif

if __name__ == '__main__':
    t_test = np.linspace(0,150,10000)
    plt.figure(figsize=(9,6))
    plt.plot(t_test,logistic_diff(30.5,0.067,t_test),color = '#1f77b4',label='a.gal1.s',linewidth=5)
    plt.plot(t_test, logistic_diff(42.7, 0.072, t_test), color='#ff7f0e',label='a.gal10.n',linewidth=5)
    plt.plot(t_test, logistic_diff(59.78, 0.078, t_test), color='#2ca02c',label='a.gal6.n',linewidth=5)
    plt.plot(t_test, logistic_diff(92.72, 0.086, t_test), color='#d62728',label='a.gal9.n',linewidth=5)
    # plt.fill_between(t_test,logistic(t_test)+50 , logistic(t_test)-50, color='gray')
    plt.xlim(0,150)
    plt.ylim(0,2.5)
    plt.xlabel('time/day',fontsize=15)
    plt.ylabel('extension rate(mm/day)',fontsize=15)
    plt.title('early growth',fontsize=25)
    plt.legend(loc='best')
    plt.tick_params(labelsize=13)
    plt.show()

