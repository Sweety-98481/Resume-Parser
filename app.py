import streamlit as st
from utils import (
    extract_text_from_pdf, clean_text, extract_email,
    extract_phone, extract_name, extract_skills,
    extract_education, extract_experience
)

st.title("📄 Resume Parser")

uploaded_file = st.file_uploader("Upload a resume (PDF only)", type=['pdf'])

if uploaded_file is not None:
    # Save uploaded file temporarily
    with open("temp_resume.pdf", "wb") as f:
        f.write(uploaded_file.read())

    raw_text = extract_text_from_pdf("temp_resume.pdf")
    cleaned_text = clean_text(raw_text)

    st.subheader("🔍 Extracted Information")

    name = extract_name(cleaned_text)
    email = extract_email(cleaned_text)
    phone = extract_phone(cleaned_text)
    skills = extract_skills(cleaned_text)
    education = extract_education(cleaned_text)
    experience = extract_experience(cleaned_text)

    st.write(f"**Name:** {name}")
    st.write(f"**Email:** {email}")
    st.write(f"**Phone:** {phone}")
    st.write(f"**Skills:** {', '.join(skills)}")
    st.write("**Education:**")
    st.write("\n".join(education))
    st.write("**Experience:**")
    st.write("\n".join(experience))
