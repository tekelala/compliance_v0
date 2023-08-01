import streamlit as st
import requests
import json
from PyPDF2 import PdfReader
import pandas as pd
import base64

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
    prompts = f'''Role: Extract and present al the relevant information from {text_file}'''

    return prompts

def read_pdf(file):
    pdf = PdfReader(file)
    text = ''
    for page in pdf.pages:
        text += page.extract_text()
    return text

st.title('Compliance Prueba de concepto extraer info')

uploaded_files = st.file_uploader("Choose PDF files", type="pdf", accept_multiple_files=True)

df_info = pd.DataFrame()
df_all_text = pd.DataFrame()

for file in uploaded_files:
    text = read_pdf(file)
    all_text_df = pd.DataFrame({'All Text': [text]})
    df_all_text = pd.concat([df_all_text, all_text_df], ignore_index=True)

st.title('Información para compliance')

if st.button('Create'):
    with st.spinner('Writing...'):
        for index, row in df_all_text.iterrows():
            # Create the 'prompts' variable
            st.session_state.prompts = prompt_compliance(row['All Text'])

            # Call the 'send_message()' function with the 'prompts' variable
            st.session_state.result = create_text(st.session_state.prompts)

            # Display the result
            st.write(st.session_state.result)

# Allow the user to propose changes
if st.session_state.result != "":
    user_changes = st.text_input('¿Qué más quieres del archivo?')
    if st.button('Responder'):
        if user_changes:
            st.session_state.prompts += f" Please follow these instructions: {user_changes.strip()}"
            with st.spinner('Applying changes...'):
                st.session_state.result = create_text(st.session_state.prompts)
            st.write(st.session_state.result)
