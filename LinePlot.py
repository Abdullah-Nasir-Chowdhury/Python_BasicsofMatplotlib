import numpy as np
from matplotlib import pyplot as plt

# initialize arrays:
x = np.arange(1,11)
print(f"x = {x}")
y = 2*x
print(f"y = {y}")
y1 = 3*x
print(f"y1 = {y1}")

# draw the plot:

plt.plot(x,y, color="red", linestyle=":", linewidth=2)
plt.plot(x,y1, color="blue", linestyle="-.")
plt.plot(y,y1, color="green")
plt.title("Line Plot")
plt.xlabel("x-label")
plt.ylabel("y-label")

plt.grid(True)

plt.show()

# use subplots:
plt.subplot(1,3,1)
plt.xlabel("x-label")
plt.ylabel("y-label")
plt.plot(x,y,color="red",linestyle="-.",linewidth=2)
plt.grid(True)

plt.subplot(1,3,2)
plt.xlabel("x-label")
plt.ylabel("y-label")
plt.plot(x,y1,color="blue",linestyle=":",linewidth=1)
plt.grid(True)

plt.subplot(1,3,3)
plt.xlabel("x-label")
plt.ylabel("y-label")
plt.plot(y,y1,color="green")
plt.grid(True)

plt.show()