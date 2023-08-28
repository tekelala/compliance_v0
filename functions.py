import streamlit as st

def prompt_compliance(text_file):
    prompts = f'''Role: You are a top data analyst read and carefully find the information, then extract and present information from {text_file}. Do the following tasks and answer always in Spanish.
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