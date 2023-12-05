import streamlit as st

st.set_page_config(
    page_title="App Streamlit",
    page_icon="👋",
)

st.write("# :orange[Welcome to My App Streamlit!] 🧡")
page_bg_img = '''
    <style>
    .stApp {
        background: url("https://cutewallpaper.org/21x/2olaxzatm/25-Awesome-Web-Background-Animation-Effects-Css-animation-.jpg");
        background-size: cover;
    }
    </style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)
st.markdown(
    """
    Streamlit is an open-source framework that lets you deploy not just a machine-learning model but any Python app in minutes. It also lets us manage and share our app with others.
"""
)
