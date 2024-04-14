import csv
import matplotlib.pyplot as plt
import statistics
from statistics import mean

listTotal = []
time = []

csv_file_path="screenTime.csv"

#Path to the CSV file
with open(csv_file_path, "r") as file:
    records = list(csv.reader(file))
    
for record in records:
    for item in record:
        listTotal.append(item)

for i in range(0, len(listTotal),1):
    if i+1 < len(listTotal):
        time = listTotal[i+1]

#print the data from the lists
print("Time:",time)
calcTime = int(time)
calcTime = sum(time)

emotionalWellbeing=int(input("On a scale of 1-10 from sad to happy, how do you feel ? :"))
physicalWellbeing=int(input("On a scale of 1-10 from tired to full of energy, how do you feel ? :"))
socialWellbeing=int(input("On a scale of 1-10 from lonely to great, how would you rate your social wellbeing? :"))

average=(emotionalWellbeing, physicalWellbeing, socialWellbeing)

averageScore = mean(average) # can only have one

print("Your average wellbeing score is", averageScore)

medianScore = median(average)

print("The median of your score is", medianScore)

maxScore = max(average)

print("The max of your score is", maxScore)

minScore = min(average)

print("The max of your score is", minScore)

plt.plot(time,"r-.")
plt.legend(["Time spent"])
plt.xlabel("Time")
plt.ylabel("Number of pickups")
plt.title("Time graph")
plt.show