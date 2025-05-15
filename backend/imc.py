def calcul_imc(poids_kg: float, taille_cm: float) -> float:
    taille_m = taille_cm / 100
    return round(poids_kg / (taille_m ** 2), 2)

def interpretation_imc(imc: float) -> str:
    if imc < 18.5:
        return "Maigreur"
    elif 18.5 <= imc < 25:
        return "Poids normal"
    elif 25 <= imc < 30:
        return "Surpoids"
    else:
        return "Obésité"
