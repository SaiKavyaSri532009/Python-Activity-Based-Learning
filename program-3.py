print("STUDENT EMAIL VALIDATION")
print("-" * 40)

n = int(input("Enter number of students: "))
for i in range(n):
    email = input("Enter email address: ")
    errors = []
    parts = email.split("@")
    if email.count("@") != 1:
        errors.append("Incorrect @ separator")
    else:
        username = parts[0]
        domain = parts[1]
        if username == "":
            errors.append("Missing username")
        if domain == "":
            errors.append("Missing domain")
        elif "." not in domain:
            errors.append("Missing domain extension")
        else:
            domain_parts = domain.split(".")
            if any(part == "" for part in domain_parts):
                errors.append("Malformed dot separator")
        allowed = (
            "abcdefghijklmnopqrstuvwxyz"
            "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            "0123456789._"
        )
        for ch in username:
            if ch not in allowed:
                errors.append("Invalid username character")
                break
        if username.startswith(".") or username.endswith("."):
            errors.append("Invalid dot position")
        if ".." in username:
            errors.append("Repeated dots in username")
        for ch in domain:
            if ch not in (
                "abcdefghijklmnopqrstuvwxyz"
                "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                "0123456789.-"
            ):
                errors.append("Invalid domain character")
                break
    if errors:
        print(email, "-> INVALID:", ", ".join(errors))
    else:
        print(email, "-> VALID")
print("\nREGISTRATION ID VALIDATION")
print("-" * 40)
for i in range(n):
    reg_id = input("Enter registration ID: ")
    if len(reg_id) != 6:
        print(reg_id, "-> INVALID: Must contain 6 characters")
    elif not reg_id.startswith("BT"):
        print(reg_id, "-> INVALID: Must start with BT")
    elif not reg_id[2:].isdigit():
        print(reg_id, "-> INVALID: Last 4 characters must be digits")
    else:
        print(reg_id, "-> VALID")