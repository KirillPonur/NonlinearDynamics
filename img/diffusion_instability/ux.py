import numpy as np 
import matplotlib.pyplot as plt

x=np.linspace(-3,3,300)
u=np.sqrt(1-x**2)
u=np.exp(-x**2)

plt.plot(x,u)
# plt.plot(x-x**2+1,u)
# plt.plot(x+1.2*u**2,u)
plt.plot(x+1.2*np.exp(-2*x**2),u)
plt.show()