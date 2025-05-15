import requests
import os

API_URL = os.getenv("API_URL", "http://backend:8000")

def calculate_imc(poids: float, taille: float, nom: str = "Anonyme"):
    payload = {"poids": poids, "taille": taille, "nom": nom}
    response = requests.post(f"{API_URL}/calculate", json=payload)
    response.raise_for_status()
    return response.json()
    
def save_imc(poids: float, taille: float, nom: str = "Anonyme"):
    payload = {"poids": poids, "taille": taille, "nom": nom}
    response = requests.post(f"{API_URL}/save", json=payload)
    response.raise_for_status()
    return response.json()

def get_history():
    response = requests.get(f"{API_URL}/history")
    response.raise_for_status()
    return response.json()

def clear_history():
    response = requests.delete(f"{API_URL}/history/clear")
    response.raise_for_status()
    return response.json()
