# Show scatter of the Iris Data Set
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Apply black background
plt.style.use("dark_background")

data = pd.read_csv('Iris-Data-Set.csv')

# Group Data by each class
data1=data[data['class']=='Iris-setosa']
data2=data[data['class']=='Iris-versicolor']
data3=data[data['class']=='Iris-virginica']

# Apply colour and label per each class
plt.scatter(data1['sepal_length'],data1['sepal_width'],color='yellow',label='Iris Setosa')
plt.scatter(data2['sepal_length'],data2['sepal_width'],color='orange',label='Iris Versicolor')
plt.scatter(data3['sepal_length'],data3['sepal_width'],color='red',label='Iris Virginica')

# Print scatter for Sepal Lenght and Width
plt.xlabel('sepal_lenght')
plt.ylabel('sepal_width')
plt.title ('Sepal lenght & Sepal width scatter')
plt.legend()
plt.show()

# Resource: https://realpython.com/visualizing-python-plt-scatter/
# Resource: https://www.machinelearningplus.com/plots/python-scatter-plot/