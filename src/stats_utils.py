"""
stats_utils.py
Script d'analyse statistique des ventes.
Guide 3 - Onboarding Data Analyst
"""

import statistics


def analyser_ventes(transactions):
    """
    Analyse une liste de montants de transactions et retourne
    un dictionnaire d'indicateurs statistiques.
    """
    # Nettoyage : on ignore les valeurs négatives ou nulles
    ventes_valides = [t for t in transactions if t > 0]

    if not ventes_valides:
        return {
            "nombre_transactions": 0,
            "somme_totale": 0,
            "moyenne": 0,
            "mediane": 0,
            "ecart_type": 0,
            "max": None,
            "min": None,
            "etendue": 0,
            "anomalies": []
        }

    nombre = len(ventes_valides)
    somme = sum(ventes_valides)
    moyenne = somme / nombre
    mediane = statistics.median(ventes_valides)
    ecart_type = statistics.stdev(ventes_valides) if nombre > 1 else 0
    valeur_max = max(ventes_valides)
    valeur_min = min(ventes_valides)

    # Calcul de l'étendue
    etendue = calculer_etendue(ventes_valides)


    # Détection des anomalies : transactions supérieures à 2x la moyenne
    seuil_anomalie = 2 * moyenne
    anomalies = [t for t in ventes_valides if t > seuil_anomalie]

    return {
        "nombre_transactions": nombre,
        "somme_totale": somme,
        "moyenne": round(moyenne, 2),
        "mediane": mediane,
        "ecart_type": round(ecart_type, 2),
        "max": valeur_max,
        "min": valeur_min,
        "etendue": etendue,
        "anomalies": anomalies
    }


def calculer_etendue(ventes):
    """
    Calcule l'étendue d'une liste de ventes.

    L'étendue correspond à la différence entre
    la valeur maximale et la valeur minimale.
    """
    if not ventes:
        return 0

    return max(ventes) - min(ventes)



if __name__ == "__main__":
    # Jeu de données de test : montants de ventes en euros
    transactions_test = [150, 200, 180, -50, 0, 220, 175, 190, 2000, 160]

    resultats = analyser_ventes(transactions_test)

    print("=== Rapport d'analyse des ventes ===")
    print(f"Nombre de transactions valides : {resultats['nombre_transactions']}")
    print(f"Somme totale des ventes        : {resultats['somme_totale']} €")
    print(f"Moyenne                        : {resultats['moyenne']} €")
    print(f"Médiane                        : {resultats['mediane']} €")
    print(f"Écart-type                     : {resultats['ecart_type']} €")
    print(f"Valeur maximale                : {resultats['max']} €")
    print(f"Valeur minimale                : {resultats['min']} €")
    print(f"Étendue                        : {resultats['etendue']} €")
    print(f"Transactions anormales (> 2x moyenne) : {resultats['anomalies']}")