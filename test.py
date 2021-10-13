import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2*np.pi, 2*np.pi, 111)

y_1= np.cos(x/2)*x
y_2=np.cos(x)*x
y_3=np.cos(2*x)*x

plt.plot(x, y_1, color='g', linewidth =1)
plt.plot(x, y_2, color='b', linewidth=1)
plt.plot(x, y_3, color='r', linewidth=1)
plt.legend(('cos(x/2)','cos(x)', 'cos(2x)'))
plt.xlabel('zmienna niezależna')
plt.ylabel('zmienna zależna')
plt.title('Cosinus o różnym okresie')
plt.grid(True)
plt.savefig('test.png', format="png")
plt.show()
