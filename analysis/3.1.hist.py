# Show histogram of the Iris Data Set
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Apply gray background
plt.style.use("grayscale")

data = pd.read_csv('Iris-Data-Set.csv')

# Show histogram for all 4 columns
data [['sepal_length', 'sepal_width', 'petal_length', 'petal_width']].hist()

plt.show()

# Resource: https://regenerativetoday.com/exploratory-data-analysis-visualization-prediction-model-in-python/