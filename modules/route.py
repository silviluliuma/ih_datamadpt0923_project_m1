#Imports 

import requests
import json
import os
from dotenv import load_dotenv
import pandas as pd
import folium
import openrouteservice as ors
from geopy.distance import great_circle
from folium.features import DivIcon

def get_token():
    load_dotenv('../.env')
    email = os.environ.get("email")
    password = os.environ.get("password")
    url = "https://openapi.emtmadrid.es/v3/mobilitylabs/user/login/"
    headers = {"email": email, "password" : password}
    response = requests.get(url, headers=headers)
    return response.content

def get_stations():
    load_dotenv('./.env')
    token = os.environ.get("access_token")
    url = "https://openapi.emtmadrid.es/v3/transport/bicimad/stations/"
    headers = {"accessToken" : token}
    response = requests.get(url, headers = headers).json()
    stations_real_time = pd.DataFrame(response["data"])
    stations_real_time[["longitude", "latitude"]] = stations_real_time["geometry"].apply(lambda x: pd.Series(x["coordinates"]))
    stations_real_time = stations_real_time.drop(["geofence", "activate", "geometry", "integrator", "reservations_count", "no_available", "tipo_estacionPBSC", "virtualDelete", "virtual_bikes", "virtual_bikes_num", "code_suburb", "geofenced_capacity", "bikesGo"], axis=1)
    stations_real_time['coordinates'] = list(zip(stations_real_time['longitude'], stations_real_time['latitude']))
    return stations_real_time

def get_district(df, district_number):
    result = df[df["code_district"] == str(district_number)]
    return result

def get_light1(df):
    df_light1 = df[df["light"]==1]
    return df_light1

def get_light0(df):
    df_light0 = df[df["light"]==0]
    return df_light0

def find_nearest_to_coords(df, coords):
    station_coordinates = df['coordinates'].tolist()
    nearest_station = min(station_coordinates, key=lambda coord: great_circle(coord, coords).meters)
    return nearest_station

def create_route(client, start_coords, end_coords):
    return client.directions(
        coordinates=[start_coords, end_coords],
        profile='driving-car',
        format='geojson'
    )

def number_DivIcon(color,number):
    icon = DivIcon(
            icon_size=(150,36),
            icon_anchor=(20,40),
            html = """<span class="fa-stack" style="font-size: 12pt; display: inline-block; position: relative;">
    <span class="fa fa-circle-o fa-stack-2x" style="color: {:s};"></span>
    <strong class="fa-stack-1x" style="line-height: 36px; color: black; position: absolute; width: 100%; text-align: center;">{:02d}</strong>
</span>""".format(color, number))
    return icon

def get_route_map(stations_real_time, number_district):
    load_dotenv('../.env')
    client = ors.Client(key=os.environ.get("openroute_api_key"))
    vehicle_start = [-3.6823731969472644, 40.46209827032537]
    m = folium.Map(location=[vehicle_start[1], vehicle_start[0]], zoom_start=12)
    folium.Marker(location=[vehicle_start[1], vehicle_start[0]], popup='CENTRAL EMT', icon=folium.Icon(color='purple')).add_to(m)
    distrito_low= get_light0(get_district(stations_real_time, number_district)).copy()
    distrito_high= get_light1(get_district(stations_real_time, number_district)).copy()
    distrito_low["visited"] = False
    distrito_high["visited"] = False
    current_coords = vehicle_start
    van = "empty"
    coords_list = [current_coords]
    stop_counter = 1 
    for i in range(100):
        if van == "empty":
            current_coords = coords_list[-1]
            if not distrito_high.loc[~distrito_high['visited'] & (distrito_high['light'] == 1)].empty:
                nearest_station = find_nearest_to_coords(distrito_high.loc[~distrito_high['visited'] & (distrito_high['light'] == 1)], current_coords)
                coords_list.append(nearest_station)
                distrito_high.loc[distrito_high['coordinates'] == nearest_station, 'visited'] = True
                distrito_high.loc[distrito_high['coordinates'] == nearest_station, 'light'] = 2
                route = create_route(client, coords_list[-2], coords_list[-1])
                van = "full"
                folium.Marker(
                                location=[nearest_station[1], nearest_station[0]],
                                popup=f"Station with high occupation\nNumber: {stop_counter}",
                                icon=folium.Icon(color='orange',icon_color='orange'),
                            ).add_to(m)
                folium.Marker(location=[nearest_station[1], nearest_station[0]],
                            icon= number_DivIcon("#C55A11", stop_counter)).add_to(m)
                stop_counter += 1
                folium.PolyLine(locations=[coord[::-1] for coord in route['features'][0]['geometry']['coordinates']],
                                color='red').add_to(m)
        elif van == "full":
            current_coords = coords_list[-1]
            if not distrito_low.loc[~distrito_low['visited'] & (distrito_low['light'] == 0)].empty:
                nearest_station = find_nearest_to_coords(distrito_low.loc[~distrito_low['visited'] & (distrito_low['light'] == 0)], current_coords)
                coords_list.append(nearest_station)
                distrito_low.loc[distrito_low['coordinates'] == nearest_station, 'visited'] = True
                distrito_low.loc[distrito_low['coordinates'] == nearest_station, 'light'] = 2
                route = create_route(client, coords_list[-2], coords_list[-1])
                van = "empty"
                folium.Marker(location=[nearest_station[1], nearest_station[0]],
                            popup=f"Station with low occupation\nNumber: {stop_counter}",
                            icon=folium.Icon(color='darkgreen', icon_color='green')).add_to(m)
                folium.Marker(location=[nearest_station[1], nearest_station[0]],
                              icon = number_DivIcon("#12A14B", stop_counter)).add_to(m)
                stop_counter += 1
                folium.PolyLine(locations=[coord[::-1] for coord in route['features'][0]['geometry']['coordinates']],
                                color='red').add_to(m)
    final_route = create_route(client, coords_list[-1], vehicle_start)
    folium.PolyLine(locations=[coord[::-1] for coord in final_route['features'][0]['geometry']['coordinates']],
                                color='red').add_to(m)

    return m   
