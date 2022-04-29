# Apply different statistic techniques to analyse the Iris Data Set
import pandas as pd

data = pd.read_csv('Iris-Data-Set.csv')
data.columns

summary=data.describe

print('\n Summary of Iris Data Set is: \n')
print (summary())

print('\n Median of Iris Data Set is: \n')
print (data.median(numeric_only=True))

print('\n Mean of Iris Data Set is: \n')
print (data.mean(numeric_only=True))

print ('\n Correlation of Iris Data Set is: \n')
print (data.corr())

print ('\n Covariance of Iris Data Set is: \n')
print (data.cov())

print('\n Summary of Iris Data class is: \n')
print (data.groupby('class').describe())

print('\n Median of Iris Data class is: \n')
print (data.groupby('class').median())

print('\n Mean of Iris Data class is: \n')
print (data.groupby('class').mean())

print('\n Correlation of Iris Data class is: \n')
print (data.groupby('class').corr())

print('\n Covariance of Iris Data class is: \n')
print (data.groupby('class').cov())

# Resource: https://docs.python.org/3/library/statistics.html
# Resource: https://stackoverflow.com/questions/70897794/finding-the-mean-of-nuisance-columns-in-dataframe-error
