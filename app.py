import streamlit as st
import requests
import json

# Constants
API_URL = "https://api.anthropic.com/v1/complete"
MODEL = "claude-2.0"
MAX_TOKENS = 10000
STOP_SEQS = ["\n\nHuman:"]

# Initialize session state variables
if "result" not in st.session_state:
    st.session_state.result = ""
if "prompts" not in st.session_state:
    st.session_state.prompts = ""

def create_text(prompt, temperature):
    """Send a prompt to the Claude API and get a response."""
    headers = {
        "Content-Type": "application/json",
        "X-API-Key": st.secrets["API_KEY"]  # Use the API key from Streamlit's secrets
    }
    conversation = f"Human: {prompt}\n\nAssistant:"
    body = {
        "prompt": conversation,
        "model": MODEL,
        "temperature": temperature,
        "max_tokens_to_sample": MAX_TOKENS,
        "stop_sequences": STOP_SEQS
    }
    try:
        response = requests.post(API_URL, headers=headers, data=json.dumps(body))
        response.raise_for_status()
    except Exception as e:
        st.error(f"Unexpected error: {e}")
        return None
    return response.json()['completion']

def prompt_creator_decks(language, audience, tone, length_in_words, intention, context, customer_segments):
    """Create a prompt for generating a slide deck."""
    return f"""Role: You are Nancy Duarte part of the Kravata team an expert in crafting slide Decks for startups. You are creating a slide Deck for Kravata and your answers needs to be always in {language}. 
                Your audience is {audience} and your tone should be {tone}, limit your response to {length_in_words} words. No need to write what you are doing, who you are or writting anything diferent than your answer. 
                The purpose of the deck is {intention}.
                Here is some context: {context}
                Task 1: Deeply analyze the following information about Kravata: {kravata_memo} and analyze the following text {customer_segments} 
                to find relevant information about the audiences. And use it in your answers.
                Task 2: Craft the slides deck with the following steps: Step 1. The Title of each slide and the information that should be in the slide; 
                Step 2 A suggestion of the visuals in the slide and Step 3 The rationale behind the slide, why it is important"""

def create_decks_page():
    """Create the main page of the Streamlit app."""
    st.image("Kravata.png", width=400)
    st.title('Create Decks')
    intention, language, audience, tone, length_in_words, context, creativity_level = transversal_options()
    if st.button('Create'):
        with st.spinner('Writing...'):
            st.session_state.prompts = prompt_creator_decks(language, audience, tone, length_in_words, intention, context, customers_segments)
            st.session_state.result = create_text(st.session_state.prompts, creativity_level)
            st.write(st.session_state.result)
    if st.session_state.result != "":
        user_changes = st.text_input('Propose changes to the deck:')
        if st.button('Apply Changes'):
            if user_changes:
                st.session_state.prompts += f" Please change the communications piece with the following instructions: {user_changes.strip()}"
                with st.spinner('Applying changes...'):
                    st.session_state.result = create_text(st.session_state.prompts, creativity_level)
                st.write(st.session_state.result)

def transversal_options():
    """Fetch transversal options."""
    # TODO: Add code to fetch the transversal options.
    pass

def main():
    """Main entry point for the Streamlit app."""
    create_decks_page()

if __name__ == "__main__":
    main()
