
# Repeated Transaction Detection

n = int(input("Enter number of transactions: "))

transactions = []

for i in range(n):
    print("\nTransaction", i + 1)
    tid = input("Enter transaction ID: ")
    amount = float(input("Enter transaction amount: "))
    transactions.append((tid, amount))

threshold = float(input("\nEnter transaction threshold: "))

suspicious = []
seen = []

for transaction in transactions:
    tid, amount = transaction
    reasons = []

    if tid in seen:
        reasons.append("Duplicate transaction")
    else:
        seen.append(tid)

    if amount > threshold:
        reasons.append("Threshold violation")

    if reasons:
        suspicious.append((tid, amount, reasons))

print("\nSUSPICIOUS TRANSACTIONS")
print("-" * 45)

if len(suspicious) == 0:
    print("No suspicious transactions found.")
else:
    for item in suspicious:
        print("Transaction ID:", item[0])
        print("Amount: Rs.", item[1])
        print("Reasons:", ", ".join(item[2]))
        print("-" * 45)

print("Total transactions:", len(transactions))
print("Suspicious entries:", len(suspicious))
