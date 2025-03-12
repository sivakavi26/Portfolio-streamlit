import streamlit as st
import requests 
from streamlit_lottie import st_lottie

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


st.markdown("""
    ## Hi, I'm Raj 👋
    # A Data Science Student
    By day, I'm diving deep into **Data Structures and Algorithms (DSA)**, and by night, I'm exploring the vast worlds of Data Science, including **Data Analysis**, **Machine Learning**, and **Deep Learning**. My journey also includes working on cutting-edge *Large Language Models*, bringing innovative ideas to fruition. My technical arsenal includes **Python**, **C++**, **SQL**, **React.js**, **Streamlit**, **pandas**, **numpy**, **matplotlib**, **Plotly**, and **seaborn**, to name a few. 
    
    My portfolio is a treasure trove of diverse projects, from building pathfinder visualizers and Gemini API clones to developing interactive data visualization tools. Whether it's crafting complex algorithms or designing captivating user interfaces, I'm your go-to person for all things development. When I'm not coding, you can find me exploring the latest tech trends or honing my problem-solving skills. I'm always eager to learn and grow, and I'm excited about where my passion for Data Science and development will take me next. If you're looking to bring your ideas to life, let's collaborate and create something extraordinary together!

    📂 Here, you will find a collection of my **projects**, **achievements**, and **insights** into the world of data science and artificial intelligence. 🌐 Explore and feel free to reach out if you have any questions or collaboration ideas!

    📫 Connect with me on [LinkedIn](https://www.linkedin.com/in/raj-tripathi-6208ab241/) || [GitHub](https://github.com/RAJTripathi3030) ||  [Email](mailto:t.raj.ripathi@gmail.com)
    """)
st.write("Here's my resume:")
with open("Raj Tripathi Resume.pdf", "rb") as file:
        btn = st.download_button(
            label="Download Resume",
            data=file,
            file_name="Raj Tripathi Resume.pdf",
            mime="application/pdf"
        )
lottie_url = "https://lottie.host/f56472c3-2021-4eb8-92e2-39ea06345f42/1L7J5mRwno.json"
lottie_animation = load_lottieurl(lottie_url)
if lottie_animation:
        st_lottie(lottie_animation, speed=1, height=300, key="home")
else:
        st.error("Failed to load Lottie animation.")
        
        