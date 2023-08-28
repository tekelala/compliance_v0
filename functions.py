import streamlit as st

def prompt_compliance(text_file):
    prompts = f'''Role: You are a top data analyst and you are going to receive information about companies. Carefully ingest the following text {text_file}  It does not matter if the information is with upper or lower letters. The key is to find the relevant information. Answer the following questions always in Spanish:
    Task 1: What is the Razón Social (name of the company)?
    Task 2: What is the Nit number (tax id number)?
    Task 3: What is the Domicilio principal (address)?
    Task 4: What is the Matrícula No. (registration number)?
    Task 5: What is the Teléfono comercial 1 (phone number)?
    Task 6: What is the Teléfono comercial 2 (phone number)?
    Task 7: What is the Página web (website)?
    Task 8: What is the Correo electrónico (email)?
    Task 9: What is the OBJETO SOCIAL (social object)?
    Task 10: What is the REPRESENTANTE LEGAL PRINCIPAL (representative legal principal)?
    Task 11: What is the REPRESENTANTE LEGAL SUPLENTE (representative legal suplente)?
    Task 12: What is the Actividad principal CÓDIGO CIIU (main activity code CIIU)?
    Task 13: What is the Actividad secundaria CÓDIGO CIIU (secondary activity code CIIU)?

    '''


    return prompts