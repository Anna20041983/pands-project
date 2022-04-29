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
plt.scatter(data1['petal_length'],data1['petal_width'],color='yellow',label='Iris Setosa')
plt.scatter(data2['petal_length'],data2['petal_width'],color='orange',label='Iris Versicolor')
plt.scatter(data3['petal_length'],data3['petal_width'],color='red',label='Iris Virginica')

# Print scatter for Petal Length and Width
plt.xlabel('petal_length')
plt.ylabel('petal_width')
plt.title ('Petal length & Petal width scatter')
plt.legend()
plt.show()