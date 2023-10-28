import dash
from dash import dcc, html
import folium, branca
import caracteristique
from dash.dependencies import Input, Output, State
from folium import IFrame

coord_dict = {
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

# Obtenir les données pour la carte
nb_accidents_par_departement = caracteristique.get_data(1)  # Remplacez ceci par vos données

# Créer une application Dash
app = dash.Dash(__name__)

# Créer la carte Folium initiale
m = folium.Map(location=[46.603354, 1.888334], zoom_start=6)

# Définir un rayon fixe pour tous les cercles (par exemple, 5000)
fixed_radius = 15

# Créer un colormap en fonction de vos données avec une palette de couleurs personnalisée
min_accidents = min(nb_accidents_par_departement.values())
max_accidents = max(nb_accidents_par_departement.values())

color_map = branca.colormap.LinearColormap(['green', 'gold', 'orange', 'red'], vmin=min_accidents, vmax=max_accidents)

# Fonction pour mettre à jour la carte en fonction de la valeur de filtre
def update_map(filter_value):
    # Effacez d'abord la carte actuelle
    m = folium.Map(location=[46.603354, 1.888334], zoom_start=6)
    for departement, nb_accidents in nb_accidents_par_departement.items():
        if departement in coord_dict and nb_accidents > filter_value:
            lat, lon, name = coord_dict[departement]
            popup_html = f'<h8>{name} {departement}</h8><p>{nb_accidents} accidents</p>'
            iframe = IFrame(html=popup_html, width=100, height=100)
            popup = folium.Popup(iframe, max_width=200)
            color = color_map(nb_accidents)  # Assigner une couleur en fonction du nombre d'accidents
            folium.CircleMarker(
                location=[lat, lon],
                radius=fixed_radius,
                fill=True,
                color=color,
                fill_color=color,
                fill_opacity=0.6,
                popup=popup
            ).add_to(m)
    color_map.add_to(m)
    return m

# Définir la mise en page de l'application
app.layout = html.Div([
    html.H1("MAP | Nombre d'accidents par départements en France"),  # Titre de la page
    dcc.Input(id='filter-input', type='number', value=0, debounce=True),
    html.Div(id='map-container')
])

# Mettre en place le rappel pour mettre à jour la carte
@app.callback(
    Output('map-container', 'children'),
    Input('filter-input', 'value')
)
def update_map_output(filter_value):
    updated_map = update_map(filter_value)
    return html.Iframe(srcDoc=updated_map.get_root().render(), width='700px', height='600px')

# Exécuter l'application
if __name__ == '__main__':
    app.run_server(debug=True)