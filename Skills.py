import streamlit as st
import requests
from streamlit_lottie import st_lottie

# Load Lottie animation
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Page config
st.set_page_config(page_title="DevOps Tech Stack", page_icon="🛠️", layout="wide")

# Custom CSS
custom_style = """
    <style>
        .main-heading {
            text-align: center;
            font-size: 48px;
            font-weight: bold;
            color: white;
        }
        .sub-heading {
            text-align: center;
            font-size: 20px;
            color: #a0aec0;
            margin-bottom: 20px;
        }
        .section-title {
            font-size: 22px;
            font-weight: 600;
            color: #2d3748;
            background-color: #f7fafc;
            padding: 10px;
            border-left: 5px solid #319795;
            margin-top: 20px;
            margin-bottom: 10px;
            border-radius: 4px;
        }
        .tool-name {
            font-weight: 500;
            color: #f1f1f1;
            margin-top: 6px;
            display: flex;
            justify-content: space-between;
        }
        .skill-level {
            font-size: 14px;
            color: #a0aec0;
            font-weight: 400;
            margin-left: 10px;
        }
    </style>
"""
st.markdown(custom_style, unsafe_allow_html=True)

# Load animation
lottie_url = "https://lottie.host/e0f72cc9-db24-4eac-a85e-19bb821629f9/mumuEVoTHL.json"
lottie_animation = load_lottieurl(lottie_url)

# Header
st.markdown("<div class='main-heading'>🛠️ DevOps Tech Stack</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-heading'>From foundational tools to advanced systems—here’s my DevOps spectrum.</div>", unsafe_allow_html=True)
st.markdown("<hr style='border: 2px solid #e2e8f0;'>", unsafe_allow_html=True)

# Determine skill level label
def get_skill_level(score):
    if score < 70:
        return "Beginner"
    elif score < 85:
        return "Intermediate"
    else:
        return "Advanced"

# Skills data
detailed_skills = {
    "🧱 IaC & Automation": {
        "Terraform": 90,
        "CloudFormation": 85,
        "Ansible": 88,
        "Bash": 80,
        "Python (Automation)": 80,
        "Groovy": 75
    },
    "⚙️ CI/CD & Version Control": {
        "Jenkins": 90,
        "GitHub Actions": 85,
        "Git": 88,
        "SonarQube": 80,
        "Nexus": 75
    },
    "📊 Monitoring & Logging": {
        "Datadog": 88,
        "Prometheus": 85,
        "Grafana": 85,
        "ElK Stack(Elasticsearch, Logstash & Kibana)": 82
    },
    "🔗 Messaging & Databases": {
        "Kafka": 78,
        "RabbitMQ": 75,
        "MongoDB": 80,
        "Redis": 78,
        "OpenSearch": 72,
        "HAProxy": 70
    },
    "📦 Containers & Orchestration": {
        "Docker": 90,
        "Kubernetes (EKS)": 88,
        "Helm": 85,
        "ArgoCD": 82
    }
}

grouped_skills = {
    "☁️ Cloud & Infrastructure": {
        "AWS (EC2, S3, EKS, Lambda, Route53, VPC, WAF, ECR)": 90,
        "Cloud Networking (VPC, Load Balancers, NAT Gateway)": 85
    },
    "🔐 Security & Compliance": {
        "IAM, AWS Macie, RBAC": 80,
        "Teleport SSO Integration": 75
    },
    "🐧 Linux & OS": {
        "Linux Admin / Scripting": 90,
        "Kernel tuning / Security hardening": 80
    }
}

# Layout
col1, col2 = st.columns([2, 1])

with col1:
    #st.markdown("<div class='section-title'>🔍 Detailed Tools</div>", unsafe_allow_html=True)
    for category, tools in detailed_skills.items():
        st.markdown(f"<div class='section-title'> {category}</div>", unsafe_allow_html=True)
        for tool, score in tools.items():
            level = get_skill_level(score)
            st.markdown(f"<div class='tool-name'>{tool}<span class='skill-level'>{level}</span></div>", unsafe_allow_html=True)
            st.progress(score)

    #st.markdown("<div class='section-title'>🔧 Other Skills</div>", unsafe_allow_html=True)
    for category, items in grouped_skills.items():
        st.markdown(f"<div class='section-title'> {category}</div>", unsafe_allow_html=True)
        for skill, val in items.items():
            level = get_skill_level(val)
            st.markdown(f"<div class='tool-name'>{skill}<span class='skill-level'>{level}</span></div>", unsafe_allow_html=True)
            st.progress(val)

with col2:
    if lottie_animation:
        st_lottie(lottie_animation, height=450, key="skills-lottie")
    else:
        st.error("⚠️ Failed to load animation.")