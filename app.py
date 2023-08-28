import streamlit as st
import requests
import json
from PyPDF2 import PdfReader
import pandas as pd
import base64
import io


# Initialize session state variables
if "result" not in st.session_state:
    st.session_state.result = ""

# Claude functions
def create_text(prompt):
    api_url = "https://api.anthropic.com/v1/complete"
    headers = {
        "Content-Type": "application/json",
        "X-API-Key": st.secrets["API_KEY"]  # Use the API key from Streamlit's secrets
    }

    # Prepare the prompt for Claude
    conversation = f"Human: {prompt}\n\nAssistant:"

    # Define the body of the request
    body = {
        "prompt": conversation,
        "model": "claude-2.0",
        "temperature": 0,
        "max_tokens_to_sample": 10000,
        "stop_sequences": ["\n\nHuman:"]
    }

    # Make a POST request to the Claude API
    try:
        response = requests.post(api_url, headers=headers, data=json.dumps(body))
        response.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        st.error(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        st.error(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        st.error(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        st.error(f"Something went wrong: {err}")
    except Exception as e:
        st.error(f"Unexpected error: {e}")

    # Extract Claude's response from the JSON response
    result = response.json()

    # Return Claude's response as a string
    return result['completion']

# Function to create the prompt for the decks generation
def prompt_compliance(text_file):
    prompts = f'''Role: You are a top data analyst extract and present information from {text_file}. Do the following tasks and answer always in Spanish.
    Task 1: Identify the "Razón Social"
    Task 2: Identify the "Nit"
    Task 3: Identify the "Domicilio principal"
    Task 4: Identify the "Matrícula No."
    Task 5: Identify the "Teléfono comercial 1:"
    Task 6: Identify the "Teléfono comercial 2:" 
    Task 7: Identify the "Página web:"
    Task 8: Identify the "Correo electrónico:"
    Task 9: Identify the "OBJETO SOCIAL:"
    Task 10: Identify the "REPRESENTANTE LEGAL PRINCIPAL"
    Task 11: Identify the "REPRESENTANTE LEGAL SUPLENTE"
    Task 12: Identify the "Actividad principal código CIIU:"
    Task 13: Identify the "Actividad secundaria código CIIU:"
    '''


    return prompts

def read_pdf(file):
    pdf = PdfReader(file)
    text = ''
    for page in pdf.pages:
        text += page.extract_text()
    return text

st.title('Compliance Prueba de concepto extraer info')

uploaded_files = st.file_uploader("Choose PDF files", type="pdf", accept_multiple_files=True)

df_all_text = pd.DataFrame()

for file in uploaded_files:
    text = read_pdf(file)
    all_text_df = pd.DataFrame({'All Text': [text]})
    df_all_text = pd.concat([df_all_text, all_text_df], ignore_index=True)

if st.button('Extraer'):
    with st.spinner('Writing...'):
        for index, row in df_all_text.iterrows():
            st.session_state.prompts = prompt_compliance(row['All Text'])
            st.session_state.result = create_text(st.session_state.prompts)
            st.write(st.session_state.result)



def download_link(object_to_download, download_filename, download_link_text):
    """
    Generates a link to download the given object_to_download.
    """
    if isinstance(object_to_download, pd.DataFrame):
        output = io.BytesIO()
        object_to_download.to_excel(output, index=False)
        object_to_download = output.getvalue()
        
    # some strings <-> bytes conversions necessary here
    b64 = base64.b64encode(object_to_download).decode()

    return f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64}" download="{download_filename}">{download_link_text}</a>'

    
    # Adding the download link here
if not df_all_text.empty:  # Making sure the DataFrame isn't empty
    st.markdown(download_link(df_all_text, 'result.xlsx', 'Click here to download the results in .xlsx format'), unsafe_allow_html=True)