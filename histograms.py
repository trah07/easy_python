import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('student.csv')

# Plot the histogram for G1 and G2 and G3 columns 
# data['G1'].plot(kind='hist', bins=10, color='blue', edgecolor='black', linewidth=1.2)
# plt.title('Histogram of G1')
# plt.xlabel('Grade')
# plt.ylabel('Frequency')
# plt.show()

# data['G2'].plot(kind='hist', bins=10, color='blue', edgecolor='black', linewidth=1.2)
# plt.title('Histogram of G2')
# plt.xlabel('Grade')
# plt.ylabel('Frequency')
# plt.show()

# data['G3'].plot(kind='hist', bins=10, color='blue', edgecolor='black', linewidth=1.2)
# plt.title('Histogram of G3')
# plt.xlabel('Grade')
# plt.ylabel('Frequency')
# plt.show()


data['Mjob'].value_counts().plot(kind='bar', color='blue', edgecolor='black', linewidth=1.2)
plt.title('Histogram of Mjob')
plt.xlabel('Job')
plt.xticks(rotation=0)
plt.ylabel('Frequency')
plt.show()

data['Fjob'].value_counts().plot(kind='bar', color='blue', edgecolor='black', linewidth=1.2)
plt.title('Histogram of Fjob')
plt.xlabel('Job')
plt.xticks(rotation=0)
plt.ylabel('Frequency')
plt.show()

data['age'].plot(kind='hist',color='blue', edgecolor='black', linewidth=1.2)
plt.title('Histogram of age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

data['Dalc'].plot(kind='hist',color='blue', edgecolor='black', linewidth=1.2)
plt.title('Histogram of Daily Alcohol Consumption')
plt.xlabel('Daily Alcohol Consumption')
plt.ylabel('Frequency')
plt.show()

data['Walc'].plot(kind='hist',color='blue', edgecolor='black', linewidth=1.2)
plt.title('Histogram of Weekly Alcohol Consumption')
plt.xlabel('Weekly Alcohol Consumption')
plt.ylabel('Frequency')
plt.show()

data['absences'].plot(kind='hist',color='blue', edgecolor='black', linewidth=1.2)
plt.title('Histogram of Absences')
plt.xlabel('Absences')
plt.ylabel('Frequency')
plt.show()