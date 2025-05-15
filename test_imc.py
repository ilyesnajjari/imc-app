import requests

FRONTEND_URL = "http://localhost:8501"
BACKEND_URL = "http://localhost:8000"

def test_calculate():
    data = {"poids": 70, "taille": 175, "nom": "Testeur"}
    resp = requests.post(f"{BACKEND_URL}/calculate", json=data)
    assert resp.status_code == 200, "Erreur API calculate"
    result = resp.json()
    print(f"IMC calculé : {result['imc']} → {result['interpretation']}")

def test_save():
    data = {"poids": 70, "taille": 175, "nom": "Testeur"}
    resp = requests.post(f"{BACKEND_URL}/save", json=data)
    assert resp.status_code == 200, "Erreur API save"
    print("Enregistrement OK, ID:", resp.json().get("id"))

def test_history():
    resp = requests.get(f"{BACKEND_URL}/history")
    assert resp.status_code == 200, "Erreur API history"
    records = resp.json()
    print(f"Historique ({len(records)} entrées) :")
    for rec in records:
        print(f"  - {rec['nom']} : IMC {rec['imc']} ({rec['interpretation']})")

def test_clear_history():
    resp = requests.delete(f"{BACKEND_URL}/history/clear")
    assert resp.status_code == 200, "Erreur API clear"
    print("Historique supprimé :", resp.json()["message"])


if __name__ == "__main__":
    print("Tester l'API IMC FastAPI\n")
    test_calculate()
    test_save()
    test_history()
    test_clear_history()



#pip install requests
#python test_imc.py
