import dash
from dash.dependencies import Input, Output
from dash import dcc, html
import pandas as pd
import folium, branca
from folium import IFrame
import plotly.express as px  # Importez Plotly Express
import get_data
import caracteristique
import vehicule


# Obtenir les données pour l'histogramme
dict_obs = vehicule.get_data_vehicule()

# Obtenir les données pour les départements
coord_dict = get_data.get_dep()

# Obtenir les données pour la carte
nb_accidents_par_departement = caracteristique.get_data(1)

# Créer une application Dash
app = dash.Dash(__name__)

# Créer la carte Folium initiale
m = folium.Map(location=[46.603354, 1.888334], zoom_start=6)

# nombre minimum et maximum d'accidents pour créer la ligne de variation sur la map
min_accidents = min(nb_accidents_par_departement.values())
max_accidents = max(nb_accidents_par_departement.values())

color_map = branca.colormap.LinearColormap(['green', 'gold', 'orange', 'red'], vmin=min_accidents, vmax=max_accidents)

# Fonction pour mettre à jour la carte en fonction de la valeur du filtre
def update_map(filter_value):
    m = folium.Map(location=[46.603354, 1.888334], zoom_start=6)
    for departement, nb_accidents in nb_accidents_par_departement.items():
        if departement in coord_dict and nb_accidents > filter_value:
            lat, lon, name = coord_dict[departement]
            popup_html = f'<h8>{name} {departement}</h8><p>{nb_accidents} accidents</p>'
            iframe = IFrame(html=popup_html, width=100, height=100)
            popup = folium.Popup(iframe, max_width=200)
            color = color_map(nb_accidents)
            folium.CircleMarker(
                location=[lat, lon],
                radius=15,
                fill=True,
                color=color,
                fill_color=color,
                fill_opacity=0.6,
                popup=popup
            ).add_to(m)
    color_map.add_to(m)
    return m

# Mise en page de l'app
app.layout = html.Div([
    html.H1("Nombre d'accidents par départements en France"),  # Titre de la page
    dcc.Input(id='filter-input', type='number', value=0, debounce=True), # Ajoute un input pour filtrer la carte
    html.Div(id='map-container'),  # Ajoute un conteneur pour la carte
    dcc.Graph(id='map-histogram')  # Ajoute un composant pour l'histogramme
])

# Mise à jours de la carte et affichage de l'histogramme
@app.callback(
    [Output('map-container', 'children'), Output('map-histogram', 'figure')],
    Input('filter-input', 'value')
)

def update_map_output(filter_value):
    updated_map = update_map(filter_value)
    
    df = pd.DataFrame({'Type d\'accidents': list(dict_obs.keys()), 'Nombre d\'accidents': list(dict_obs.values())})

    # Créer un histogramme avec Plotly Express
    fig = px.bar(df, x='Type d\'accidents', y='Nombre d\'accidents', title='Nombre d\'accidents par type d\'accidents')
    
    # Retourne la mise en page avec la carte mise à jour et l'histogramme
    return html.Iframe(srcDoc=updated_map.get_root().render(), width='100%', height='600px'), fig

# Exécute l'application
if __name__ == '__main__':
    app.run_server(debug=True)
