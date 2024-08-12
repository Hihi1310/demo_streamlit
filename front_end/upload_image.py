import streamlit as st
import os
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
        file_details = {"FileName":uploaded_image.name,"FileType":uploaded_image.type}
        st.write(file_details['FileName'])

        # Load image to PIL ImageFile class
        img = _load_image(uploaded_image)
        
        # Save file and show image
        with open(os.path.join("tempDir",uploaded_image.name),"wb") as f: 
            f.write(uploaded_image.getbuffer())
            _render_image(img)         
        st.success('File uploaded!', icon="✅")

# ------------------ Public Functions ------------------ #

def render_ele():
    st.subheader('Upload prescription')
    #define the upload widget
    upload_file = st.file_uploader(label="Upload image of prescription",
                    key='uploaded_image',
                    type=["jpg", "jpeg", "png"])
    _save_image()