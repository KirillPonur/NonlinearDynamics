import numpy as np
from scipy.integrate import odeint,solve_ivp
import scipy
from numpy import sqrt, exp
import matplotlib.pyplot as plt

def model(t,z):
	# print(z)
	y1=z[0]
	y2=z[1]
	return [y2,1*y1-y1**2/2-0.05*y2]

# initial condition
z0 = np.array([0,0.00000001])

solve = solve_ivp(model,[0,150],z0,method='LSODA',min_step=0.001,max_step=0.01)

Time=np.flip(solve.t)
Time=solve.t
z=solve.y
# print(z)

Y1=z[0]
Y2=z[1]

plt.subplot(221)
plt.plot(Time,Y1)
# for x in range(0,len(Time)):
# 	print(Time[x],'\t', Y1[x])
# print(Time)
# print(Y1)
# plt.show()
plt.subplot(222)
plt.plot(Time,Y2)
# plt.show()
plt.subplot(223)
plt.plot(Y1,Y2)
plt.show()