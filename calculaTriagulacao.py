import math
import numpy as np
import pandas as pd
import folium

df = pd.read_csv('input.csv')
coordinates = []

def lat_lon_to_cartesian(latitude, longitude):
    R = 6371000
    x = R * math.radians(longitude)
    y = R * math.log(math.tan(math.pi/4 + math.radians(latitude)/2))
    return x, y

def ponto_interseccao_circulos(P1, P2, P3, dist_P1, dist_P2, dist_P3):
    
    A = 2 * (P2[0] - P1[0])
    B = 2 * (P2[1] - P1[1])
    C = dist_P1**2 - dist_P2**2 - P1[0]**2 + P2[0]**2 - P1[1]**2 + P2[1]**2
    D = 2 * (P3[0] - P2[0])
    E = 2 * (P3[1] - P2[1])
    F = dist_P2**2 - dist_P3**2 - P2[0]**2 + P3[0]**2 - P2[1]**2 + P3[1]**2

    x = (C*E - F*B) / (E*A - B*D)
    y = (C*D - A*F) / (B*D - A*E)

    return x, y

def cartesian_to_lat_lon(x, y):
    R = 6371000 
    latitude = math.degrees(2 * math.atan(math.exp(y / R)) - math.pi / 2)
    longitude = math.degrees(x / R)
    return latitude, longitude

def process_line(row):
    P1_lat_lon = (row['latitude_p1'], row['longitude_p1'])
    P2_lat_lon = (row['latitude_p2'], row['longitude_p2'])
    P3_lat_lon = (row['latitude_p3'], row['longitude_p3'])
    dist_P1 = row['dist_p1']
    dist_P2 = row['dist_p2']
    dist_P3 = row['dist_p3']

    P1_cartesian = lat_lon_to_cartesian(*P1_lat_lon)
    P2_cartesian = lat_lon_to_cartesian(*P2_lat_lon)
    P3_cartesian = lat_lon_to_cartesian(*P3_lat_lon)

    interseccao_cartesian = ponto_interseccao_circulos(P1_cartesian, P2_cartesian, P3_cartesian, dist_P1, dist_P2, dist_P3)

    interseccao_lat_lon = cartesian_to_lat_lon(*interseccao_cartesian)

    print("Ponto de interseção em latitude e longitude:", interseccao_lat_lon)
    latitude, longitude = interseccao_lat_lon
    coordinates.append((latitude, longitude)) 

def plot_points_on_map(coordinates):
    m = folium.Map(location=[0, 0], zoom_start=2)

    for coord in coordinates:
        folium.Marker(location=coord).add_to(m)

    m.save('mapa.html')

df.apply(process_line, axis=1)
plot_points_on_map(coordinates)






