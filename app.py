# Base package
import os
import base64
import json
import time
import streamlit as st
from PIL import Image

# Custom package
import front_end as fe
from setting import THEME_CONFIG, IMAGE_RESOURCE_PATH

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

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    body {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)



# ------------------ Streamlit UI Configuration ------------------ #

st.set_page_config(
    page_title="Rx Strategist",
    page_icon=":shield:",
    layout="wide",
    #"auto" or "expanded" or "collapsed"
    initial_sidebar_state="collapsed",
)

# get base64 decode result of file path
bin_str = get_base64(os.path.join(IMAGE_RESOURCE_PATH, 'background.png'))

custom_css = """
    <link href='https://fonts.googleapis.com/css?family=Poppins' rel='stylesheet'>
    <style>
        .stApp {
            background-image: url("data:image/png;base64,%s");
            background-size: cover;
        }

        p, ul, span {
            font-family: 'Poppins' !important;
            font-size: 17px;
        }

        h2, h3 {
            font-family: 'Poppins' !important;
            color: #FFFFFF;
            font-size: 28px;
            font-weight: bolder;
        }

        h1 {
            font-family: 'Poppins' !important;
            color: #FFFFFF;
            font-size: 32px;
            font-weight: bolder;
        }
        
        [data-testid="stHeader"]{
            visibility: hidden;
        }
    </style>
    """ % bin_str
st.markdown(custom_css, unsafe_allow_html=True)


# ------------------ Sidebar ------------------ #

fe.side_bar.render_ele()

# ------------------ Main App UI ------------------ #

st.title('Rx Strategist')

st.markdown("""<p style="color: #FFFFFF">
An app that helps identify and evaluate potential illogical information in prescription. It provides a systematic approach to 
understanding possible flaws when using prescribed medications. </p> 
""", unsafe_allow_html=True)

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
            





