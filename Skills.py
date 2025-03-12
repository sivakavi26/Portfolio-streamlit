import streamlit as st
import requests 
from streamlit_lottie import st_lottie
import time

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Page Configuration
st.set_page_config(page_title="My Skills", page_icon="🚀", layout="wide")

# Animated Title
st.markdown("""
    <h1 style='text-align: center; font-size: 48px;'>🚀 My Skills</h1>
    <hr style='border: 2px solid #ddd;'>
""", unsafe_allow_html=True)

# Load Lottie Animation
lottie_url = "https://lottie.host/e0f72cc9-db24-4eac-a85e-19bb821629f9/mumuEVoTHL.json"
lottie_animation = load_lottieurl(lottie_url)

# Columns for Layout
col1, col2 = st.columns([2, 1])

# Skills Section
with col1:
    skills = {
        "🖥️ Programming Languages": ["Python", "C++", "SQL", "CSS", "HTML", "JavaScript"],
        "📚 Libraries": ["Pandas", "NumPy", "Matplotlib", "Plotly", "Seaborn"],
        "🚀 Frameworks": ["Streamlit", "React.js", "Bootstrap CSS", "LangChain"],
        "🛠️ Tools & Platforms": [
            "Git", "Jupyter Notebook", "VS Code", "Ollama", "Tableau", 
            "Power BI", "Google Colab", "Anaconda"
        ],
        "🗄️ Databases": ["MySQL", "Vector Databases"],
        "🤖 Machine Learning": ["Scikit-learn", "Machine Learning Algorithms"],
        "🧠 Deep Learning": ["TensorFlow", "Keras", "OpenCV", "NLTK", "Spacy", "PyTorch", "Transformers"],
        "💡 Soft Skills": ["Teamwork", "Communication", "Problem-Solving", "Time Management", "Adaptability"],
        "🎯 Others": ["Data Structures & Algorithms", "Computer Vision", "Natural Language Processing"]
    }
    
    for category, items in skills.items():
        with st.expander(category):
            st.success(", ".join(items))  # Enhanced styling with success box

# Animated Lottie Animation on Right
with col2:
    if lottie_animation:
        st_lottie(lottie_animation, speed=1, height=300, key="skills")
    else:
        st.error("Failed to load Lottie animation.")

# Footer Animation
st.markdown("""
    <style>
    @keyframes fadeIn {
        from {opacity: 0;}
        to {opacity: 1;}
    }
    .footer {
        animation: fadeIn 2s ease-in;
        text-align: center;
        font-size: 18px;
        margin-top: 20px;
        color: #555;
    }
    </style>
""", unsafe_allow_html=True)