import PyPDF2
import docx

skills = [
    "Python", "Java", "C Programming", "SQL",
    "Git", "Machine Learning", "Cybersecurity",
    "Data Structures", "HTML", "CSS"
]

def read_pdf(file_path):
    text = ""
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    return text

def read_docx(file_path):
    doc = docx.Document(file_path)
    text = ""
    for para in doc.paragraphs:
        text += para.text + " "
    return text

def analyze_resume(text):
    text = text.lower()

    found_skills = []
    missing_skills = []

    for skill in skills:
        if skill.lower() in text:
            found_skills.append(skill)
        else:
            missing_skills.append(skill)

    print("\n===== ATS RESUME ANALYZER =====\n")

    print("✔ Found Skills:")
    for skill in found_skills:
        print("-", skill)

    score = len(found_skills) * 10
    print("\n📊 Score:", score, "/100")

    percentage = (len(found_skills) / len(skills)) * 100
    print("📈 Match %:", round(percentage, 2), "%")

    print("\n❌ Missing Skills:")
    for skill in missing_skills:
        print("-", skill)


file_path = input("Enter file name (pdf/docx): ")

if file_path.endswith(".pdf"):
    resume_text = read_pdf(file_path)
elif file_path.endswith(".docx"):
    resume_text = read_docx(file_path)
else:
    print("❌ Only PDF or DOCX supported")
    exit()

analyze_resume(resume_text)
    print("-", skill)
