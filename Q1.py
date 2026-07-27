import re

resume = """
Name: Rahul Sharma
Email: rahul@gmail.com
Mobile: 9876543210
Skills: Python, SQL, Machine Learning, NLP
Experience: 3 years
"""

# Extract Name
name = re.search(r"Name:\s*(.*)", resume)
print("Candidate Name:", name.group(1))

# Extract Email
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", resume)
print("Email:", emails)

# Extract Mobile Number
mobile = re.findall(r"\b\d{10}\b", resume)
print("Mobile:", mobile)

# Detect Skills
skills = ["Python", "Java", "SQL", "Machine Learning", "NLP"]
found_skills = []

for skill in skills:
    if re.search(skill, resume, re.IGNORECASE):
        found_skills.append(skill)

print("Skills:", found_skills)

# Extract Experience
experience = re.search(r"(\d+)\s+years", resume)
years = int(experience.group(1))
print("Experience:", years, "Years")

# Structured Summary
print("\n------ Candidate Summary ------")
print("Name:", name.group(1))
print("Email:", emails[0])
print("Mobile:", mobile[0])
print("Skills:", ", ".join(found_skills))
print("Experience:", years, "Years")

# Eligibility
if years >= 2 and "Python" in found_skills:
    print("Eligible for Shortlisting")
else:
    print("Not Eligible")