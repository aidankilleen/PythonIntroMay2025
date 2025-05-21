# matplotlib_investigation.py

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6]
y = [66, 44, 35, 67, 99, 14]

plt.plot(x, y)
plt.xlabel("X Axis")
plt.ylabel("Sales")
plt.title("First Plot")

plt.savefig("firstplot.png")

plt.show()



