import pandas as pd
import csv

def get_dep() : 
    """
    Retourne les coordonées de chaque département.
    Args:
        aucun
    Returns:
        {"01": (46.099, 5.349, "Ain"), "02": (49.559, 3.333, "Aisne"), . . .}
    """
    return  {
        "01": (46.099, 5.349, "Ain"),
        "02": (49.559, 3.333, "Aisne"),
        "03": (46.394, 3.188, "Allier"),
        "04": (44.106, 6.244, "Alpes-de-Haute-Provence"),
        "05": (44.664, 6.262, "Hautes-Alpes"),
        "06": (43.938, 7.116, "Alpes-Maritimes"),
        "07": (44.539, 4.383, "Ardèche"),
        "08": (49.616, 4.712, "Ardennes"),
        "09": (42.920, 1.504, "Ariège"),
        "10": (48.304, 4.155, "Aube"),
        "11": (43.194, 2.922, "Aude"),
        "12": (44.259, 2.544, "Aveyron"),
        "13": (43.474, 5.390, "Bouches-du-Rhône"),
        "14": (49.104, -0.289, "Calvados"),
        "15": (45.085, 2.765, "Cantal"),
        "16": (45.849, 0.675, "Charente"),
        "17": (45.833, -0.674, "Charente-Maritime"),
        "18": (47.147, 2.215, "Cher"),
        "19": (45.409, 1.439, "Corrèze"),
        "2A": (41.927, 8.738, "Corse-du-Sud"),
        "2B": (42.296, 9.164, "Haute-Corse"),
        "21": (47.321, 4.866, "Côte-d'Or"),
        "22": (48.415, -2.840, "Côtes-d'Armor"),
        "23": (45.954, 2.160, "Creuse"),
        "24": (45.144, 0.761, "Dordogne"),
        "25": (47.245, 6.024, "Doubs"),
        "26": (44.722, 4.556, "Drôme"),
        "27": (49.030, 1.156, "Eure"),
        "28": (48.447, 1.507, "Eure-et-Loir"),
        "29": (48.049, -4.095, "Finistère"),
        "30": (43.908, 4.282, "Gard"),
        "31": (43.605, 1.443, "Haute-Garonne"),
        "32": (43.796, 0.622, "Gers"),
        "33": (44.983, -0.511, "Gironde"),
        "34": (43.581, 3.674, "Hérault"),
        "35": (48.113, -1.685, "Ille-et-Vilaine"),
        "36": (46.819, 1.675, "Indre"),
        "37": (47.253, 0.720, "Indre-et-Loire"),
        "38": (45.171, 5.742, "Isère"),
        "39": (46.673, 5.590, "Jura"),
        "40": (43.883, -0.751, "Landes"),
        "41": (47.671, 1.389, "Loir-et-Cher"),
        "42": (45.433, 4.395, "Loire"),
        "43": (45.139, 3.833, "Haute-Loire"),
        "44": (47.326, -1.642, "Loire-Atlantique"),
        "45": (47.977, 2.743, "Loiret"),
        "46": (44.603, 1.580, "Lot"),
        "47": (44.367, 0.757, "Lot-et-Garonne"),
        "48": (44.523, 3.501, "Lozère"),
        "49": (47.500, -0.750, "Maine-et-Loire"),
        "50": (49.144, -1.255, "Manche"),
        "51": (48.938, 4.219, "Marne"),
        "52": (48.023, 4.958, "Haute-Marne"),
        "53": (48.153, -0.620, "Mayenne"),
        "54": (48.692, 6.184, "Meurthe-et-Moselle"),
        "55": (49.141, 5.405, "Meuse"),
        "56": (47.735, -2.860, "Morbihan"),
        "57": (49.041, 6.227, "Moselle"),
        "58": (47.283, 3.751, "Nièvre"),
        "59": (50.628, 3.057, "Nord"),
        "60": (49.650, 2.278, "Oise"),
        "61": (48.549, 0.402, "Orne"),
        "62": (50.541, 2.285, "Pas-de-Calais"),
        "63": (45.771, 3.109, "Puy-de-Dôme"),
        "64": (43.323, -0.416, "Pyrénées-Atlantiques"),
        "65": (42.991, 0.128, "Hautes-Pyrénées"),
        "66": (42.610, 2.833, "Pyrénées-Orientales"),
        "67": (48.288, 7.409, "Bas-Rhin"),
        "68": (47.875, 7.267, "Haut-Rhin"),
        "69": (45.758, 4.841, "Rhône"),
        "70": (47.641, 6.187, "Haute-Saône"),
        "71": (46.655, 4.350, "Saône-et-Loire"),
        "72": (48.006, 0.199, "Sarthe"),
        "73": (45.555, 6.393, "Savoie"),
        "74": (45.977, 6.113, "Haute-Savoie"),
        "75": (48.859, 2.351, "Paris"),
        "76": (49.443, 0.105, "Seine-Maritime"),
        "77": (48.628, 2.990, "Seine-et-Marne"),
        "78": (48.818, 2.135, "Yvelines"),
        "79": (46.617, -0.169, "Deux-Sèvres"),
        "80": (49.895, 2.302, "Somme"),
        "81": (43.731, 1.378, "Tarn"),
        "82": (44.044, 1.356, "Tarn-et-Garonne"),
        "83": (43.471, 6.641, "Var"),
        "84": (44.054, 5.050, "Vaucluse"),
        "85": (46.648, -1.418, "Vendée"),
        "86": (46.577, 0.609, "Vienne"),
        "87": (45.833, 1.261, "Haute-Vienne"),
        "88": (48.170, 6.446, "Vosges"),
        "89": (47.800, 3.574, "Yonne"),
        "90": (47.632, 6.856, "Territoire de Belfort"),
        "91": (48.522, 2.341, "Essonne"),
        "92": (48.900, 2.259, "Hauts-de-Seine"),
        "93": (48.917, 2.333, "Seine-Saint-Denis"),
        "94": (48.791, 2.393, "Val-de-Marne"),
        "95": (49.046, 2.167, "Val-d'Oise"),
        "971": (16.230, -61.504, "Guadeloupe"),
        "972": (14.641, -61.024, "Martinique"),
        "973": (4.069, -52.339, "Guyane"),
        "974": (-21.130, 55.526, "La Réunion"),
    }

