import pandas as pd

# Lien vers l'API
url = "https://static.data.gouv.fr/resources/bases-de-donnees-annuelles-des-accidents-corporels-de-la-circulation-routiere-annees-de-2005-a-2021/20231005-094147/vehicules-2022.csv"

# Charger les données en utilisant Pandas
data = pd.read_csv(url, sep=";")

# Utilisation de la méthode iterrows() pour parcourir chaque ligne
for index, row in data.iterrows():
    # Vous pouvez accéder aux colonnes spécifiques de chaque ligne comme ceci :
    print(row['colonne1'], row['colonne2'])

    # Pour accéder à toutes les colonnes de la ligne :
    # print(row)

    # Si vous souhaitez vous arrêter après un certain nombre de lignes, par exemple, les 10 premières, vous pouvez ajouter une condition d'arrêt.
    if index >= 10:
        break
