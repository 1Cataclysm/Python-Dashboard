import pandas as pd
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

def get_data(flag):
    # Lien vers l'API
    url = "https://static.data.gouv.fr/resources/bases-de-donnees-annuelles-des-accidents-corporels-de-la-circulation-routiere-annees-de-2005-a-2021/20231005-093927/carcteristiques-2022.csv"

    # Charger les données en utilisant Pandas
    data = pd.read_csv(url, sep=";")

    data_accident = {}

    nb_acc_dp = {}

    for index, row in data.iterrows():
        departement = str(row['dep'])
        adresse = str(row['adr'])
        latitude = float(row['lat'].replace(',', '.'))
        longitude = float(row['long'].replace(',', '.'))
        
        if(departement.isdigit() and int(departement) < 99 or departement == '2B' or departement == '2A'):

            if departement not in data_accident:
                data_accident[departement] = set()
            
            data_accident[departement].add((adresse, latitude, longitude))
            
            if departement not in nb_acc_dp:
                nb_acc_dp[departement] = 1
            else:
                nb_acc_dp[departement] += 1

    if flag == 0:
        return data_accident
    elif flag == 1:
        return nb_acc_dp


# -------------------------------------------------------------------------------- #
