# Student Marks Matrix Analysis
n = int(input("Enter number of students: "))
m = int(input("Enter number of subjects: "))
students = []
subjects = []
marks = []
# Input student names
for i in range(n):
    name = input("Enter student name: ")
    students.append(name)
# Input subject names
for j in range(m):
    subject = input("Enter subject name: ")
    subjects.append(subject)
# Input marks matrix
for i in range(n):
    row = []
    print("Enter marks for", students[i])
    for j in range(m):
        mark = float(input("Enter marks in " + subjects[j] + ": "))
        row.append(mark)
    marks.append(row)
low_threshold = float(input("Enter low-average threshold: "))
# Row-wise analysis
averages = []
print("\nSTUDENT-WISE AVERAGES")
for i in range(n):
    total = sum(marks[i])
    average = total / m
    averages.append(average)
    print(students[i], "Average:", round(average, 2))
# Identify top performer
top_index = 0
for i in range(1, len(averages)):
    if averages[i] > averages[top_index]:
        top_index = i
print("\nTop Performer:", students[top_index])
print("Highest Average:", round(averages[top_index], 2))
# Column-wise analysis
print("\nSUBJECT-WISE AVERAGES")
low_subjects = []
for j in range(m):
    total = 0
    for i in range(n):
        total += marks[i][j]
    average = total / n
    print(subjects[j], "Average:", round(average, 2))
    if average < low_threshold:
        low_subjects.append(subjects[j])
print("\nSUBJECTS WITH LOW AVERAGES (below",
      low_threshold, "):")
if len(low_subjects) > 0:
    for subject in low_subjects:
        print(subject)
else:
    print("No low-performing subjects found.")


