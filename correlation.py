import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from merge import data  # Importing the 'data' variable from merge.py

## To gain a comprehensive understanding, let's begin by examining the correlation among the features.
plt.figure(figsize=(15,15))
sns.heatmap(data.corr(numeric_only=True), annot=True, fmt=".2f", cbar=True)
plt.xticks(rotation=90)
plt.yticks(rotation=0)
plt.show()

# As evident from the correlation map, only exam scores exhibit a high level of correlation with each other.
# This indicates that students tend to achieve similar grades across multiple exams.

## I intend to merge the alcohol consumption data for weekdays with that of weekends.

data['Dalc'] = data['Dalc'] + data['Walc']

## Weekly Consumption of Alcohol

# Students consume alcohol at least twice a week.

# Every student consumes alcohol; however, each student consumes alcohol at least twice a week.
list = []
for i in range(11):
    list.append(len(data[data.Dalc == i]))

colors_list = sns.color_palette("hsv", len(list))

ax = sns.barplot(x = [0,1,2,3,4,5,6,7,8,9,10], y = list, palette=colors_list)
plt.ylabel('Number of Students')
plt.xlabel('Weekly alcohol consumption')
plt.show()

## Final Exam Scored According to Student’s alcohol consumption

labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10']
explode = [0, 0, 0, 0, 0, 0, 0, 0, 0]
sizes = []
for i in range(2, 11):
    sizes.append(sum(data[data.Dalc == i].G3))
total_grade = sum(sizes)
average = total_grade / float(len(data))

colors_labels = sns.color_palette("hsv", len(labels))

plt.pie(sizes, explode=explode, colors=colors_labels, labels=labels, autopct='%1.1f%%')
plt.axis('equal')
plt.title('Total grade: ' + str(total_grade))
plt.xlabel('Students grade distribution according to weekly alcohol consumption')
plt.show()

##Students grade with grade average according to alcohol consumption 

# Final exam average grade is 10.4
# In order to understand whether alcohol affects students success, I compare grades with average.

ave = sum(data.G3)/float(len(data))
data['ave_line'] = ave
data['average'] = ['above average' if i > ave else 'under average' for i in data.G3]
sns.swarmplot(x='Dalc', y = 'G3', hue = 'average',data= data,palette={'above average':'lime', 'under average': 'red'})
plt.savefig('graph.png')
plt.show()

# As it can be seen swarm plot, student who takes highest grade consumes alcohol only 2 times in a week.

## Average G3 Score for Students who Consume Alcohol Twice a Week

sum(data[data.Dalc == 2].G3)/float(len(data[data.Dalc == 2]))

## Average grades of students based on their weekly alcohol consumption

# Calculate average grades for each level of weekly alcohol consumption
list = []
for i in range(2, 11):
    list.append(sum(data[data.Dalc == i].G3) / float(len(data[data.Dalc == i])))

ax = sns.barplot(x=[2, 3, 4, 5, 6, 7, 8, 9, 10], y=list, palette=colors_list)

plt.ylabel('Average Grades of students')
plt.xlabel('Weekly alcohol consumption')
plt.show()
