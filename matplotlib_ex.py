import matplotlib.pyplot as plt
import numpy as np

x = np.arange(10)
# y = np.arange(10)
y = np.sin(x)

plt.plot(x,y)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("SINE")

plt.show()