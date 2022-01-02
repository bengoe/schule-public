import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt("data_new.csv", delimiter=",", names=["x", "y"])
plt.scatter(data['x'], data['y'])
plt.xlabel("Versuch")
plt.ylabel("q")
plt.show()