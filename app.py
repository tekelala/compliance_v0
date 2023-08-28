import streamlit as st
import requests
import json
from PyPDF2 import PdfReader
import pandas as pd
import base64
import io
from functions import prompt_compliance
import re  # Required for the regex operations in the parsing function

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

def read_pdf(file):
    pdf = PdfReader(file)
    text = ''
    for page in pdf.pages:
        text += page.extract_text()
    return text

# Function to parse text to Excel (from the previous code)
def parse_text_to_excel(text):
    # Define regular expressions for each field
    patterns = {
        "Razón Social": r"Razón Social:\s*(.*?)\s*(?=(Nit:|$))",
        "Nit": r"Nit:\s*(.*?)\s*(?=(Domicilio principal:|$))",
        "Domicilio principal": r"Domicilio principal:\s*(.*?)\s*(?=(Matrícula No\.:|$))",
        "Matrícula No.": r"Matrícula No\.:\s*(.*?)\s*(?=(Teléfono comercial 1:|$))",
        "Teléfono comercial 1": r"Teléfono comercial 1:\s*(.*?)\s*(?=(Teléfono comercial 2:|$))",
        "Teléfono comercial 2": r"Teléfono comercial 2:\s*(.*?)\s*(?=(Página web:|$))",
        "Página web": r"Página web:\s*(.*?)\s*(?=(Correo electrónico:|$))",
        "Correo electrónico": r"Correo electrónico:\s*(.*?)\s*(?=(OBJETO SOCIAL:|$))",
        "OBJETO SOCIAL": r"OBJETO SOCIAL:\s*(.*?)\s*(?=(REPRESENTANTE LEGAL PRINCIPAL:|$))",
        "REPRESENTANTE LEGAL PRINCIPAL": r"REPRESENTANTE LEGAL PRINCIPAL:\s*(.*?)\s*(?=(REPRESENTANTE LEGAL SUPLENTE:|$))",
        "REPRESENTANTE LEGAL SUPLENTE": r"REPRESENTANTE LEGAL SUPLENTE:\s*(.*?)\s*(?=(Actividad principal código CIIU:|$))",
        "Actividad principal código CIIU": r"Actividad principal código CIIU:\s*(.*?)\s*(?=(Actividad secundaria código CIIU:|$))",
        "Actividad secundaria código CIIU": r"Actividad secundaria código CIIU:\s*(.*?)\s*(?=$)"
    }
    
    # Extract information using regex
    data = {}
    for key, pattern in patterns.items():
        match = re.search(pattern, text, re.DOTALL)  # re.DOTALL allows . to match newlines as well
        data[key] = match.group(1).strip() if match else None
    
    # Convert dictionary to DataFrame
    df = pd.DataFrame([data])
    
    return df  # Return DataFrame instead of saving to Excel in this function

st.title('Compliance Prueba de concepto extraer info')

uploaded_files = st.file_uploader("Choose PDF files", type="pdf", accept_multiple_files=True)

df_all_text = pd.DataFrame()

for file in uploaded_files:
    text = read_pdf(file)
    # Parse the text using the function
    parsed_df = parse_text_to_excel(text)
    df_all_text = pd.concat([df_all_text, parsed_df], ignore_index=True)

df_extracted_data = pd.DataFrame()  # Create an empty DataFrame to store parsed data after pressing 'Extraer'

if st.button('Extraer'):
    with st.spinner('Writing...'):
        for index, row in df_all_text.iterrows():
            # Assuming you want to process each row with the prompt_compliance and create_text functions
            # Convert the row (which is a Series) to a string representation
            row_text = row.to_string()
            st.session_state.prompts = prompt_compliance(row_text)
            st.session_state.result = create_text(st.session_state.prompts)
            
            # Display the result
            st.write(st.session_state.result)

# Adjust the download link to use df_extracted_data
if not df_extracted_data.empty:
    st.markdown(download_link(df_extracted_data, 'result.xlsx', 'Click here to download the results in .xlsx format'), unsafe_allow_html=True)
