import matplotlib.pyplot as plt
import numpy as np
import math
import time
def one_dim(n,T):
        dx = np.random.randn(n,T)
        x = np.cumsum(dx, axis=1)
        time = np.linspace(0, T, T)
        cmap=plt.get_cmap("Set1")
        opis =[]
        plt.figure(1)
        for i in range(10):
            plt.plot(time, x[i,:], color=cmap(i), alpha=0.5)
            opis.append("Cząstka "+str(i))
        plt.legend(opis, loc=4, fontsize="xx-small")
        plt.xlabel('Time')
        plt.ylabel('Position')
        plt.title('1-d random walk')
        plt.figure(2)
        mean_err= 1/n*(np.sum(np.square(x), axis=0))
        plt.plot(time, mean_err)
        plt.plot(time, time)
        plt.show()

def two_dim(T):
    dx = np.random.randn(T)
    x = np.cumsum(dx, axis=0)
    dy = np.random.randn(T)
    y = np.cumsum(dy, axis=0)
    plt.plot(x,y)
    plt.xlabel("x coordinate")
    plt.ylabel("y coordinate")
    plt.title("2-d random walk trajectory")
    plt.show()

def gauss(T,D,x):
    return ((1/np.sqrt(4*math.pi*T*D))*np.exp(-(x**2)/(4*D*T)))

def diffuse(T,D,dt,n):
    dx = math.sqrt(2*D*dt)*np.random.randn(n,T)
    x = np.sum(dx, axis=1)
    plt.figure(1)
    plt.xlim(-40,40)
    plt.ylim(0, 0.1)
    plt.hist(x,bins=50, density=True, facecolor='g', alpha=0.5)
    gauss_x=np.linspace(np.amin(x),np.amax(x), 100)
    gauss_y=gauss(T,D,gauss_x)
    plt.plot(gauss_x,gauss_y)
    return plt

#Driver functions, write your own or uncomment below
#one_dim(100,100)
#two_dim(10000000)
#for i in range(5):
#    a=diffuse(30*(i+1),1,1,10000)
#    plt.show()
