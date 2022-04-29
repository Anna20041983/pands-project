# Show the boxplot of Irish Data Set
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
   
data = pd.read_csv('Iris-Data-Set.csv')

# Show boxplot for all 4 columns
data.boxplot()

plt.title('Boxplot of each variable in the Iris Data Set')
plt.show()

# Resource: https://matplotlib.org/stable/plot_types/index
# Resource: http://seaborn.pydata.org/introduction.html#visualizing-dataset-structure