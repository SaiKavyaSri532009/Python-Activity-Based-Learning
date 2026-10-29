print("EXAMINATION SEATING ARRANGEMENT")
print("-" * 45)
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
capacity = rows * cols
reserved = []
n = int(input("Enter number of reserved seats: "))
for i in range(n):
    r = int(input("Enter reserved seat row: "))
    c = int(input("Enter reserved seat column: "))
    if 1 <= r <= rows and 1 <= c <= cols:
        reserved.append((r, c))
    else:
        print("Invalid seat position!")
student_no = 1
occupied = 0
reserved_count = 0
empty = 0
print("\nTotal classroom capacity:", capacity)
print("-" * 45)
for r in range(1, rows + 1):
    for c in range(1, cols + 1):
        if (r, c) in reserved:
            seat = "RESERVED"
            reserved_count += 1
        elif c % 2 == 0:
            seat = "EMPTY"
            empty += 1
        else:
            seat = "S" + str(student_no)
            student_no += 1
            occupied += 1
        print("R" + str(r) + "C" + str(c) + ": "
              + seat, end=" | ")
    print()
print("-" * 45)
print("Students seated:", occupied)
print("Reserved seats:", reserved_count)
print("Empty seats:", empty)
print("Total classroom capacity:", capacity)