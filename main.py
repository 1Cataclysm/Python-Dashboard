import pandas as pd

# Lien vers l'API
url = "https://static.data.gouv.fr/resources/bases-de-donnees-annuelles-des-accidents-corporels-de-la-circulation-routiere-annees-de-2005-a-2021/20231005-094147/vehicules-2022.csv"

# Charger les données en utilisant Pandas
data = pd.read_csv(url, sep=";")

# Afficher les 5 premières lignes pour vérification
# print(data.head(500))

for index, row in data.iterrows():
    if row["occutc"] > 0:
        print(row["occutc"])