import streamlit as st
import requests 
from streamlit_lottie import st_lottie
from PIL import Image

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Page Config
st.set_page_config(page_title="Sivakavi Portfolio", page_icon="👨‍💻", layout="wide")

# Load profile image
profile_image = Image.open("profile.png")  # Ensure it's a transparent background PNG

# Custom CSS
st.markdown("""
    <style>
        .profile-card {
            background-color: #1f2937;
            padding: 30px;
            border-radius: 20px;
            display: flex;
            align-items: center;
            box-shadow: 0 4px 10px rgba(0,0,0,0.3);
        }
        .profile-img {
            width: 200px;
            height: 200px;
            border-radius: 50%;
            object-fit: flex;
            transform: scale(1.2);
            margin-left: -10px;  /* Optional: re-center after zoom */
        }
        .profile-text {
            color: white;
            margin-left: 30px;
        }
    </style>
""", unsafe_allow_html=True)

# HTML/CSS wrapper for image
profile_html = """
    <div class="profile-card">
        <img src="data:image/png;base64,{}" class="profile-img"/>
        <div class="profile-text">
            <h1>👋 Hi, I'm <span style="color:#38bdf8;">Sivakavi Shanmugam</span></h1>
            <h3>DevOps Engineer | AWS Certified Solutions Architect</h3>
            <p>
                I engineer resilient cloud systems, automate pipelines, and lead DevOps initiatives.<br><br>
                With <b>4 years of IT experience</b> — including <b>2 years in DevOps/SRE</b> — I bridge the gap between development and operations.<br>
                I'm passionate about <b>automation, infrastructure optimization</b>, and building scalable, secure cloud environments.
                I engineer resilient cloud systems, automate software delivery pipelines, and lead DevOps initiatives end to end.
        </div>
    </div>
"""

# Convert image to base64
import base64
from io import BytesIO

buffered = BytesIO()
profile_image.save(buffered, format="PNG")
img_b64 = base64.b64encode(buffered.getvalue()).decode()

# Render image + bio in a styled card
st.markdown(profile_html.format(img_b64), unsafe_allow_html=True)

st.markdown("""

    ### My Toolkit includes:
    - ☁️ **AWS** (certified)
    - 🐳 **Docker**, ☸️ **Kubernetes**
    - ⚙️ **Terraform**, 🧰 **Ansible**
    - 🚀 **CI/CD tools** like GitHub Actions, Jenkins
    - 🔐 Security-first approach to **cloud & pipeline hardening**
    - 📊 **Monitoring & observability** with tools like Datadog, Prometheus, Grafana, and CloudWatch
    
    I've led successful **cloud migrations**, automated **end-to-end deployment pipelines**, and continuously improved **system reliability and performance**.
    
    ---
    
    ### 📂 In this portfolio:
    - Explore my **DevOps projects**
    - Dive into my **automation scripts**
    - Learn from my **cloud architecture designs**
    - Reach out for **collaboration or consulting**
    
    ---
    
    If you're looking for someone who thrives at the intersection of **cloud, code, and security**, let's connect and create something impactful together!
    
    ---
    """)

# ----- Contact & Links -----
st.markdown("## 📫 Connect with Me")

col1, col2= st.columns(2)
with col1:
    st.link_button("🔗 GitHub", "https://github.com/sivakavi26")
with col2:
    st.link_button("💼 LinkedIn", "https://www.linkedin.com/in/sivakavishanmugam")

st.write("Here's my resume:")
with open("Sivakavi's Resume.pdf", "rb") as file:
        btn = st.download_button(
            label="Download Resume",
            data=file,
            file_name="Sivakavi's Resume.pdf",
            mime="application/pdf"
        )
lottie_url = "https://lottie.host/f56472c3-2021-4eb8-92e2-39ea06345f42/1L7J5mRwno.json"
lottie_animation = load_lottieurl(lottie_url)
if lottie_animation:
        st_lottie(lottie_animation, speed=1, height=300, key="home")
else:
        st.error("Failed to load Lottie animation.")
        
        