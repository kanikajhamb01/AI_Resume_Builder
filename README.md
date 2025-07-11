# 🤖 AI Resume Builder (Powered by Gemini)

An AI-powered Streamlit application that generates professional, ATS-optimized resumes using Google Gemini. Users can export their resumes in DOCX or PDF format and choose from multiple beautifully designed templates.

---

## 🚀 Features

- 🔐 **Gemini Integration**: Uses Google Gemini API to generate resume content (experience & project bullet points).
- 📝 **Input Form**: Fill in your personal info, work experience, skills, and project details.
- 🎯 **Smart Bullet Points**: Gemini writes concise, quantified and tailored bullet points.
- 📄 **Export Formats**: Choose to download your resume as a `DOCX` or `PDF`.
- 🎨 **Multiple Templates** (PDF): Choose from `Modern`, `Classic`, or `Minimal` resume designs.
- ⚡ **Live HTML Preview** *(coming soon)*: View your resume before downloading.
- ✅ **Clean UI** with real-time feedback, error handling, and auto-download.

## 🧰 Tech Stack

| Layer              | Technology                                  | Purpose                                                      |
|--------------------|----------------------------------------------|--------------------------------------------------------------|
| **Frontend**        | [Streamlit](https://streamlit.io/)                 | Build interactive UI with user forms and resume preview      |
| **AI Integration**  | [Google Gemini API](https://aistudio.google.com/)  | Generate resume bullet points using Gemini LLM              |
| **Templating**      | [Jinja2](https://jinja.palletsprojects.com/)       | Render dynamic HTML templates for PDF export                 |
| **PDF Export**      | [WeasyPrint](https://weasyprint.org/)              | Convert HTML templates into styled PDF resumes               |
| **DOCX Export**     | [python-docx](https://python-docx.readthedocs.io/) | Programmatically create Word documents                      |
| **Resume Styling**  | HTML5 + CSS3                                       | Used in Jinja2 templates for modern resume designs           |
| **Version Control** | Git + GitHub                                       | Manage source code and track changes                         |


## 🔧 Installation

### 1. Clone the repo

git clone https://github.com/kanikajhamb01/AI_Resume_Builder.git
cd AI_Resume_Builder

### 2️⃣ Create a Virtual Environment

python -m venv venv
# Activate it:
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate

### 3️⃣ Install Dependencies

pip install -r requirements.txt

### 4️⃣ Run the App

streamlit run app.py

### 🔐 Gemini API Setup
- Get your free Gemini API Key.
- Paste it into the sidebar of the Streamlit app.

