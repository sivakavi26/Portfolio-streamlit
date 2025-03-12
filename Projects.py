import streamlit as st
import requests 
from streamlit_lottie import st_lottie


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


st.title('My Projects')
# Project 1 Container
with st.container():
        img_col, text_col = st.columns((1, 2))
        with img_col:
            lottie_url = "https://lottie.host/eee3dbab-2db1-47ff-8517-bbe523b2e542/DJxtNRMpWw.json"
            lottie_animation = load_lottieurl(lottie_url)
            if lottie_animation:
                st_lottie(lottie_animation, speed=1, height=300, key="project1")
            else:
                st.error("Failed to load Lottie animation.")
        with text_col:
            # Enter Desctipion
            st.write("### Steam Game Analyzer")
            st.write("""
                    - Developed a streamlined analysis tool using Streamlit, enabling efficiant game data exploration.
                    - Utilised data analysis techniques to provide actionable insights.
                    - Recieved positive feedback from 100+ users for creating a user-friendly interface.
                    """)
            if st.button("Know More ➡️"):
                with st.expander("### Technologies Used", expanded=False):
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.write("- Python")
                        st.write("- Streamlit")
                        st.write("- Pandas")
                    with col2:
                        st.write("- Plotly")
                        st.write("- Seaborn")
                        st.write("- Numpy")
                    with col3:
                        st.write("- Matplotlib")
                        
                with st.expander("### Project Link", expanded = False):
                    st.write("[Try the Steam Game Analyzer](https://steam-streamli-app.streamlit.app/)")
                    
                with st.expander("Features", expanded = False):
                    st.write("""
                            - **Data Exploration**: Analyze game data based on various attributes.
                            - **Data Visualization**: Visualize data using interactive plots.
                            - **User-Friendly Interface**: Easy-to-use interface for all users.
                            - **Added Features**: Analyse games based on the trophies they won and the number of DLCs they have.
                            """)
    
# Project 2 Container
with st.container():
        st.write("---")
        st.write("##")
        img_col, text_col = st.columns((1, 2))
        with img_col:
            lottie_url = "https://lottie.host/01132fcd-221d-4491-8c99-6ce0f1127dd7/lJxZcH3eAt.json"
            lottie_animation = load_lottieurl(lottie_url)
            if lottie_animation:
                st_lottie(lottie_animation, speed=1, height=300, key="project2")
            else:
                st.error("Failed to load Lottie animation.")
        with text_col:
            st.write("### PresentSeek : The Attendance Management System")
            st.write("""
                    - Implemented detailed dashboards for over 1,000 students, enhancing attendance accuracy by 25%.
                    -  Reduced time spent on attendance management by 30%, streamlining administrative processes.
                    """)
            if st.button("Know More 🚀"):
                with st.expander("### Technologies Used", expanded=False):
                    col1, col2 = st.columns(2)
                    with col1:
                        st.write("- HTML")
                        st.write("- CSS")
                        st.write("- JavaScript")
                    with col2:
                        st.write("- BootStrap CSS")
                        st.write("- PHP")
                        st.write("- MySQL")
                
                with st.expander("### Project Link", expanded = False):
                    st.write("[PresentSeek's Repo](https://github.com/RAJTripathi3030/PresentSeek)")
                    
                with st.expander("Features", expanded = False):
                    st.write("""
                            - **Detailed Dashboards**: View detailed attendance reports for each student.
                            - **Attendance Management**: Manage attendance for over 1,000 students.
                            - **Streamlined Processes**: Reduce time spent on administrative tasks.
                            - **User-Friendly Interface**: Easy-to-use interface for all users.
                            """)
    
# Project 3 Container
with st.container():
        st.write("---")
        st.write("##")
        img_col, text_col = st.columns((1, 2))
        with img_col:
            lottie_url = "https://lottie.host/26387e36-3492-4465-9f16-fbf9db4a4807/YuzVL6WIpe.json"
            lottie_animation = load_lottieurl(lottie_url)
            if lottie_animation:
                st_lottie(lottie_animation, speed=1, height=300, key="project3")
            else:
                st.error("Failed to load Lottie animation.")
        with text_col:
            st.write("### EDA Projet on Suicide Dataset")
            st.write("""
                    - Analyzed 10 years of suicide rate data across multiple regions, identifying a 15% increase in specific areas.
                    - Pinpointed significant changes using statistical methods, revealing a 10% spike in 2017.
                    - Mapped trends showing a 20% higher rate in urban areas compared to rural ones.
                    """)
            if st.button("Know More 🎂"):
                with st.expander("### Technologies Used", expanded=False):
                    col1, col2 = st.columns(2)
                    with col1:
                        st.write("- Python")
                        st.write("- Pandas")
                        st.write("- Numpy")
                    with col2:
                        st.write("- Matplotlib")
                        st.write("- Seaborn")
                
                with st.expander("### Project Link", expanded = False):
                    st.write("[View The Project on This Repo](https://github.com/RAJTripathi3030/Suicide-Dataset-EDA)")

# Project 4 Container
with st.container():
        st.write("---")
        st.write("##")
        img_col, text_col = st.columns((1, 2))
        with img_col:
            lottie_url = "https://lottie.host/2ba6554c-8a54-456d-b6c4-b70f155468c2/DX7lA91qJG.json"
            lottie_animation = load_lottieurl(lottie_url)
            if lottie_animation:
                st_lottie(lottie_animation, speed=1, height=300, key="project4")
            else:
                st.error("Failed to load Lottie animation.")
        with text_col:
            st.write("### Google Gemini Project")
            st.write("""
                    - Engineered a fully functional Google Gemini clone, achieving 100% feature parity and functionality replication .
                    - Crafted a pixel-perfect UI, meticulously adhering to Gemini's established design patterns and user experience guidelines .
                    - Architected the front-end using React.js, seamlessly integrating Google Gemini API for powerful LLM capabilities .
                    - Optimized performance, reducing initial load time by 20% compared to the original Gemini interface .
                    """)
            if st.button("Know More 🗯️"):
                with st.expander("### Technologies Used", expanded=False):
                    col1, col2 = st.columns(2)
                    with col1:
                        st.write("- JavaScript")
                        st.write("- React.js")
                        st.write("- LLM")
                    with col2:
                        st.write("- CSS")
                
                with st.expander("### Project Link", expanded = False):
                    st.write("[View The Project on This Repo](https://github.com/RAJTripathi3030/Gemini-Clone)")
    
    # Project 5 Container
    