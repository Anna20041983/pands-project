# Import and show the Iris data
import pandas as pd

# CSV file with Iris Data Set
data = pd.read_csv('Iris-Data-Set.csv')
data.columns 

# Print what the table includes
print ('\n The Iris Data Set contains the below information: \n')
print (data.head())

# Show the shape of the data
print ('\n The shape of the Iris Data Set is: \n')
print (data.shape)


