import streamlit as st

# Comprehensive list of skills/tools for data-related fields
data_skills_tools = [
    "python", "r", "java", "sql", "scala", "tableau", "power bi", "excel","visual studio code"
    "vs code", "matplotlib", "seaborn", "deep learning", "nlp", "tensorflow", "model", "git", 
    "github", "pytorch", "apache spark", "aws", "azure", "google cloud", 
    "postgresql", "mysql", "mongodb", "snowflake", "teamwork", "communication",
    "crm platforms", "hubspot", "google analytics", "tag manager", "dashboards", "visualizations"
    "salesforce", "databox", "customer acquisition", "campaign performance", 
    "revenue metrics", "problem-solving", "collaboration"
]

# Page title
st.title("Skills Match App for Data Roles")

# Input fields for job description and candidate skills
job_description = st.text_area("Paste the job requirements:")
candidate_profile = st.text_area("Paste the candidate skills:")

# Matching analysis
if st.button("Analyze Match"):
    if job_description and candidate_profile:
        # Extract matches using the comprehensive list
        matching_skills = [skill for skill in data_skills_tools if skill.lower() in job_description.lower()]
        candidate_skills = [skill for skill in data_skills_tools if skill.lower() in candidate_profile.lower()]

        # Find mismatches
        missing_skills = [skill for skill in matching_skills if skill not in candidate_skills]

        # Calculate match percentage
        skill_matches = len([skill for skill in candidate_skills if skill in matching_skills])
        total_matches = skill_matches
        total_requirements = len(matching_skills)
        match_percentage = (total_matches / total_requirements) * 100 if total_requirements > 0 else 0

        # Display results
        st.header("Match Analysis")

        # Match percentage with color formatting
        if match_percentage >= 80:
            st.markdown(f"<p style='color:green; font-size:24px;'>Match Percentage: {match_percentage:.2f}%</p>", unsafe_allow_html=True)
        elif match_percentage >= 50:
            st.markdown(f"<p style='color:orange; font-size:24px;'>Match Percentage: {match_percentage:.2f}%</p>", unsafe_allow_html=True)
        else:
            st.markdown(f"<p style='color:red; font-size:24px;'>Match Percentage: {match_percentage:.2f}%</p>", unsafe_allow_html=True)

        # Matched skills
        st.subheader("Matched Skills")
        if candidate_skills:
            for skill in candidate_skills:
                st.write(f"• {skill}")
        else:
            st.write("None")

        # Missing skills
        st.subheader("Missing Skills")
        if missing_skills:
            for skill in missing_skills:
                st.write(f"• {skill}")
        else:
            st.write("None")
    else:
        st.error("Please provide both job description and candidate profile.")
