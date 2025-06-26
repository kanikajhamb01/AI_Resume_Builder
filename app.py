import streamlit as st
from openai import OpenAI
from docx import Document
import os
import uuid

# --- Sidebar: API key ---
st.sidebar.title("🔐 API Settings")
openai_api_key = st.sidebar.text_input("Enter your OpenAI API Key", type="password")
if not openai_api_key:
    st.sidebar.warning("Please enter your OpenAI API key.")
    st.stop()

# Initialize OpenAI client
client = OpenAI(api_key=openai_api_key)

st.title("🤖 AI Resume Builder")

# --- Form UI ---
with st.form("resume_form"):
    name = st.text_input("Full Name")
    email = st.text_input("Email")
    education = st.text_input("Education")
    skills = st.text_input("Skills (comma separated)")

    st.markdown("### Work Experience")
    role = st.text_input("Job Role")
    company = st.text_input("Company Name")
    description = st.text_area("Job Description")

    st.markdown("### Project")
    project_title = st.text_input("Project Title")
    project_desc = st.text_area("Project Description")

    submit = st.form_submit_button("Generate Resume")

# --- Helper Functions ---

def generate_bullets(role, company, description):
    prompt = f"""
    Convert the following job experience into 2 strong, quantified, ATS-optimized bullet points:
    Role: {role}
    Company: {company}
    Description: {description}
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"[Error generating experience bullets: {e}]"

def generate_project_bullet(title, description):
    prompt = f"""
    Write 1 impactful bullet point for this project:
    Project: {title}
    Description: {description}
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"[Error generating project bullet: {e}]"

def create_resume(name, email, education, skills, job, company, job_desc, proj_title, proj_desc):
    doc = Document()
    doc.add_heading(name, 0)
    doc.add_paragraph(email)

    doc.add_heading("Education", level=1)
    doc.add_paragraph(education)

    doc.add_heading("Skills", level=1)
    for skill in skills.split(","):
        doc.add_paragraph(skill.strip(), style='List Bullet')

    doc.add_heading("Experience", level=1)
    bullets = generate_bullets(job, company, job_desc)
    doc.add_paragraph(f"{job} at {company}", style='List Bullet')
    for line in bullets.split("\n"):
        doc.add_paragraph(line.strip(), style='List Bullet')

    doc.add_heading("Projects", level=1)
    bullet = generate_project_bullet(proj_title, proj_desc)
    doc.add_paragraph(proj_title, style='List Bullet')
    doc.add_paragraph(bullet, style='List Bullet')

    filename = f"AI_Resume_{uuid.uuid4().hex[:6]}.docx"
    doc.save(filename)
    return filename

# --- Resume Generation and Download ---
if submit:
    if not all([name, email, education, skills, role, company, description, project_title, project_desc]):
        st.error("❗ Please fill in all fields.")
    else:
        with st.spinner("Generating your resume with AI..."):
            resume_file = create_resume(name, email, education, skills, role, company, description, project_title, project_desc)
        with open(resume_file, "rb") as file:
            st.success("✅ Resume Generated Successfully!")
            st.download_button(
                label="📥 Download Resume",
                data=file,
                file_name=resume_file,
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )
        os.remove(resume_file)

