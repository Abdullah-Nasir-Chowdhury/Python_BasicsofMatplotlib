import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# initialize lists:
x = [1,2,3,4,5,6,7,8,9]
y = [9,2,4,5,6,7,1,5,7]
z = [1,2,3,4,5,8,3,2,1]

# plot scatter plot:
# plt.scatter(x,y)

# plot two scatter plots in same plot:
# plt.scatter(x,y,marker="*",c="g",s=100)
# plt.scatter(x,z,marker=".",c="y",s=100)

# plot two scatter plots in sub plot:
plt.subplot(1,2,1)
plt.scatter(x,y,marker="*",c="b",s=100)
plt.subplot(1,2,2)
plt.scatter(x,y,marker=".",c="g",s=100)

plt.show()