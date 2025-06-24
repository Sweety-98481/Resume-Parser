import streamlit as st
import os
from streamlit.components.v1 import html

# Page settings
st.set_page_config(page_title="Resume Parser", page_icon="📄", layout="centered")

# Custom CSS styling
st.markdown("""
    <style>
        .title {
            font-size: 36px;
            font-weight: bold;
            color: #2c3e50;
            text-align: center;
            margin-bottom: 10px;
        }
        .subtitle {
            font-size: 18px;
            text-align: center;
            margin-bottom: 30px;
            color: #6c757d;
        }
        .section-title {
            font-size: 22px;
            font-weight: 600;
            color: #1abc9c;
            margin-top: 30px;
        }
        .info-block {
            background-color: #f9f9f9;
            padding: 15px;
            border-radius: 8px;
            border: 1px solid #ddd;
            margin-bottom: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Custom heading
st.markdown("<div class='title'>📄 Resume Parser</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Upload your resume to extract key details</div>", unsafe_allow_html=True)

# Import your functions
from utils import (
    extract_text_from_pdf, clean_text, extract_email,
    extract_phone, extract_name, extract_skills,
    extract_education, extract_experience
)

# Upload section
uploaded_file = st.file_uploader("Upload a resume (PDF only)", type=['pdf'])

# Processing logic
if uploaded_file is not None:
    with open("temp_resume.pdf", "wb") as f:
        f.write(uploaded_file.read())

    raw_text = extract_text_from_pdf("temp_resume.pdf")
    cleaned_text = clean_text(raw_text)

    name = extract_name(cleaned_text)
    email = extract_email(cleaned_text)
    phone = extract_phone(cleaned_text)
    skills = extract_skills(cleaned_text)
    education = extract_education(cleaned_text)
    experience = extract_experience(cleaned_text)

    # Output layout
    st.markdown("<div class='section-title'>🔍 Extracted Information</div>", unsafe_allow_html=True)

    with st.container():
        st.markdown("<div class='info-block'>", unsafe_allow_html=True)
        st.write(f"**🧑 Name:** {name}")
        st.write(f"**📧 Email:** {email}")
        st.write(f"**📱 Phone:** {phone}")
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='section-title'>🛠️ Skills</div>", unsafe_allow_html=True)
        st.markdown("<div class='info-block'>" + ", ".join(skills) + "</div>", unsafe_allow_html=True)

        st.markdown("<div class='section-title'>🎓 Education</div>", unsafe_allow_html=True)
        st.markdown("<div class='info-block'>" + "<br>".join(education) + "</div>", unsafe_allow_html=True)

        st.markdown("<div class='section-title'>💼 Experience</div>", unsafe_allow_html=True)
        st.markdown("<div class='info-block'>" + "<br>".join(experience) + "</div>", unsafe_allow_html=True)
