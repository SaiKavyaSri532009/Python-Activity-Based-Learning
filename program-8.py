
# Campus Event Seating and Entry Validation

n = int(input("Enter number of registered students: "))
registered_ids = []

for i in range(n):
    reg_id = input("Enter registration ID: ")
    registered_ids.append(reg_id)

m = int(input("\nEnter number of tickets: "))
tickets = []

for i in range(m):
    print("\nTicket", i + 1)
    ticket_id = input("Enter ticket ID: ")
    reg_id = input("Enter registration ID: ")
    tickets.append((ticket_id, reg_id))

rows = int(input("\nEnter number of rows: "))
cols = int(input("Enter seats per row: "))

capacity = rows * cols

# Create seating matrix
seats = [["EMPTY" for c in range(cols)]
         for r in range(rows)]

entered_ids = []
valid_count = 0
invalid_count = 0
duplicate_count = 0
full_count = 0

print("\nCAMPUS EVENT ENTRY VALIDATION")
print("-" * 45)

for ticket_id, reg_id in tickets:
    print("\nTicket:", ticket_id, "Registration:", reg_id)

    if reg_id not in registered_ids:
        print("Status: INVALID - Not registered")
        invalid_count += 1

    elif reg_id in entered_ids:
        print("Status: DUPLICATE ENTRY")
        duplicate_count += 1

    else:
        assigned = False

        # Find the first available seat
        for r in range(rows):
            for c in range(cols):
                if seats[r][c] == "EMPTY" and not assigned:
                    seats[r][c] = reg_id
                    entered_ids.append(reg_id)
                    valid_count += 1
                    assigned = True

                    print("Status: VALID")
                    print("Seat: Row", r + 1,
                          "Column", c + 1)

        if not assigned:
            print("Status: REJECTED - Auditorium full")
            full_count += 1

# Display seating arrangement
print("\nSEATING ARRANGEMENT")
print("-" * 45)

for r in range(rows):
    for c in range(cols):
        print("R" + str(r + 1) + "C" + str(c + 1)
              + ":" + seats[r][c], end=" | ")
    print()

available = capacity - valid_count

print("\nEVENT SUMMARY")
print("-" * 45)
print("Total seating capacity:", capacity)
print("Valid entries:", valid_count)
print("Invalid tickets:", invalid_count)
print("Duplicate entries:", duplicate_count)
print("Rejected due to full auditorium:", full_count)
print("Occupied seats:", valid_count)
print("Available seats:", available)
