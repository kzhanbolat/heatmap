import pandas as pd
import folium
from folium.plugins import MarkerCluster
from scipy.spatial import Voronoi
from geopy import distance
import math


def voronoi(data1):
    # print("vornoi function first step")
    import pandas as pd
    import folium
    from folium.plugins import MarkerCluster
    from scipy.spatial import Voronoi
    from geopy import distance
    import math
    from shapely.geometry import Polygon


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

    data1['latitude'] = data1['latitude'].astype(float)
    data1['longitude'] = data1['longitude'].astype(float)
    # data1 = pd.read_excel('jusan_atm_all.xlsx')
    # data2 = pd.read_excel('kaspi_all.xlsx')
    # data3 = pd.read_excel('halyk_all.xlsx')
    # data4 = pd.read_excel('all_atms_kz.xlsx')
    data1.drop_duplicates(subset=['latitude', 'longitude'], inplace=True)
    # data2.drop_duplicates(subset=['latitude', 'longitude'], inplace=True)
    # data3.drop_duplicates(subset=['latitude', 'longitude'], inplace=True)
    # data4.drop_duplicates(subset=['latitude', 'longitude'], inplace=True)

    vor = Voronoi(data1[['latitude', 'longitude']].values, furthest_site=False)


    # print("vornoi function second step")
    boundary = Polygon([(41.321416, 45.719719), 
                        (52.030452, 47.581617), (51.317477, 59.203303), (54.211706, 60.881301), (55.640020, 69.488807), (54.573547, 77.319462), (51.569261, 80.147199), 
                        (49.561840, 87.397408), (42.196627, 80.261853), (42.974490, 74.109195), (42.311627, 73.518789),
                        (40.470162, 68.578018), (41.734613, 65.750438), (43.449110, 64.937450), (43.385269, 61.905224), (45.394765, 58.587353), (44.467937, 56.853179),
                        (41.067759, 55.834769),
                        (42.231291, 54.040979), (41.699882, 52.425130)
                        ])

    m = folium.Map(location=[data1['latitude'].mean(), data1['longitude'].mean()], 
                zoom_start=10, 
                max_bounds=True)

    # print("vornoi function third step")
    mc1 = MarkerCluster(name='Jusan', options={'disableClusteringAtZoom': 12})
    for index, row in data1.iterrows():
        folium.CircleMarker(location=[row['latitude'], row['longitude']], radius=5,
                            popup=row['name'], fill=True, color='blue').add_to(mc1)

    # mc2 =  MarkerCluster(name='kaspi', options={'disableClusteringAtZoom': 12})
    # for index, row in data2.iterrows():
    #     folium.CircleMarker(location=[row['latitude'], row['longitude']], radius=5,
    #                         popup=row['name'], fill=True, color='red').add_to(mc2)

    # mc3 =  MarkerCluster(name='Halyk', options={'disableClusteringAtZoom': 12})
    # for index, row in data3.iterrows():
    #     folium.CircleMarker(location=[row['latitude'], row['longitude']], radius=5,
    #                         popup=row['name'], fill=True, color='green').add_to(mc3)

    # mc4 =  MarkerCluster(name='Others', options={'disableClusteringAtZoom': 12})
    # for index, row in data4.iterrows():
    #     folium.CircleMarker(location=[row['latitude'], row['longitude']], radius=5,
    #                         popup=row['name'], fill=True, color='black').add_to(mc4)
        
    m.add_child(mc1)
    # m.add_child(mc2)
    # m.add_child(mc3)
    # m.add_child(mc4)

    # print("vornoi function fourth step")
    for i, region in enumerate(vor.regions):
        if len(region) > 2 and all(index >= 0 for index in region):  
            polygon = [vor.vertices[i] for i in region]
            polygon_area = geodesic_area(polygon)   
            polygon = Polygon(polygon)
            polygon = polygon.intersection(boundary)  # Clip the polygon to the boundary       
            if not polygon.is_empty:
                folium.Polygon(locations=list(polygon.exterior.coords), color='orange', fill_color='orange', tooltip=f"Area: {polygon_area:.2f} km²").add_to(m)


    folium.TileLayer('Stamen Toner').add_to(m)
    folium.TileLayer('Stamen Terrain').add_to(m)
    folium.TileLayer('Stamen Water Color').add_to(m)
    folium.TileLayer('cartodbpositron').add_to(m)
    folium.TileLayer('cartodbdark_matter').add_to(m)
    folium.LayerControl().add_to(m)

    # print("vornoi function fifth step")
    m.save('static/voronoi_generated.html')







