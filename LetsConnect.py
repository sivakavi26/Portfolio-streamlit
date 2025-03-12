import streamlit as st
import requests
from streamlit_lottie import st_lottie

# Function to load Lottie animation from a URL
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load a Lottie animation for the contact page
lottie_contact = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_vnikrcia.json")

# Custom CSS only for the submit button (contact-form container block removed)
st.markdown(
    """
    <style>
    .custom-button {
      background-color: #4CAF50;
      color: white;
      border: none;
      padding: 10px 20px;
      border-radius: 5px;
      cursor: pointer;
      font-size: 16px;
    }
    .custom-button:hover {
      background-color: #45a049;
    }
    </style>
    """, unsafe_allow_html=True)

# Page title and introduction
st.title("Contact Me")
st.write("Fill out the form below to get in touch.")

# Divide the page into two columns for balanced layout
col1, col2 = st.columns(2)

with col1:
    if lottie_contact:
        st_lottie(lottie_contact, height=300, key="contact")
    else:
        st.write("Animation could not be loaded.")

with col2:
    # Create a contact form using Streamlit's form component without extra HTML block
    with st.form(key='contact_form'):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        submit_button = st.form_submit_button("Send Message")
        
        if submit_button:
            st.success("Thank you for your message! We will get back to you soon.")
