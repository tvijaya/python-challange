
import os
import csv


months = []
revenue = []
change_revenue = []
months_revenue = dict()
with open("budget_data_1.csv", newline = '') as csvfile:
    csvreader = csv.reader(csvfile , delimiter = ',')
    next(csvreader, None)
    for row in csvreader:
        months.append(row[0])
        revenue.append(int(row[1]))
        months_revenue[row[0]] = int(row[1])
    

unique_months = set(months)
total_revenue = sum(revenue)
sortedValues  = sorted(months_revenue.values())

for i in range(0, len(revenue) -1):  
    change_revenue.append(int(revenue[i+1]) - int(revenue[i]))

print("Financial Analysis:")
print("____________________")
print("Total Months: " + str(len(unique_months)))
print("Total Revenue: $" + str(total_revenue))
print("Average Revenue Change: $"+ str(round(sum(change_revenue) / float(len(change_revenue)), 2)))



for key, value in months_revenue.items():
        if (value == sortedValues[0]) : #first element in sorted list is the least
            print("Greatest Decrease in Revenue: " + str(key) + "  ($" + str(value) + ")")
        if(value == sortedValues[len(sortedValues)-1]): #last element in sorted list is the highest
            print("Greatest Increase in Revenue: " + str(key) + "  ($" + str(value) + ")")


with open("budget_results_1.txt", 'w') as text_file:
    text_file.write("Financial Analysis: \n")
    text_file.write("_________________\n")
    text_file.write("Total Months: " + str(len(unique_months)) + "\n")
    text_file.write("Total Revenue: $" + str(total_revenue) + "\n")
    text_file.write("Average Revenue Change: $"+ str(round(sum(change_revenue) / float(len(change_revenue)), 2)) + "\n")
    for key, value in months_revenue.items():
        if (value == sortedValues[0]) : #first element in sorted list is the least
            text_file.write("Greatest Decrease in Revenue: " + str(key) + "  ($" + str(value) + ") \n")
        if(value == sortedValues[len(sortedValues)-1]): #last element in sorted list is the highest
            text_file.write("Greatest Increase in Revenue: " + str(key) + "  ($" + str(value) + ") \n")