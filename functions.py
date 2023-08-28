import streamlit as st

def prompt_compliance(text_file):
    prompts = f'''Role: You are a top data analyst carefully ingest the following text {text_file}  It does not matter if the information is with upper or lower letters. The key is to find the relevant information. Do not stop untill you find the information. Do the following tasks and answer always in Spanish.
    Task 1: Search for Razón Social
    Task 2: Search for Nit
    Task 3: Search for Domicilio principal
    Task 4: Search for Matrícula No.
    Task 5: Search for Teléfono comercial 1
    Task 6: Search for Teléfono comercial 2
    Task 7: Search for Página web
    Task 8: Search for Correo electrónico
    Task 9: Search for tOBJETO SOCIAL
    Task 10: Search for tREPRESENTANTE LEGAL PRINCIPAL
    Task 11: Search for REPRESENTANTE LEGAL SUPLENTE
    Task 12: Search for Actividad principal Código CIIU
    Task 13: Search for Actividad secundaria Código CIIU

    '''


    return prompts