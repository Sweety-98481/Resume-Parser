import os
import csv
from utils import (
    extract_text_from_pdf, clean_text, extract_email,
    extract_phone, extract_name, extract_skills,
    extract_education, extract_experience
)

resumes_folder = 'resumes'
output_file = 'output/resume_data.csv'
os.makedirs('output', exist_ok=True)

fieldnames = ['Name', 'Email', 'Phone', 'Skills', 'Education', 'Experience']
file_exists = os.path.isfile(output_file)

with open(output_file, mode='a', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    if not file_exists:
        writer.writeheader()

    for filename in os.listdir(resumes_folder):
        if filename.endswith('.pdf'):
            file_path = os.path.join(resumes_folder, filename)
            print(f"\n📄 Processing: {filename}")

            # Step 1: Extract & clean text
            raw_text = extract_text_from_pdf(file_path)
            cleaned_text = clean_text(raw_text)

            # Step 2: Extract info
            name = extract_name(cleaned_text)
            email = extract_email(cleaned_text)
            phone = extract_phone(cleaned_text)
            skills = extract_skills(cleaned_text)
            education = extract_education(cleaned_text)
            experience = extract_experience(cleaned_text)

            # Step 3: Save to CSV
            writer.writerow({
                'Name': name,
                'Email': email,
                'Phone': phone,
                'Skills': ", ".join(skills),
                'Education': " | ".join(education),
                'Experience': " | ".join(experience)
            })

print("\n✅ All resumes processed and saved to output/resume_data.csv")
