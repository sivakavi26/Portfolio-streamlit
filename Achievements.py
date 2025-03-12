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
st.set_page_config(page_title="My Achievements", page_icon="🏆", layout="wide")

# Animated Title
st.markdown("""
    <h1 style='text-align: center; font-size: 48px;'>🏆 My Achievements</h1>
    <hr style='border: 2px solid #ddd;'>
""", unsafe_allow_html=True)

# Load Lottie Animation
lottie_url = "https://lottie.host/a7990eb1-5152-4cd1-a7fd-e0c592683b97/KOvlwaJ4uL.json"
lottie_animation = load_lottieurl(lottie_url)

# Columns for Layout
col1, col2 = st.columns([2, 1])

# Achievements Section
with col1:
    achievements = [
        "🧠 Solved 300+ questions on LeetCode. I'm on a roll!",
        "🌟 Topped the DevStar Bootcamp. Yes, I did that!",
        "⚽ Winner of the Intra-School Football Championship. Go team!"
    ]
    
    for achievement in achievements:
        st.success(achievement)  # Enhanced styling with success box
    
    st.markdown("""
        **I believe that every achievement, big or small, is a stepping stone towards success.** 
        I am always eager to learn and grow, and I am excited to see what the future holds for me. 🚀
    """)

# Animated Lottie Animation on Right
with col2:
    if lottie_animation:
        st_lottie(lottie_animation, speed=1, height=300, key="achievements")
    else:
        st.error("Failed to load Lottie animation.")

# Topics of Interest Section
st.write("---")
st.markdown("""
    <h2 style='text-align: center;'>📚 I Like To Talk About</h2>
""", unsafe_allow_html=True)

topics = [
    "📊 Data Science", "🤖 Machine Learning", "🧠 Deep Learning", "🚀 Artificial Intelligence",
    "🖼️ Computer Vision", "📜 Natural Language Processing", "📌 Data Structures & Algorithms", "💡 Self-Improvement"
]

cols = st.columns(2)
for i, topic in enumerate(topics):
    with cols[i % 2]:
        st.info(topic)  # Enhanced styling with info box

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