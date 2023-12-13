import pandas as pd
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

# variable contenant les mois avec leur numéro
mois_annee = {
    1: 'janvier', 2: 'fevrier', 3: 'mars', 4: 'avril', 5: 'mai', 6: 'juin',
    7: 'juillet', 8: 'aout', 9: 'septembre', 10: 'octobre', 11: 'novembre', 12: 'decembre'
}

def get_data(flag):
    """
    Retourne un dictionnaire contenant : 
        si flag = 0 => dictionnaire contenant pour chaque département un set qui contient l'adresse et la localisation de l'accident
        si flag = 1 => dictionnaire contenant le nombre d'accident pour chaque département
        si flag = 2 => dictionnaire contenant le nombre d'accident pour chaque jour du mois trié par jour
    Args:
        flag: valeur entière positive
    Returns:
        {'90': {('10 Rue de la Pouchotte', 47.688894, 6.830803), ('SAVOUREUSE (RUE DE LA)', 47.649, 6.855), ... }}
        or {'26': 327, '25': 356, '22': 442, '16': 145, '13': 2255, '12': 173, '10': 359, '09': 157, '06' ... }
        or {'janvier': {1: 112, 2: 80, 3: 125, 4: 125, 5: 124, 6: 112, 7: 135, 8: 108, 9: 89, 10: 125, 11: 120, 12: 136, 13: 145, 14: 160, 15: 121, 16: 89, 17: 138, 18: 118, 19: 121, 20: 116, 21: 162, 22: 121, 23: 97, 24: 129, 25: 124, 26: 127, 27: 122, 28: 143, 29: 121, 30: 101, 31: 111}, . . . }
    """
    # Lien vers l'API
    url = "https://static.data.gouv.fr/resources/bases-de-donnees-annuelles-des-accidents-corporels-de-la-circulation-routiere-annees-de-2005-a-2021/20231005-093927/carcteristiques-2022.csv"

    # Charger les données en utilisant Pandas
    data = pd.read_csv(url, sep=";")

    # dictionnaire contenant pour chaque département un set qui contient l'adresse et la localisation de l'accident
    data_accident = {}
    
    # dictionnaire contenant le nombre d'accident pour chaque département
    nb_acc_dp = {}
    
    # dictionnaire contenant le nombre d'accident pour chaque jour du mois
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
    elif flag == 2:
        sorted_details_acc_mois = {}
        for mois, jours in details_acc_mois.items():
            # Trie par jour dans le mois
            sorted_jours = dict(sorted(jours.items(), key=lambda item: int(item[0])))
            sorted_details_acc_mois[mois] = sorted_jours
        return sorted_details_acc_mois