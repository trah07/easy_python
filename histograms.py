import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('student.csv')

# Plot the histogram for G1 and G2 and G3 columns 
data['G1'].plot(kind='hist', bins=10, color='blue', edgecolor='black', linewidth=1.2)
plt.title('Histogram of G1')
plt.xlabel('Grade')
plt.ylabel('Frequency')
plt.show()

data['G2'].plot(kind='hist', bins=10, color='blue', edgecolor='black', linewidth=1.2)
plt.title('Histogram of G2')
plt.xlabel('Grade')
plt.ylabel('Frequency')
plt.show()

data['G3'].plot(kind='hist', bins=10, color='blue', edgecolor='black', linewidth=1.2)
plt.title('Histogram of G3')
plt.xlabel('Grade')
plt.ylabel('Frequency')
plt.show()