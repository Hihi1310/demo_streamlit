import toml
import os

IMAGE_RESOURCE_PATH = "./resource/png"
UPLOAD_FOLDER = "./tempDir"
# All config file for streamlit is put here
STREAMLIT_CONFIG_PATH = './.streamlit'

# Load theme config
with open(os.path.join(STREAMLIT_CONFIG_PATH, 'config.toml'), 'r') as f: 
    THEME_CONFIG = toml.load(f)['theme']

