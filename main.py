skills = [
    "Python",
    "Java",
    "SQL",
    "Git",
    "Machine Learning",
    "Data Structures"
]

resume_text = input("Paste Resume Text: ")

found_skills = []

for skill in skills:
    if skill.lower() in resume_text.lower():
        found_skills.append(skill)

print("Skills Found:")

for skill in found_skills:
    print("-", skill)

score = len(found_skills) * 15

print("\nResume Score:", score)
