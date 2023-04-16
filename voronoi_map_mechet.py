import pandas as pd
import folium
from folium.plugins import MarkerCluster
from scipy.spatial import Voronoi
from geopy import distance
import math


def geodesic_area(points):
    area = 0
    for i in range(len(points)):
        j = (i + 1) % len(points)
        lat1, lon1 = points[i]
        lat2, lon2 = points[j]
        area += (lon2 - lon1) * (2 + 
            math.sin(math.radians(lat1)) + 
            math.sin(math.radians(lat2))) 
    area = area * 6378137.0 
    area = area * 57113.6363/1000000
    return abs(area)


data1 = pd.read_excel('doner.xlsx')
data1.drop_duplicates(subset=['latitude', 'longitude'], inplace=True)


vor = Voronoi(data1[['latitude', 'longitude']].values)

# Set the boundaries for the map
min_lat = data1['latitude'].min()
max_lat = data1['latitude'].max()
min_lon = data1['longitude'].min()
max_lon = data1['longitude'].max()


m = folium.Map(location=[data1['latitude'].mean(), data1['longitude'].mean()], 
               zoom_start=10, 
               max_bounds=True)


mc1 = folium.plugins.MarkerCluster(name='Data 1')
for index, row in data1.iterrows():
    folium.CircleMarker(location=[row['latitude'], row['longitude']], radius=5,
                        popup=row['name'], fill=True, color='blue').add_to(mc1)


m.add_child(mc1)


for i, region in enumerate(vor.regions):
    if len(region) > 2 and all(index >= 0 for index in region):
        polygon = [vor.vertices[i] for i in region]
        polygon_area = geodesic_area(polygon)
        folium.Polygon(locations=polygon, color='orange', fill_color='orange', tooltip=f"Area: {polygon_area:.2f} km²").add_to(m)


folium.TileLayer('Stamen Toner').add_to(m)
folium.TileLayer('Stamen Terrain').add_to(m)
folium.TileLayer('Stamen Water Color').add_to(m)
folium.TileLayer('cartodbpositron').add_to(m)
folium.TileLayer('cartodbdark_matter').add_to(m)
folium.LayerControl().add_to(m)


m.save('voronoi_map_donerki.html')
