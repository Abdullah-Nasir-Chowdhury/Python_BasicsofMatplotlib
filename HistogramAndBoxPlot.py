import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# initialize list:
data = [1,2,3,4,3,3,3,4,5,7,8,]
data1 = [2,3,4,5,6,7,8,9,2,3]
data2 = [1,2,3,4,5,6,7,4,3]
# plot histogram:
# plt.hist(data)

# control bins in histogram:
# plt.hist(data,color="red",bins=1)

# read csv and show histogram:
# iris = pd.read_csv("vgsales.csv")
# iris.head()
# print(iris)
#
# plt.hist(iris['Global_Sales'],bins=100,color='g')


# Box-plot:
data_final = list([data,data1,data2])
plt.boxplot(data_final)


plt.show()
