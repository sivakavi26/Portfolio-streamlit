import streamlit as st
from streamlit_option_menu import option_menu
import requests 
from streamlit_lottie import st_lottie
# Setting Page Config, must remain at top
st.set_page_config(page_title="My Portfolio ", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Creating Functions for differet Sections
# Home Function --------------------------------------------------------------------------------------------------------------
def Home():
    st.markdown("""
    ## Hi, I'm Raj 👋
    # A Data Science Student
    By day, I'm diving deep into **Data Structures and Algorithms (DSA)**, and by night, I'm exploring the vast worlds of Data Science, including **Data Analysis**, **Machine Learning**, and **Deep Learning**. My journey also includes working on cutting-edge *Large Language Models*, bringing innovative ideas to fruition. My technical arsenal includes **Python**, **C++**, **SQL**, **React.js**, **Streamlit**, **pandas**, **numpy**, **matplotlib**, **Plotly**, and **seaborn**, to name a few. 
    
    My portfolio is a treasure trove of diverse projects, from building pathfinder visualizers and Gemini API clones to developing interactive data visualization tools. Whether it's crafting complex algorithms or designing captivating user interfaces, I'm your go-to person for all things development. When I'm not coding, you can find me exploring the latest tech trends or honing my problem-solving skills. I'm always eager to learn and grow, and I'm excited about where my passion for Data Science and development will take me next. If you're looking to bring your ideas to life, let's collaborate and create something extraordinary together!

    📂 Here, you will find a collection of my **projects**, **achievements**, and **insights** into the world of data science and artificial intelligence. 🌐 Explore and feel free to reach out if you have any questions or collaboration ideas!

    📫 Connect with me on [LinkedIn](https://www.linkedin.com/in/raj-tripathi-6208ab241/) || [GitHub](https://github.com/RAJTripathi3030) ||  [Email](mailto:t.raj.ripathi@gmail.com)
    """)
    st.write("Here's my resume:")
    with open("Raj-Tripathi-FlowCV-Resume-20240803 (1).pdf", "rb") as file:
        btn = st.download_button(
            label="Download Resume",
            data=file,
            file_name="Raj-Tripathi-FlowCV-Resume-20240803 (1).pdf",
            mime="application/pdf"
        )
    lottie_url = "https://lottie.host/f56472c3-2021-4eb8-92e2-39ea06345f42/1L7J5mRwno.json"
    lottie_animation = load_lottieurl(lottie_url)
    if lottie_animation:
        st_lottie(lottie_animation, speed=1, height=300, key="home")
    else:
        st.error("Failed to load Lottie animation.")
    

# Projects Function --------------------------------------------------------------------------------------------------------------
def Projects():
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
    with st.container():
        st.write("---")
        st.write("##")
        img_col, text_col = st.columns((1, 2))
        with img_col:
            lottie_url = "https://lottie.host/f2e469ad-fe3c-471c-a817-b1768ab0312f/Yh7qlSV0Uq.json"
            lottie_animation = load_lottieurl(lottie_url)
            if lottie_animation:
                st_lottie(lottie_animation, speed=1, height=300, key="project5")
            else:
                st.error("Failed to load Lottie animation.")
                
        with text_col:
            st.write("### Movie Recommender System")
            st.write("""
                    - Developed an advanced recommender system, leveraging collaborative filtering and content-based filtering techniques.
                    - Designed a user-friendly interface that allows seamless product discovery, significantly enhancing user engagement and satisfaction.
                    - Implemented a robust algorithm that analyzes user behavior and preferences, providing personalized product recommendations with high accuracy.
                    """)
            if st.button("Know More 😄"):
                with st.expander("### Technologies Used", expanded=False):
                    col1, col2 = st.columns(2)
                    with col1:
                        st.write("- Python")
                        st.write("- Pandas")
                        st.write("- NumPy")
                    with col2:
                        st.write("- Scikit-Learn")
                        st.write("- Streamlit")
                        st.write("- NLTK")
                
                with st.expander("### Project Link", expanded = False):
                    st.write("[View the live demo here](https://recommender-system-app.streamlit.app/)")
# Achievements Function --------------------------------------------------------------------------------------------------------------
def Achievements():
    with st.container():
        st.write("# 🏆 My Achievements")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
                        - 🧠 Solved 300+ questions on LeetCode. I'm on a roll!
                        - 🌟 Topped the DevStar Bootcamp. Yes, I did that!
                        - ⚽ Winner of the Intra-School Football Championship. Go team!
                    """)
            st.markdown("""
                        I believe that every achievement, big or small, is a stepping stone towards success. I am always eager to learn and grow, and I am excited to see what the future holds for me. 🚀
                        """)
        with col2:
            lottie_url = "https://lottie.host/a7990eb1-5152-4cd1-a7fd-e0c592683b97/KOvlwaJ4uL.json"
            lottie_animation = load_lottieurl(lottie_url)
            if lottie_animation:
                st_lottie(lottie_animation, speed=1, height=300, key="achievements")
            else:
                st.error("Failed to load Lottie animation.")
        st.write("---")
        st.write("# 📚 I Like To Talk About")
        st.markdown("""
                    - **Data Science**
                    - **Machine Learning**
                    - **Deep Learning**
                    - **Artificial Intelligence**
                    - **Computer Vision**
                    - **Natural Language Processing**
                    - **Data Structures & Algorithms**
                    - **Self-Improvement** 
                    """) 

# Skills Function --------------------------------------------------------------------------------------------------------------
def Skills():
    
    with st.container():
        st.write("### 💼 My Skills")
        col1, col2 = st.columns(2)
        with col1:
            st.write("""
                    - **Languages**: Python, C++, SQL, CSS, HTML, JavaScript
                    - **Libraries**: Pandas, Numpy, Matplotlib, Plotly, Seaborn
                    - **Frameworks**: Streamlit, React.js, Bootstrap CSS
                    - **Tools**: Git, Docker, Jupyter Notebook, VS Code
                    - **Databases**: MySQL, Vector Databases
                    - **Machine Learning**: Scikit-learn & Machine Learining Algorithms
                    - **Deep Learning**: Tensorflow, Keras, OpenCV, NLP & it's Libraries 
                    - **Soft Skills**: Teamwork, Communication, Problem-Solving, Time Management, Adaptability
                    - **Others**: Data Structures & Algorithms, Computer Vision, Natural Language Processing
                """)
        with col2:
            lottie_url = "https://lottie.host/e0f72cc9-db24-4eac-a85e-19bb821629f9/mumuEVoTHL.json"
            lottie_animation = load_lottieurl(lottie_url)
            if lottie_animation:
                st_lottie(lottie_animation, speed=1, height=300, key="skills")
            else:
                st.error("Failed to load Lottie animation.")

# Setting Sidebar Main Menu ------------------------------------------------------------------------------------------------------------
with st.sidebar:
    selected_page = option_menu(
        "Navigate Here", 
        ["Home", "Projects", "Achievements","Skills"],
        icons = ['house', 'braces', 'trophy', 'code'],
        menu_icon = "cast",
        default_index = 0,
        )

# Displaying Selected Page --------------------------------------------------------------------------------------------------------------

if selected_page == "Home":
    Home()
elif selected_page == "Projects":
    Projects()
elif selected_page == "Achievements":
    Achievements()
elif selected_page == "Skills":
    Skills()