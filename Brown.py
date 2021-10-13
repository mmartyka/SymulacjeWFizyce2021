import matplotlib.pyplot as plt
import numpy as np


def one_dim(n,T):
        dx = np.random.randn(n,T)
        x = np.cumsum(dx, axis=1)
        time = np.linspace(0, T, T)
        cmap=plt.get_cmap("Set1")
        opis =[]

        for i in range(10):
            plt.plot(time, x[i,:], color=cmap(i), alpha=0.5)
            opis.append("Cząstka "+str(i))
        plt.legend(opis, loc=4, fontsize="xx-small")
        plt.xlabel('Time')
        plt.ylabel('Position')
        plt.title('1-d random walk')
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

one_dim(10,1000)
two_dim(1000)
