import os
import base64
import streamlit as st
import streamlit.components.v1 as components
from PIL import Image

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

@st.cache_resource(show_spinner=False)
def load_image(image_file):
    img = Image.open(image_file)
    return img

def save_image(uploaded_image):
    if uploaded_image is not None:
        file_details = {"FileName":uploaded_image.name,"FileType":uploaded_image.type}
        st.write(file_details['FileName'])
        img = load_image(uploaded_image)
        st.image(img, use_column_width=True)
        with open(os.path.join("tempDir",uploaded_image.name),"wb") as f: 
            f.write(uploaded_image.getbuffer())         
        # st.success("Saved File")
        st.success('File uploaded!', icon="✅")

# ------------------ Streamlit UI Configuration ------------------ #

st.set_page_config(
    page_title="Rx Strategist",
    page_icon=":shield:",
    layout="wide",
    #"auto" or "expanded" or "collapsed"
    initial_sidebar_state="collapsed",
)

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

    #define the upload widget
    uploaded_file = st.file_uploader("Upload image of prescription", type=["jpg", "jpeg", "png"])
    save_image(uploaded_file)

    # Use text_area with the session state value and update the session state on change
    # app_input = st.text_area(
    #     label="Describe the prescription to be evaluate",
    #     value=st.session_state['app_input'],
    #     key="app_input_widget",
    #     help="Provide additional detailes of the prescription, including the purpose of the drugs, how it is related to the patient, and any other relevant information.",
    # )

    # # Update session state only if the text area content has changed
    # if app_input != st.session_state['app_input']:
    #     st.session_state['app_input'] = app_input

    # else:
    #     # For other model providers or models, use the get_input() function
    #     app_input = get_input()
    #     # Update session state
    #     st.session_state['app_input'] = app_input

# Ensure app_input is always up to date in the session state
# app_input = st.session_state['app_input']

with col2:

    custom_bg = """
    <style>
    .st-emotion-cache-16h9saz {background-color: #0F67B1; height: 250px;}
    </style>
    """
    st.markdown(custom_bg, unsafe_allow_html=True)
    with st.container(border=True):
        with st.chat_message(name="ai", avatar=Image.open('assistance_avatar.png')):
            st.write("Hello I am a medical assistant tasked with evaluating prescription. How can I help you today.")
            text_1 = 'Inappropriate'
            text_2 = 'Appropriate'
            s1 = f"<p style='font-size:25px; color:red;'>{text_1}</p>"
            s2 = f"<p style='font-size:25px; color:#1ae5ad;'>{text_2}</p>"
            st.markdown(s1, unsafe_allow_html=True)
            st.markdown(s2, unsafe_allow_html=True)



