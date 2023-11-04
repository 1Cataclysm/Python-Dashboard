import pandas as pd
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

# ** 
# retourne un dictionnaire contenant soit tous les accidents,
# soit le nombre d'accidents par départements soit le nombre d'accidents par jour pour chaque mois
# **

mois_annee = {
    1: 'janvier', 2: 'fevrier', 3: 'mars', 4: 'avril', 5: 'mai', 6: 'juin',
    7: 'juillet', 8: 'aout', 9: 'septembre', 10: 'octobre', 11: 'novembre', 12: 'decembre'
}

def get_data(flag):
    # Lien vers l'API
    url = "https://static.data.gouv.fr/resources/bases-de-donnees-annuelles-des-accidents-corporels-de-la-circulation-routiere-annees-de-2005-a-2021/20231005-093927/carcteristiques-2022.csv"

    # Charger les données en utilisant Pandas
    data = pd.read_csv(url, sep=";")

    data_accident = {}
    nb_acc_dp = {}
    details_acc_mois = {mois: {} for mois in ['janvier', 'fevrier', 'mars', 'avril', 'mai', 'juin', 'juillet', 'aout', 'septembre', 'octobre', 'novembre', 'decembre']}

    for index, row in data.iterrows():
        departement = str(row['dep'])
        adresse = str(row['adr'])
        latitude = float(row['lat'].replace(',', '.'))
        longitude = float(row['long'].replace(',', '.'))
        jour = row['jour']
        mois = mois_annee.get(row['mois'], 'inconnu')
        
        if(departement.isdigit() and int(departement) < 99 or departement == '2B' or departement == '2A'):

            if departement not in data_accident:
                data_accident[departement] = set()
            
            data_accident[departement].add((adresse, latitude, longitude))
            
            if departement not in nb_acc_dp:
                nb_acc_dp[departement] = 1
            else:
                nb_acc_dp[departement] += 1

            if jour not in details_acc_mois[mois]:
                details_acc_mois[mois][jour] = 0

            details_acc_mois[mois][jour] += 1

    if flag == 0:
        # retourne tous les accidents
        return data_accident
    elif flag == 1:
        # retourne le nombre d'accidents par département
        return nb_acc_dp
    elif flag == 3:
        sorted_details_acc_mois = {}
        for mois, jours in details_acc_mois.items():
            # Trie par jour dans le mois
            sorted_jours = dict(sorted(jours.items(), key=lambda item: int(item[0])))
            sorted_details_acc_mois[mois] = sorted_jours
        return sorted_details_acc_mois