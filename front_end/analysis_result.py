import streamlit as st
import json
import os
from PIL import Image
from setting import IMAGE_RESOURCE_PATH, THEME_CONFIG

def render_ele():
    st.subheader('Analysis result')
    custom_bg = f"""
    <style>
        .st-emotion-cache-163oi9g {{background-color: {THEME_CONFIG['secondaryBackgroundColor']}; min-height: 250px;}}
    </style>
    """
    st.markdown(custom_bg, unsafe_allow_html=True)
    with st.container(border=True):
        with st.chat_message(name="ai", avatar=Image.open(os.path.join(IMAGE_RESOURCE_PATH, 'chatbot.png'))):
            st.write("Hello I am a medical assistant tasked with evaluating prescription. Here is my analysis result of the presciption you provided.")
            with open("tempDir/text_349.json", 'r', encoding='utf-8') as f:
                analysis = json.load(f)
            st.markdown(analysis['output'], unsafe_allow_html=True)
            text_1 = 'Inappropriate'
            text_2 = 'Appropriate'
            s1 = f"<p style='font-size:18px;'>Conclusion:   <span style='color:red;'> {text_1}</span></p>"
            s2 = f"<p style='font-size:18px;'>Conclusion:   <span style='color:#1ae5ad;'>   {text_2}</span></p>"
            st.markdown(s1, unsafe_allow_html=True)