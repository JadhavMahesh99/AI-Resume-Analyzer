📄 ATS Resume Analyzer

A Python-based ATS (Applicant Tracking System) Resume Analyzer that reads resumes and matches skills against a predefined list. It supports **PDF and DOCX files** and gives a score based on skill matching.

---

🚀 Features

- 📄 PDF & DOCX resume support  
- 🧠 Skill extraction using Python logic  
- 📊 ATS score calculation (/100)  
- ❌ Missing skills detection  
- ⚡ Lightweight and fast execution  

---

🛠️ Tech Stack

- Python  
- PyPDF2  
- python-docx  

---

## 📂 Project Structure

ATS-Resume-Analyzer/
├── main.py
├── sample_resume.txt
├── README.md

---

## ▶️ How to Run

1. Install dependencies
```bash
pip install PyPDF2 python-docx

2. Run program
python main.py

3. Enter file name
resume.pdf
or
resume.docx

📊 Sample Output
Skills Found:
- Python
- SQL

Resume Score: 40 / 100
Match Percentage: 40%

Missing Skills:
- Git
- Machine Learning

🎯 Purpose
This project simulates a real-world ATS system used in recruitment and helps understand:
File handling in Python
Resume parsing
Basic text processing
Real-world project structuring

👨‍💻 Author
Mahesh Jadhav
AIML Engineering Student
Interested in AI, Cybersecurity, and Software Development