def get_OBS() : 
    """
    Retourne les différents type d'accident.
    Args:
        aucun
    Returns:
        { "-1": "Non renseigné", "1" : "Véhicule en stationnement ", "2" : "Arbre ", "3" : "Glissière métallique ", "4" : "Glissière béton" , "5" : "Autre glissière" , . . . }
    """
    return {
        "-1": "Non renseigné",
        "1" : "Véhicule en stationnement ",
        "2" : "Arbre ",
        "3" : "Glissière métallique ",
        "4" : "Glissière béton" ,
        "5" : "Autre glissière" ,
        "6" : "Bâtiment, mur, pile de pont", 
        "7" : "Support de signalisation verticale ou poste d'appel d'urgence ",
        "8" : "Poteau" ,
        "9" : "Mobilier urbain ",
        "10": "Parapet" ,
        "11" : "Ilot, refuge, borne haute" ,
        "12" : "Bordure de trottoir" ,
        "13" : "Fossé, talus, paroi rocheuse" ,
        "14" : "Autre obstacle fixe sur chaussée" ,
        "15" : "Autre obstacle fixe sur trottoir ou accotement" ,
        "16" : "Sortie de chaussée sans obstacle" ,
        "17" : "Buse - tête d'aqueduc",
    }



if __name__ == '__main__':
    # Obtenir les données
    dep_data = get_dep()
    obs_data = get_OBS()

    # Créer un DataFrame pour le dictionnaire "dep"
    dep_df = pd.DataFrame(list(dep_data.values()), columns=["Latitude", "Longitude", "Nom"])
    dep_df.index = dep_data.keys()

    # Créer un DataFrame pour le dictionnaire "OBS"
    obs_df = pd.DataFrame(list(obs_data.items()), columns=["Code", "Description"])

    # Nom des fichiers Excel de sortie
    dep_excel_filename = "departements.csv"
    obs_excel_filename = "obstacles.csv"

    # Écrit les données du dictionnaire "dep" dans le fichier CSV
    with open(dep_excel_filename, 'w', newline='', encoding='utf8') as dep_csvfile:
        dep_csvwriter = csv.writer(dep_csvfile, delimiter=';')
        dep_csvwriter.writerow(["Code", "Latitude", "Longitude", "Nom"])
        for code, data in dep_data.items():
            dep_csvwriter.writerow([code, data[0], data[1], data[2]])

    # Écrit les données du dictionnaire "OBS" dans le fichier CSV
    with open(obs_excel_filename, 'w', newline='', encoding='utf8') as obs_csvfile:
        obs_csvwriter = csv.writer(obs_csvfile, delimiter=';')
        obs_csvwriter.writerow(["Code", "Description"])
        for code, description in obs_data.items():
            obs_csvwriter.writerow([code, description])

    print(f"Les fichiers Excel {dep_excel_filename} et {obs_excel_filename} ont été créés.")