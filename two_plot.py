import matplotlib.pyplot as plt
import numpy as np

x =  np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x,y1,label="Sin x",color="blue",linestyle="-",linewidth=2)
plt.plot(x,y2,label="Cos x",color="red",linestyle="--",linewidth=2)

plt.title("Graph")
plt.xlabel("x-axis")
plt.ylabel("y-axis")

plt.legend()

plt.show()