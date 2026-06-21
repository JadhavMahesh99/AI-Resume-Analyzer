skills = [
    "Python",
    "Java",
    "SQL",
    "Git",
    "Machine Learning",
    "Data Structures"
]

with open("sample_resume.txt", "r") as file:
    resume_text = file.read()
    
found_skills = []

for skill in skills:
    if skill.lower() in resume_text.lower():
        found_skills.append(skill)

print("Skills Found:")

for skill in found_skills:
    print("-", skill)

score = len(found_skills) * 15

print("\nResume Score:", score)

missing_skills = []

for skill in skills:
    if skill.lower() not in resume_text.lower():
        missing_skills.append(skill)

print("\nMissing Skills:")

for skill in missing_skills:
    print("-", skill)
