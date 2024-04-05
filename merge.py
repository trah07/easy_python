import pandas as pd

# Load the data
data1 = pd.read_csv('student-mat.csv')
data2 = pd.read_csv('student-por.csv')

# Merge the data
data = pd.concat([data1, data2])

# Save the data
data.to_csv('student.csv', index=False)