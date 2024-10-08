import streamlit as st
import os
from setting import UPLOAD_FOLDER, THEME_CONFIG
from PIL import Image, ImageFile

# ------------------ Private Functions ------------------ #


@st.cache_resource(show_spinner=False)
def _load_image(image_file: str) -> None:
    img = Image.open(image_file)
    return img

def _render_image(img: ImageFile) -> None:
    st.image(img, width=400)

def _save_image() -> None:
    uploaded_image = st.session_state['uploaded_image']
    if uploaded_image is not None:
        # show file details
        # file_details = {"FileName":uploaded_image.name,"FileType":uploaded_image.type}
        # st.write(file_details['FileName'])

        # Load image to PIL ImageFile class
        img = _load_image(uploaded_image)
        
        # Save file and show image
        with open(os.path.join(UPLOAD_FOLDER, uploaded_image.name),"wb") as f: 
            f.write(uploaded_image.getbuffer())
            _render_image(img)         
        st.success('File uploaded!', icon="✅")

# ------------------ Public Functions ------------------ #

def render_ele():
    st.subheader('Upload prescription')
    #define the upload widget
    custom_css = f"""
    <style>
        .eyeqlp53 {{
            color: {THEME_CONFIG['textColor']};
        }}
        .st-emotion-cache-n3wj7a{{
            color: #FFFFFF
        }}
    </style>
    """
    
    st.markdown(custom_css, unsafe_allow_html=True)
    upload_file = st.file_uploader(label="Upload image of prescription",
                    key='uploaded_image',
                    type=["jpg", "jpeg", "png"])
    
    _save_image()