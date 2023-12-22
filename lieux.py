import pandas as pd
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

def get_lieux_data():
    """
    Retourne la liste de tous les vma (vitesse maximale autorisée sur le lieu de l'accident)
    Args:
        aucun
    Returns:
        []
    """
    # Lien vers l'API
    url = "https://static.data.gouv.fr/resources/bases-de-donnees-annuelles-des-accidents-corporels-de-la-circulation-routiere-annees-de-2005-a-2021/20231005-094112/lieux-2022.csv"

    # Charger les données en utilisant Pandas
    data = pd.read_csv(url, sep=";", low_memory=False)

    # Convertir en int les valeurs de vma
    data['vma'] = pd.to_numeric(data['vma'], errors='coerce')  
    data = data.dropna(subset=['vma'])
    data['vma'] = data['vma'].astype(int) 
    data = data[(data['vma'] >= 0) & (data['vma'] <= 200)]

    return data