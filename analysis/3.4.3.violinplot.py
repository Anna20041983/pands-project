# Show the violinplot for each column in the Iris Data Set
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Apply black background
plt.style.use("dark_background")

data = pd.read_csv('Iris-Data-Set.csv')

# Apply different colours per each class
colors = {"yellow", "orange", "red"}

# Show Violilplot for Sepal Width
sns.violinplot(x=data['class'], y=data['sepal_width'], palette=colors)

plt.title('Sepal Width for 3 Iris Classes')
plt.show()