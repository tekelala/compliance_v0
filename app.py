import streamlit as st
import requests
import json
import pandas as pd

# Initialize session state variables
if "result" not in st.session_state:
    st.session_state.result = ""

# Claude functions
def create_text(prompt, temperature):
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
        "temperature": temperature,
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
def prompt_creator_decks(language, audience, tone, length_in_words, intention, context, customer_segments):
    prompts = f'''Role: You are Nancy Duarte part of the Kravata team an expert in crafting slide Decks for startups. You are creating a slide Deck for Kravata and your answers needs to be always in {language}. 
                Your audience is {audience} and your tone should be {tone}, limit your response to {length_in_words} words. No need to write what you are doing, who you are or writting anything diferent than your answer. 
                The purpose of the deck is {intention}.
                Here is some context: {context}
                Task 1: Deeply analize the following information about Kravata: {kravata_memo} and analyze the following text {customer_segments} 
                to find relevant information about the audiences. And use it in your answers.
                Task 2: Craft the slides deck with the following steps: Step 1. The Title of each slide and the information that should be in the slide; 
                Step 2 A suggestion of the visuals in the slide and Step 3 The rationale behind the slide, why it is important'''

    return prompts

def create_decks_page():
    st.image("Kravata.png", width=400)
    st.title('Create Decks')

    # Initialize session state variables if not already done
    if "result" not in st.session_state:
        st.session_state.result = ""
    if "prompts" not in st.session_state:
        st.session_state.prompts = ""

    intention, language, audience, tone, length_in_words, context, creativity_level = transversal_options()

    if st.button('Create'):
        with st.spinner('Writting...'):
            # Create the 'prompts' variable
            st.session_state.prompts = prompt_creator_decks(language, audience, tone, length_in_words, intention, context, customers_segments)

            # Call the 'send_message()' function with the 'prompts' variable
            st.session_state.result = create_text(st.session_state.prompts, creativity_level)

            # Display the prompt
            #st.write(st.session_state.prompts)
            # Display the result
            st.write(st.session_state.result)

    # Allow the user to propose changes
    if st.session_state.result != "":
        user_changes = st.text_input('Propose changes to the deck:')
        if st.button('Apply Changes'):
            if user_changes:
                st.session_state.prompts += f" Please change the communications piece with the following instructions: {user_changes.strip()}"
                with st.spinner('Applying changes...'):
                    st.session_state.result = create_text(st.session_state.prompts, creativity_level)
                st.write(st.session_state.result)