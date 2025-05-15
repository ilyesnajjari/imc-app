import streamlit as st
from api_client import calculate_imc, save_imc, get_history, clear_history
import pandas as pd
import requests

st.set_page_config(page_title="Calculateur d'IMC", layout="centered")

st.title("Calculateur d'IMC ")

nom = st.text_input("Nom (optionnel)", value="Anonyme")
poids = st.number_input("Poids (kg)", min_value=10.0, max_value=300.0, step=0.1)
taille = st.number_input("Taille (cm)", min_value=50.0, max_value=250.0, step=1.0)

if st.button("Calculer IMC"):
    try:
        result = calculate_imc(poids, taille, nom)
        st.success(f"Votre IMC est de {result['imc']} → {result['interpretation']}")
    except Exception as e:
        st.error(f"Erreur lors du calcul : {e}")

if st.button("Sauvegarder ce calcul"):
    try:
        resp = save_imc(poids, taille, nom)
        st.success(f"Calcul sauvegardé, ID: {resp['id']}")
    except Exception as e:
        st.error(f"Erreur lors de la sauvegarde : {e}")

if st.button("Afficher historique"):
    try:
        history = get_history()
        if history:
            df = pd.DataFrame(history)
            st.dataframe(df)
        else:
            st.info("Aucun historique disponible.")
    except Exception as e:
        st.error(f"Erreur lors de la récupération : {e}")


if st.button("Supprimer l'historique"):
    try:
        response_data = clear_history()
        st.success(response_data["message"])
    except Exception as e:
        st.error(f"Erreur lors de la suppression : {e}")


#streamlit run frontend/app.py

