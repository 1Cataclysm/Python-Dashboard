import dash
from dash import dcc, html
import folium
import caracteristique
from dash.dependencies import Input, Output
from folium import IFrame

coord_dict = {
    "01": (46.099, 5.349, "Ain"),
    "02": (49.559, 3.558, "Aisne"),
    "03": (46.394, 3.188, "Allier"),
    "04": (44.106, 6.244, "Alpes-de-Haute-Provence"),
    "05": (44.664, 6.263, "Hautes-Alpes"),
    "06": (43.937, 7.116, "Alpes-Maritimes"),
    "07": (44.751, 4.425, "Ardèche"),
    "08": (49.615, 4.641, "Ardennes"),
    "09": (42.920, 1.504, "Ariège"),
    "10": (48.304, 4.161, "Aube"),
    "11": (43.103, 2.415, "Aude"),
    "12": (44.281, 2.680, "Aveyron"),
    "13": (43.543, 5.086, "Bouches-du-Rhône"),
    "14": (49.099, 0.364, "Calvados"),
    "15": (45.051, 2.669, "Cantal"),
    "16": (45.718, 0.202, "Charente"),
    "17": (45.781, 0.674, "Charente-Maritime"),
    "18": (47.065, 2.488, "Cher"),
    "19": (45.354, 1.877, "Corrèze"),
    "2A": (41.865, 8.988, "Corse-du-Sud"),
    "2B": (42.394, 9.206, "Haute-Corse"),
    "21": (47.425, 4.772, "Côte-d'Or"),
    "22": (48.441, 2.865, "Côtes-d'Armor"),
    "23": (46.057, 2.019, "Creuse"),
    "24": (45.104, 0.741, "Dordogne"),
    "25": (47.166, 6.361, "Doubs"),
    "26": (44.685, 5.168, "Drôme"),
    "27": (49.115, 0.996, "Eure"),
    "28": (48.387, 1.370, "Eure-et-Loir"),
    "29": (48.261, 4.058, "Finistère"),
    "30": (43.993, 4.180, "Gard"),
    "31": (43.358, 1.173, "Haute-Garonne"),
    "32": (43.692, 0.453, "Gers"),
    "33": (44.826, 0.575, "Gironde"),
    "34": (43.579, 3.367, "Hérault"),
    "35": (48.154, 1.638, "Ille-et-Vilaine"),
    "36": (46.777, 1.576, "Indre"),
    "37": (47.258, 0.691, "Indre-et-Loire"),
    "38": (45.264, 5.576, "Isère"),
    "39": (46.729, 5.698, "Jura"),
    "40": (43.965, 0.784, "Landes"),
    "41": (47.617, 1.429, "Loir-et-Cher"),
    "42": (45.727, 4.166, "Loire"),
    "43": (45.128, 3.806, "Haute-Loire"),
    "44": (47.361, 1.682, "Loire-Atlantique"),
    "45": (47.912, 2.344, "Loiret"),
    "46": (44.371, 1.271, "Lot"),
    "47": (44.367, 0.460, "Lot-et-Garonne"),
    "48": (44.517, 3.500, "Lozère"),
    "49": (47.391, 0.564, "Maine-et-Loire"),
    "50": (49.079, 1.327, "Manche"),
    "51": (48.949, 4.236, "Marne"),
    "52": (45.157, 6.256, "Haute-Marne"),
    "53": (48.147, 0.658, "Mayenne"),
    "54": (48.787, 6.165, "Meurthe-et-Moselle"),
    "55": (48.989, 5.382, "Meuse"),
    "56": (47.847, 2.810, "Morbihan"),
    "57": (49.037, 6.663, "Moselle"),
    "58": (47.115, 3.504, "Nièvre"),
    "59": (50.448, 3.220, "Nord"),
    "60": (49.410, 2.425, "Oise"),
    "61": (48.623, 0.129, "Orne"),
    "62": (50.494, 2.288, "Pas-de-Calais"),
    "63": (45.726, 3.141, "Puy-de-Dôme"),
    "64": (43.221, 0.762, "Pyrénées-Atlantiques"),
    "65": (43.127, 0.174, "Hautes-Pyrénées"),
    "66": (42.689, 2.832, "Pyrénées-Orientales"),
    "67": (48.383, 7.617, "Bas-Rhin"),
    "68": (47.918, 7.384, "Haut-Rhin"),
    "69": (45.754, 4.885, "Rhône"),
    "70": (47.688, 6.120, "Haute-Saône"),
    "71": (46.667, 4.450, "Saône-et-Loire"),
    "72": (47.898, 0.220, "Sarthe"),
    "73": (45.600, 6.401, "Savoie"),
    "74": (46.045, 6.335, "Haute-Savoie"),
    "75": (48.856, 2.352, "Paris"),
    "76": (49.494, 0.107, "Seine-Maritime"),
    "77": (48.646, 2.712, "Seine-et-Marne"),
    "78": (48.812, 2.097, "Yvelines"),
    "79": (46.617, 0.149, "Deux-Sèvres"),
    "80": (49.892, 2.302, "Somme"),
    "81": (43.939, 1.849, "Tarn"),
    "82": (44.077, 1.248, "Tarn-et-Garonne"),
    "83": (43.373, 6.616, "Var"),
    "84": (44.068, 5.103, "Vaucluse"),
    "85": (46.669, 1.427, "Vendée"),
    "86": (46.581, 0.336, "Vienne"),
    "87": (45.889, 1.062, "Haute-Vienne"),
    "88": (48.235, 6.077, "Vosges"),
    "89": (47.799, 3.566, "Yonne"),
    "90": (47.639, 6.877, "Territoire de Belfort"),
    "91": (48.520, 2.243, "Essonne"),
    "92": (48.847, 2.245, "Hauts-de-Seine"),
    "93": (48.917, 2.478, "Seine-Saint-Denis"),
    "94": (48.777, 2.468, "Val-de-Marne"),
    "95": (49.082, 2.131, "Val-d'Oise")
}

# Obtenir les données pour la carte
nb_accidents_par_departement = caracteristique.get_data(1)

# Créer une application Dash
app = dash.Dash(__name__)

# Créer la carte Folium
m = folium.Map(location=[46.603354, 1.888334], zoom_start=6)

# Définir un rayon fixe pour tous les cercles (par exemple, 5000)
fixed_radius = 5
total = 0
# Parcourir les départements et ajouter des cercles colorés
for departement, nb_accidents in nb_accidents_par_departement.items():
    if departement in coord_dict:
        total += 1
        lat, lon, name = coord_dict[departement]
        popup_html = f'<h5>{name}</h5><p>{nb_accidents} accidents</p>'
        iframe = IFrame(html=popup_html, width=100, height=100)
        popup = folium.Popup(iframe, max_width=200)
        folium.CircleMarker(
            location=[lat, lon],
            radius=fixed_radius,  # Utilisation du rayon fixe pour tous les cercles
            fill=True,
            color='red',
            fill_opacity=0.6,
            popup=popup
        ).add_to(m)

# Sauvegarder la carte en tant que fichier HTML temporaire
m.save('temp_map.html')
print(total)
# Mise en page de l'application
app.layout = html.Div([
    html.H1("Ma page"),  # Titre de la page
    html.Iframe(srcDoc=open('temp_map.html', 'r').read(), width='100%', height='600')
])

# Exécuter l'application
if __name__ == '__main__':
    app.run_server(debug=True)