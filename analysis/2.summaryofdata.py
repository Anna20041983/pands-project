# Show summary of the Iris Data Set
import pandas as pd

data = pd.read_csv('Iris-Data-Set.csv')
data.columns

# Summaries the Iris Data
print ('\n The summary of the Data Iris Set is: \n')
print (data.describe())

# Count the Iris Data by class
print ('\n Variety of the Iris Data Set is: \n')
print (data.groupby('class').size())

# Resource: https://towardsdatascience.com/solving-a-simple-classification-problem-with-python-fruits-lovers-edition-d20ab6b071d2; 
# Resource: https://stackabuse.com/classification-in-python-with-scikit-learn-and-pandas/

