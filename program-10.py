# University Scholarship Allocation

n = int(input("Enter number of applicants: "))
applicants = []

for i in range(n):
    print("\nApplicant", i + 1)

    sid = int(input("Enter applicant ID: "))
    name = input("Enter applicant name: ")
    aggregate = float(input("Enter aggregate marks: "))

    subjects = []
    for j in range(3):
        mark = float(input(
            "Enter marks for subject " + str(j + 1) + ": "
        ))
        subjects.append(mark)

    attendance = float(input("Enter attendance percentage: "))
    income = float(input("Enter annual family income: "))

    applicants.append(
        (sid, name, aggregate, tuple(subjects), attendance, income)
    )

# Eligibility criteria
MIN_AGGREGATE = float(input("\nMinimum aggregate marks: "))
MIN_SUBJECT = float(input("Minimum subject marks: "))
MIN_ATTENDANCE = float(input("Minimum attendance percentage: "))
MAX_INCOME = float(input("Maximum annual family income: "))

eligible = []
rejected = []

# Stage 1: Check eligibility
for student in applicants:
    sid, name, aggregate, subjects, attendance, income = student

    if (aggregate >= MIN_AGGREGATE
            and all(mark >= MIN_SUBJECT for mark in subjects)
            and attendance >= MIN_ATTENDANCE
            and income <= MAX_INCOME):

        eligible.append(student)
    else:
        rejected.append(student)

# Stage 2: Rank eligible applicants
# 1. Higher aggregate
# 2. Higher attendance
# 3. Lower family income
# 4. Lower applicant ID

eligible.sort(key=lambda s: (-s[2], -s[4], s[5], s[0]))

# Stage 3: Display results
print("\nUNIVERSITY SCHOLARSHIP ALLOCATION")
print("=" * 65)

if not eligible:
    print("No eligible students found.")
else:
    print("Rank ID Name Aggregate Attendance Income")
    for rank, student in enumerate(eligible, start=1):
        sid, name, aggregate, subjects, attendance, income = student
        print(rank, sid, name, aggregate, attendance, income)

print("\nRejected Applicants")
for student in rejected:
    print(student[0], student[1], "- Not eligible")

print("\nTotal applicants:", len(applicants))
print("Eligible applicants:", len(eligible))
print("Rejected applicants:", len(rejected))

