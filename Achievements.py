import streamlit as st
import requests
from streamlit_lottie import st_lottie

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Page Configuration
st.set_page_config(page_title="My Projects & Achievements", page_icon="🏆", layout="wide")

# Load Lottie Animation
lottie_url = "https://lottie.host/a7990eb1-5152-4cd1-a7fd-e0c592683b97/KOvlwaJ4uL.json"
lottie_animation = load_lottieurl(lottie_url)

# Custom CSS for animations and cards
st.markdown("""
    <style>
    .card {
        background-color: #fdfdfd;
        border-radius: 15px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 2px 4px 10px rgba(0,0,0,0.05);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        animation: fadeInUp 1s ease-in-out;
        color: #333333;
    }
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 4px 8px 20px rgba(0,0,0,0.1);
    }
    .card h4 {
        margin-bottom: 10px;
        font-size: 20px;
        color: #111111;
        font-weight: 700;
    }
    .card p {
        margin: 0;
        color: #333333;
        font-size: 16px;
    }
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 style='text-align: center; font-size: 48px;'>🏆 My Projects & Achievements</h1><hr>", unsafe_allow_html=True)

# Layout
col1, col2 = st.columns([2, 1])

with col1:
    achievements = [
        {
            "icon": "🔐",
            "title": "Migrated 25+ Applications to Teleport SSO",
            "desc": "Enhanced authentication and access control by implementing RBAC across environments."
        },
        {
            "icon": "🛠️",
            "title": "Built Scalable Dev Environment",
            "desc": "Used Terraform, Jenkins, Ansible, and Docker on AWS. Cut provisioning time by 50%."
        },
        {
            "icon": "🔍",
            "title": "Automated PII Detection with AWS Macie",
            "desc": "Implemented alerting and JIRA flows to improve logging security posture."
        },
        {
            "icon": "⚙️",
            "title": "Optimized CI/CD Pipelines",
            "desc": "Integrated Jenkins, SonarQube, and Nexus. Reduced deployment from 60 to 25 minutes."
        },
        {
            "icon": "🧱",
            "title": "Infra for Data Engineering Platform",
            "desc": "Deployed Redis + EC2 Microservices to support scalable feed optimization."
        },
        {
            "icon": "📊",
            "title": "Zero-Downtime Grafana Upgrade",
            "desc": "Used rolling deployments to keep production monitoring uninterrupted."
        },
        {
            "icon": "📡",
            "title": "Upgraded Teleport Agent Across 1,500+ Servers",
            "desc": "Built Ansible + Jenkins pipelines for non-prod to prod rollout with validation."
        }
    ]

    for ach in achievements:
        st.markdown(f"""
        <div class="card">
            <h4>{ach['icon']} <b>{ach['title']}</b></h4>
            <p>{ach['desc']}</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
        <div style='text-align: center; margin-top: 30px; font-style: italic; color: #4dd0e1;'>
            🚀 Every milestone reflects my passion for automation, reliability, and building systems that scale.
        </div>
    """, unsafe_allow_html=True)

# Lottie Animation
with col2:
    if lottie_animation:
        st_lottie(lottie_animation, speed=1, height=400, key="achievements")
    else:
        st.error("⚠️ Failed to load Lottie animation.")

st.write("---")
st.markdown("""
    <h2 style='text-align: center;'>📚 I Like To Talk About</h2>
""", unsafe_allow_html=True)

topics = [
    "☁️ Cloud Architecture (AWS)",
    "🔐 Infrastructure Security",
    "📦 Kubernetes & Containerization",
    "📈 Observability & Monitoring (Grafana, Prometheus, Datadog)",
    "🚀 CI/CD Pipelines (Jenkins, GitHub Actions)",
    "🛡️ IAM, SSO & Compliance (Teleport, RBAC, Macie)",
    "🧰 Infrastructure as Code (Terraform, Ansible)",
    "🔄 Disaster Recovery & High Availability",
    "📉 Cost Optimization in Cloud",
    "🧪 Automation Testing in DevOps",
    "🔄 GitOps with ArgoCD",
    "🧑‍💻 Site Reliability Engineering (SRE)",
    "📊 Incident Response & Alerting",
    "🔧 Linux Internals & Troubleshooting"
]

cols = st.columns(2)
for i, topic in enumerate(topics):
    with cols[i % 2]:
        st.info(topic)