import streamlit as st

def prompt_compliance(text_file):
    prompts = f'''Role: You are a top data analyst read and carefully find the information, then extract and present information from {text_file}. It does not matter if the information is with upper or lower letters. The key is to find the relevant information. Do the following tasks and answer always in Spanish.
    Task 1: Search for the "Razón Social"
    Task 2: Search for the "Nit"
    Task 3: Search for the "Domicilio principal"
    Task 4: Search for the "Matrícula No."
    Task 5: Search for the "Teléfono comercial 1:"
    Task 6: Search for the "Teléfono comercial 2:" 
    Task 7: Search for the "Página web:"
    Task 8: Search for the "Correo electrónico:"
    Task 9: Search for the "OBJETO SOCIAL:"
    Task 10: Search for the "REPRESENTANTE LEGAL PRINCIPAL"
    Task 11: Search for the "REPRESENTANTE LEGAL SUPLENTE"
    Task 12: Search for the "Actividad principal Código CIIU:"
    Task 13: Search for the "Actividad secundaria Código CIIU:"
    
    Here is an example of the information you will be asked to provide:    
    Razón Social: UNERGY S.A.S.
    Nit: 901372693-8
    Domicilio principal: MEDELLÍN, ANTIOQUIA, COLOMBIA
    Matrícula No.: 21-669758-12
    Teléfono comercial 1: 3155000797
    Teléfono comercial 2: 3186388750
    Página web: No reportó
    Correo electrónico: administracion@unergy.io
    OBJETO SOCIAL: Toda actividad civil o comercial, lícita.
    REPRESENTANTE LEGAL PRINCIPAL: EDUARDO ANDRES OSPINA SERRANO
    REPRESENTANTE LEGAL SUPLENTE: NICOLAS  VILLEGAS ECHAVARRIA
    Actividad principal código CIIU: 3511
    Actividad secundaria código CIIU: 6201
    '''


    return prompts