# Split the boxplot for each column in the Iris Data Set
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Apply black background
plt.style.use("dark_background")

data = pd.read_csv('Iris-Data-Set.csv')

# Apply different colours per each class
colors = {"yellow", "orange", "red"}

# Show boxplot for Petal Width
sns.boxplot(x=data['class'], y=data['petal_width'], palette=colors)

plt.title('Petal Width for 3 Iris Classes')
plt.show()