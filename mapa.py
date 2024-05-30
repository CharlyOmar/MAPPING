import folium
import pandas

data = pandas.read_csv("volcanoes.txt")
lon = list(data["LON"])
lat = list(data["LAT"])
elev = list(data["ELEV"])

def color_volcanoe(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[24.02, -104.67], zoom_start=6, tiles = "OpenStreetMap")

fgv = folium.FeatureGroup(name="Volcanes")

for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius=7, popup=str(el)+" mts", fill_color=color_volcanoe(el), color='grey', fill_opacity=0.7))

fgp = folium.FeatureGroup(name="Población")

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 200000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Mapa.html")