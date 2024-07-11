import streamlit as st

st.set_page_config(
    page_title="Phishing Catcher", 
    page_icon="🛡️",
    layout="wide"
)
# st.title(":shield: :blue[Phishing Catcher]")

st.markdown("""
    <style>
    .title-center {
        text-align: center;
        font-size: 3rem;
        font-weight: bold;
        color: #3498db;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<h1 class="title-center">🛡️ Phishing Catcher</h1>', unsafe_allow_html=True)

st.write("\n")

st.header("Protecting from Phishing",divider="rainbow")
st.write("""
         Phishing attacks trick people into giving away private information by pretending to be trusted websites. 
         Our smart computer program checks web addresses to spot possible phishing threats, helping keep you safe on the internet. 
         Just type a web address, and we'll check if it's real or fake to protect you from online thieves.
""")

st.write("\n")

st.header("How it works?", divider="rainbow")
st.write("""
        Our machine learning model looks closely at web addresses. It checks many parts of the address, like how it's spelled and what it contains. 
        The model compares these details to patterns found in known fake websites. 
        Based on this check, it decides if the address is likely safe or might be dangerous. 
        This helps you know which websites to trust before you click on them.
""")

st.header("What is the approach behind it?", divider="rainbow")
st.write("""
        We use a supervised machine learning classification model to catch phishing websites. 
        This model learns from a large set of known safe and dangerous web addresses. 
        It figures out patterns that separate good sites from bad ones. 
        When you enter a new web address, the model uses what it learned to decide if it looks more like a safe site or a phishing site.
""")