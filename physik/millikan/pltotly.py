import numpy as np
import plotly.express as px

data = np.genfromtxt("data_new.csv", delimiter=",", names=["x", "y"])
fig = px.scatter(x=data['x'], y=data['y'])
fig.show()
