# Multi-Stage Scholarship Shortlisting System
n = int(input("Enter number of students: "))
students = []
for i in range(n):
    print("\nEnter details for student", i + 1)
    name = input("Enter student name: ")
    marks = float(input("Enter academic marks: "))
    attendance = float(input("Enter attendance percentage: "))
    income = float(input("Enter family annual income: "))
    students.append([name, marks, attendance, income])
min_marks = float(input("\nEnter minimum marks: "))
min_attendance = float(input("Enter minimum attendance: "))
max_income = float(input("Enter maximum family income: "))
quota = int(input("Enter scholarship quota: "))
eligible = []
rejected = []
# Stage 1: Check eligibility
for student in students:
    name, marks, attendance, income = student
    if (marks >= min_marks and
        attendance >= min_attendance and
        income <= max_income):
        eligible.append(student)
    else:
        rejected.append(student)
# Stage 2: Rank eligible students
# Marks descending, attendance descending,
# income ascending
n = len(eligible)
for i in range(n):
    for j in range(n - i - 1):
        a = eligible[j]
        b = eligible[j + 1]
        swap = False
        if a[1] < b[1]:
            swap = True
        elif a[1] == b[1]:
            if a[2] < b[2]:
                swap = True
            elif a[2] == b[2] and a[3] > b[3]:
                swap = True
        if swap:
            eligible[j], eligible[j + 1] = (
                eligible[j + 1], eligible[j]
            )
# Stage 3: Select candidates within quota
print("\nSCHOLARSHIP SHORTLISTING RESULTS")
print("-" * 55)
print("Eligible candidates:", len(eligible))
for i, s in enumerate(eligible):
    print(i + 1, s[0], "Marks:", s[1],
          "Attendance:", s[2], "Income:", s[3])
print("\nFINAL SCHOLARSHIP RECIPIENTS")
print("-" * 55)
selected = min(quota, len(eligible))
for i in range(selected):
    print("Rank", i + 1, "-", eligible[i][0])
print("\nScholarships available:", quota)
print("Scholarships awarded:", selected)
print("Scholarships remaining:", quota - selected)
print("\nREJECTED CANDIDATES")
for s in rejected:
    print(s[0], "- Does not meet all eligibility criteria")
