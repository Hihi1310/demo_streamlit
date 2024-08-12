# Base package
import os
import base64
import json
import time
import streamlit as st
from PIL import Image

# Custom package
import front_end as fe

# ------------------ Helper Functions ------------------ #


# Function to get user input for the application description and key details
def get_input():
       input_text = st.text_area(
           label="Describe the application to be modelled",
           placeholder="Enter your application details...",
           height=150,
           key="app_desc",
           help="Please provide a detailed description of the application, including the purpose of the application, the technologies used, and any other relevant information.",
       )

       st.session_state['app_input'] = input_text

       return input_text

@st.cache_resource(show_spinner=False)
def query_response(prescription: str):
    # args = parse_arguments()

    # Start the timer``
    start_time = time.time()  

    # Process the query
    # response = main(prescription, args)
    response = 'hello how are you'
    # End the timer and calculate the time taken
    end_time = time.time()
    time_excecution = end_time - start_time 

    timed_response = format_response(response, time_excecution)
    st.info(timed_response)

# ------------------ Streamlit UI Configuration ------------------ #

st.set_page_config(
    page_title="Rx Strategist",
    page_icon=":shield:",
    layout="wide",
    #"auto" or "expanded" or "collapsed"
    initial_sidebar_state="collapsed",
)

custom_font = """
    <link href='https://fonts.googleapis.com/css?family=Poppins' rel='stylesheet'>
    <style>
    body, h1, h2, h3, p {
        font-family: 'Poppins' !important; font-size: 20px;
    }
    </style>
    """
st.markdown(custom_font, unsafe_allow_html=True)


# ------------------ Sidebar ------------------ #

# st.sidebar.image("logo.png")

# Add instructions on how to use the app to the sidebar
st.sidebar.header("How to use Rx Strategist")

with st.sidebar:
    st.markdown(
        "Welcome to STRIDE GPT, an AI-powered tool designed to help teams produce better threat models for their applications."
    )
    st.markdown(
        "Threat modelling is a key activity in the software development lifecycle, but is often overlooked or poorly executed. STRIDE GPT aims to help teams produce more comprehensive threat models by leveraging the power of Large Language Models (LLMs) to generate a threat list, attack tree and/or mitigating controls for an application based on the details provided."
    )
    st.markdown("Created by [Matt Adams](https://www.linkedin.com/in/matthewrwadams/).")
    # Add "Star on GitHub" link to the sidebar
    st.sidebar.markdown(
        "⭐ Star on GitHub: [![Star on GitHub](https://img.shields.io/github/stars/mrwadams/stride-gpt?style=social)](https://github.com/mrwadams/stride-gpt)"
    )
    st.markdown("""---""")


# Add "Example Application Description" section to the sidebar
st.sidebar.header("Example Application Description")

with st.sidebar:
    st.markdown(
        "Below is an example application description that you can use to test STRIDE GPT:"
    )
    st.markdown(
        "> A web application that allows users to create, store, and share personal notes. The application is built using the React frontend framework and a Node.js backend with a MongoDB database. Users can sign up for an account and log in using OAuth2 with Google or Facebook. The notes are encrypted at rest and are only accessible by the user who created them. The application also supports real-time collaboration on notes with other users."
    )
    st.markdown("""---""")

# Add "FAQs" section to the sidebar
st.sidebar.header("FAQs")

with st.sidebar:
    st.markdown(
        """
    ### **What is STRIDE?**
    STRIDE is a threat modeling methodology that helps to identify and categorise potential security risks in software applications. It stands for **S**poofing, **T**ampering, **R**epudiation, **I**nformation Disclosure, **D**enial of Service, and **E**levation of Privilege.
    """
    )
    st.markdown(
        """
    ### **How does STRIDE GPT work?**
    When you enter an application description and other relevant details, the tool will use a GPT model to generate a threat model for your application. The model uses the application description and details to generate a list of potential threats and then categorises each threat according to the STRIDE methodology.
    """
    )
    st.markdown(
        """
    ### **Do you store the application details provided?**
    No, STRIDE GPT does not store your application description or other details. All entered data is deleted after you close the browser tab.
    """
    )
    st.markdown(
        """
    ### **Why does it take so long to generate a threat model?**
    If you are using a free OpenAI API key, it will take a while to generate a threat model. This is because the free API key has strict rate limits. To speed up the process, you can use a paid API key.
    """
    )
    st.markdown(
        """
    ### **Are the threat models 100% accurate?**
    No, the threat models are not 100% accurate. STRIDE GPT uses GPT Large Language Models (LLMs) to generate its output. The GPT models are powerful, but they sometimes makes mistakes and are prone to 'hallucinations' (generating irrelevant or inaccurate content). Please use the output only as a starting point for identifying and addressing potential security risks in your applications.
    """
    )
    st.markdown(
        """
    ### **How can I improve the accuracy of the threat models?**
    You can improve the accuracy of the threat models by providing a detailed description of the application and selecting the correct application type, authentication methods, and other relevant details. The more information you provide, the more accurate the threat models will be.
    """
    )


# ------------------ Main App UI ------------------ #

st.header('Rx Strategist')

st.markdown("""
An app that helps identify and evaluate potential illogical information in prescription. It provides a systematic approach to 
understanding possible flaws when using prescribed medications. 
""")

st.divider()

# Two column layout for the main app content
col1, divider, col2 = st.columns([2, 0.2, 2])

# Initialize app_input in the session state if it doesn't exist
if 'app_input' not in st.session_state:
    st.session_state['app_input'] = ''

# the right side of the page
with col1:
    fe.upload_image.render_ele()
# the left side of the page
with col2:
    fe.analysis_result.render_ele()
            





