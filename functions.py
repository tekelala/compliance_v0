import streamlit as st

def prompt_compliance(text_file):
    prompts = f'''Role: You are a top data analyst carefully ingest the following text {text_file}  It does not matter if the information is with upper or lower letters. The key is to find the relevant information. Do not stop untill you find the information. Do the following tasks and answer always in Spanish.
    Task 1: Search for the information after the text "Razón Social"
    Task 2: Search for the information after the text "Nit"
    Task 3: Search for the information after the text  "Domicilio principal"
    Task 4: Search for the information after the text  "Matrícula No."
    Task 5: Search for the information after the text  "Teléfono comercial 1:"
    Task 6: Search for the information after the text  "Teléfono comercial 2:" 
    Task 7: Search for the information after the text  "Página web:"
    Task 8: Search for the information after the text  "Correo electrónico:"
    Task 9: Search for the information after the text  "OBJETO SOCIAL:"
    Task 10: Search for the information after the text  "REPRESENTANTE LEGAL PRINCIPAL"
    Task 11: Search for the information after the text  "REPRESENTANTE LEGAL SUPLENTE"
    Task 12: Search for the information after the text  "Actividad principal Código CIIU:"
    Task 13: Search for the information after the text  "Actividad secundaria Código CIIU:"

    '''


    return prompts