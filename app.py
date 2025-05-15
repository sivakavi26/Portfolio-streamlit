import streamlit as st


intro_page = st.Page("Intro.py", title = "Home", icon = ":material/home:")
skills_page = st.Page("Skills.py", title = "My Skills", icon = ":material/palette:")
ach_page = st.Page("Achievements.py", title = "Professional Achievements", icon = ":material/work:")
project_page = st.Page("Projects.py", title = "Projects & Certifications", icon = ":material/sports_score:")
conn_page = st.Page("LetsConnect.py", title = "Let's Connect", icon = ":material/hub:")

pg = st.navigation(
    {
        "Navigate Here" : [intro_page, skills_page, ach_page, project_page, conn_page]
    })

pg.run() 