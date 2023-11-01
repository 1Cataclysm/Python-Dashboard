import pandas as pd
import ssl
import get_data

ssl._create_default_https_context = ssl._create_unverified_context

def get_data_vehicule():

    dic_obs=get_data.get_OBS()
    # Lien vers l'API
    url = "https://static.data.gouv.fr/resources/bases-de-donnees-annuelles-des-accidents-corporels-de-la-circulation-routiere-annees-de-2005-a-2021/20231005-094147/vehicules-2022.csv"

    # Charger les données en utilisant Pandas
    data = pd.read_csv(url, sep=";")

    data_accident = {}

    for index, row in data.iterrows():
        OBS = str(row['obs'])
        if OBS == "0" :
            continue
        if dic_obs[OBS] in data_accident :
            data_accident[dic_obs[OBS]] += 1
        else: 
            data_accident[dic_obs[OBS]] = 1
    return data_accident