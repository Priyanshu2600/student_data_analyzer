import csv

marks = []

with open("student.CSV", "r") as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        marks.append(int(row["final_score"]))

# Calculations
average = sum(marks) / len(marks)
highest = max(marks)
lowest = min(marks)

# Output
print("Average Marks:", average)
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)
print("Total Students:", len(marks))