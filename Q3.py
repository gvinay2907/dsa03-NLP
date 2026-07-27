import re

reg = input("Enter Register Number: ")
email = input("Enter College Email: ")
course = input("Enter Course Code: ")
semester = input("Enter Semester: ")
mobile = input("Enter Mobile Number: ")

# Validation
reg_valid = re.fullmatch(r"\d{12}", reg)

email_valid = re.fullmatch(r"[a-zA-Z0-9._%+-]+@saveetha\.com", email)

course_valid = re.fullmatch(r"[A-Z]{3}\d{2}", course)

semester_valid = re.fullmatch(r"[1-8]", semester)

mobile_valid = re.fullmatch(r"\d{10}", mobile)

print("\nValidation Results")

if reg_valid:
    print("Register Number: Valid")
else:
    print("Register Number: Invalid")

if email_valid:
    print("Email: Valid")
else:
    print("Email: Invalid")

if course_valid:
    print("Course Code: Valid")
else:
    print("Course Code: Invalid")

if semester_valid:
    print("Semester: Valid")
else:
    print("Semester: Invalid")

if mobile_valid:
    print("Mobile Number: Valid")
else:
    print("Mobile Number: Invalid")

# Final Report
if reg_valid and email_valid and course_valid and semester_valid and mobile_valid:
    print("\nRegistration Successful")
else:
    print("\nRegistration Failed")