
# Integrated University Fee and Eligibility Audit

n = int(input("Enter number of students: "))

students = []

for i in range(n):
    print("\nEnter details for Student", i + 1)

    name = input("Enter student name: ")
    total_fee = float(input("Enter total fee: "))
    paid_fee = float(input("Enter fee paid: "))
    attendance = float(input("Enter attendance percentage: "))
    internal = float(input("Enter internal marks: "))
    exam_input = input("Exam eligibility approved? (yes/no): ")

    exam_ok = exam_input.lower() == "yes"

    students.append([
        name, total_fee, paid_fee,
        attendance, internal, exam_ok
    ])

min_attendance = float(input("\nEnter minimum attendance: "))
min_internal = float(input("Enter minimum internal marks: "))

fee_total = 0
attendance_total = 0
internal_total = 0
exam_total = 0

print("\nUNIVERSITY FEE AND ELIGIBILITY AUDIT")
print("=" * 50)

for student in students:
    name, total_fee, paid_fee, attendance, internal, exam_ok = student

    reasons = []
    balance = total_fee - paid_fee

    # Fee audit
    if balance > 0:
        reasons.append("Outstanding fee: Rs." + str(round(balance, 2)))
        fee_total += 1

    # Attendance audit
    if attendance < min_attendance:
        reasons.append("Attendance below minimum")
        attendance_total += 1

    # Internal marks audit
    if internal < min_internal:
        reasons.append("Internal marks below minimum")
        internal_total += 1

    # Examination eligibility audit
    if not exam_ok:
        reasons.append("Exam eligibility not approved")
        exam_total += 1

    print("\nStudent:", name)

    if len(reasons) == 0:
        print("Status: ALL CLEAR")
    else:
        print("Status: OUTSTANDING")
        for reason in reasons:
            print("-", reason)

# Reason-wise summary
print("\n" + "=" * 50)
print("REASON-WISE AUDIT SUMMARY")
print("Students with outstanding fees:", fee_total)
print("Students with low attendance:", attendance_total)
print("Students with low internal marks:", internal_total)
print("Students without exam approval:", exam_total)
