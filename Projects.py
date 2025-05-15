import streamlit as st
import requests 
from streamlit_lottie import st_lottie


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


st.title('Personal Projects')
# Project 1 Container
with st.container():
        img_col, text_col = st.columns((1, 2))
        with img_col:
            lottie_url = "https://lottie.host/a2013158-113e-4fdc-806a-4cab66f3a7df/vj8L5jvQqL.json"
            lottie_animation = load_lottieurl(lottie_url)
            if lottie_animation:
                st_lottie(lottie_animation, speed=1, height=300, key="project1")
            else:
                st.error("Failed to load Lottie animation.")
        with text_col:
            # Enter Desctipion
            st.write("### E-Commerce Website")
            st.write("""
                    - Developed a Basic Ecommerce Website using Django framework.
                    - Added checkout and payment feature to the website.
                    - Included Admin page setup
                    """)
            if st.button("Know More ➡️"):
                with st.expander("### Technologies Used", expanded=False):
                    col1, col2 = st.columns(2)
                    with col1:
                        st.write("- Python")
                        st.write("- Django")
                    with col2:
                        st.write("- HTML")
                        st.write("- Bootstrap CSS")
                        st.write("- Javascript")
                        
                with st.expander("### 🔗Project Link", expanded = False):
                    st.write("[Ecommerce site Repo ](https://github.com/sivakavi26/My-first-project.git)")
    
# Project 2 Container
with st.container():
        st.write("---")
        st.write("##")
        img_col, text_col = st.columns((1, 2))
        with img_col:
            lottie_url = "https://lottie.host/2d4afafd-bda4-406b-b341-ab96aaf0a9cd/0BwBa9R2WA.json"
            lottie_animation = load_lottieurl(lottie_url)
            if lottie_animation:
                st_lottie(lottie_animation, speed=1, height=300, key="project2")
            else:
                st.error("Failed to load Lottie animation.")
        with text_col:
            st.write("### My Portfolio Website")
            st.write("""
                    - Developed portfolio website with python streamlit framework.
                    - The website is hosted in the streamlit.io platform.
                    """)
            if st.button("Know More 🚀"):
                with st.expander("### Technologies Used", expanded=False):
                    col1, col2 = st.columns(2)
                    with col1:
                        st.write("- Streamlit")
                    with col2:
                        st.write("- HTML")
                        st.write("- CSS")
                        st.write("- JavaScript")
                
                with st.expander("### 🔗Project Link", expanded = False):
                    st.write("[My Portfolio Repo]()")

st.title('Certifications')
# Enter Desctipion
st.write("### AWS Certified Solutions Architect – Associate")
certificate_url1 = "https://www.credly.com/badges/b3e5e035-8f90-4789-a794-72a53d848254/public_url"
st.markdown(f"[🔗 View Certificate]({certificate_url1})", unsafe_allow_html=True)
certificate_url2 = "https://www.udemy.com/certificate/UC-362cdac7-7427-4787-9033-89a695d3309a/"
st.write("### DevOps Beginners to Advanced | Decoding DevOps with Projects - Udemy")
st.markdown(f"[🔗 View Certificate]({certificate_url2})", unsafe_allow_html=True)
certificate_url3 = "https://www.udemy.com/certificate/UC-a4c1cd73-1950-40d8-93f5-b999f5ac6bf7/"
st.write("### Python and Django Full Stack Web Developer Bootcamp - Udemy")
st.markdown(f"[🔗 View Certificate]({certificate_url3})",unsafe_allow_html=True)




