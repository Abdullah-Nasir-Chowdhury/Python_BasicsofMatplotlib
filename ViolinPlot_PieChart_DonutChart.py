import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# initialize list:
data = [1,2,3,4,3,3,3,4,5,7,8,]
data1 = [2,3,4,5,6,7,8,9,2,3]
data2 = [1,2,3,4,5,6,7,4,3]

# Violin-plot:
# data_final = list([data,data1,data2])
# plt.violinplot(data_final,showmedians=True)


# pie-charts:
fruit = ['Apple','Oranges','Mango','Guava']
quantity = [10,20,30,40]
# just plot:
# plt.pie(quantity,labels=fruit)
# plot with percentage:
# plt.pie(quantity,labels=fruit, autopct="%0.1f%%")

# doughnut chart
plt.pie(quantity,labels=fruit, radius=1)
plt.pie([1],colors=['w'],radius=0.5)


plt.show()
