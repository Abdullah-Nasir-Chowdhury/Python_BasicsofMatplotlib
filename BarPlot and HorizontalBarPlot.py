import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# initialize dictionary key and values:
student = {"Bob" : 87,
           "Matt" : 56,
           "Sam" : 27}
# initialize list for keys and values:
names = list(student.keys())
values = list(student.values())
# plot bar graph of keys and values:
plt.bar(names,values)
# add beauty:
plt.title("Bar Plot")
plt.xlabel("Names")
plt.ylabel("Marks")
plt.grid("True")

# plot horizontal bar plot:
# plt.barh(names,values)
# plt.title("Horizontal Bar Plot")
# plt.xlabel("Names")
# plt.ylabel("Marks")
# plt.grid("True")


plt.show()