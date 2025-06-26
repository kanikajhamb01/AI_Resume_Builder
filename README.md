# 🤖 AI Resume Builder

An AI-powered resume generator using **Streamlit** and **OpenAI GPT-4 API**.  
It takes user input and creates an ATS-optimized `.docx` resume with quantified bullet points and project descriptions.

---

## 🚀 Features

- 🔐 Secure OpenAI API key input (via sidebar)
- 📝 Simple UI form for resume details
- 📄 Generates `.docx` resume using `python-docx`
- 🎯 AI-generated bullet points for work experience and projects
- 🧠 Powered by OpenAI GPT-4 via `openai` Python SDK

---

## 📦 Tech Stack

- Python
- Streamlit
- OpenAI API
- python-docx

---

## 📂 How to Run Locally

### 1️⃣ Clone the Repo

git clone https://github.com/kanikajhamb01/AI_Resume_Builder.git
cd AI_Resume_Builder
--
### 2️⃣ Create a Virtual Environment

Copy code
python -m venv venv
# Activate it:
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate

### 3️⃣ Install Dependencies

Copy code
pip install -r requirements.txt

### 4️⃣ Run the App

Copy code
streamlit run app.py

