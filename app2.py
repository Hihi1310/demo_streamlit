import streamlit as st
import time
# from prescription_verification.main import main
# import argparse


# def parse_arguments():
#     parser = argparse.ArgumentParser(description='Process some integers.')
#     parser.add_argument('--data_drugs_path', type=str, help="Path to the JSON file containing the drugs' information", default="data/processed/drugs_information_processed.json")
#     parser.add_argument('--icd_database_path', type=str, help='Path to the JSON file containing the ICD database', default="data/processed/indication_w_ICD10.json")

#     args = parser.parse_args()
#     return args


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

def format_response(response, time_excecution):
    return f"{response}\n\n(Response Time: {time_excecution:.2f} seconds)"



st.title("Dose Detective App")

with st.form("my_form"):
    text = st.text_area(label="Prescription:")
    submitted = st.form_submit_button("Submit")
    if submitted:
      query_response(text)   

