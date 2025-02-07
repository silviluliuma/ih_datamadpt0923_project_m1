import pandas as pd
import numpy as np

def nearest_bicimad(places, bicimad):
    data_list = []
    bicimad_lat_rad = np.radians(bicimad['latitude'].to_numpy())
    bicimad_lon_rad = np.radians(bicimad['longitude'].to_numpy())
    places_lat_rad = np.radians(places['location.latitude'].to_numpy())
    places_lon_rad = np.radians(places['location.longitude'].to_numpy())
    dlat = bicimad_lat_rad[:, np.newaxis] - places_lat_rad
    dlon = bicimad_lon_rad[:, np.newaxis] - places_lon_rad

    a = np.sin(dlat / 2) ** 2 + np.cos(bicimad_lat_rad[:, np.newaxis]) * np.cos(places_lat_rad) * np.sin(dlon / 2) ** 2
    c = 2 * np.arcsin(np.sqrt(a))
    distance_matrix = c * 6371000 

    min_distance_indices = np.argmin(distance_matrix, axis=0)

    for x in range(len(places["title"])):
        station_index = min_distance_indices[x]
        station = bicimad['name'].iloc[station_index]
        station_address = bicimad["address"].iloc[station_index]
        bikes_available = bicimad["dock_bikes"].iloc[station_index]
        station_id = bicimad["id"].iloc[station_index]
        place_address = places["address.street-address"][x]
        place = places["title"][x]
        min_distance = round(distance_matrix[station_index, x], 2)
        data_list.append({"place": place, "place_address": place_address, "station_name": station, "bikes_available": bikes_available, "station_id" : station_id, "station_address": station_address,  "distance": min_distance})
        
    return pd.DataFrame(data_list)

def nearest_bicipark(places, bicipark):
    data_list_bicipark = []
    bicipark_lat_rad = np.radians(bicipark['latitude'].to_numpy())
    bicipark_lon_rad = np.radians(bicipark['longitude'].to_numpy())
    places_lat_rad = np.radians(places['location.latitude'].to_numpy())
    places_lon_rad = np.radians(places['location.longitude'].to_numpy())
    dlat = bicipark_lat_rad[:, np.newaxis] - places_lat_rad
    dlon = bicipark_lon_rad[:, np.newaxis] - places_lon_rad

    
    a = np.sin(dlat / 2) ** 2 + np.cos(bicipark_lat_rad[:, np.newaxis]) * np.cos(places_lat_rad) * np.sin(dlon / 2) ** 2
    c = 2 * np.arcsin(np.sqrt(a))
    distance_matrix = c * 6371000 

    min_distance_indices = np.argmin(distance_matrix, axis=0)

    for x in range(len(places["title"])):
        station_index = min_distance_indices[x]
        station = bicipark['stationName'].iloc[station_index]
        station_address = bicipark["address"].iloc[station_index]
        spots_available = bicipark["free_places"].iloc[station_index]
        station_id = bicipark["stationId"].iloc[station_index]
        place_address = places["address.street-address"][x]
        place = places["title"][x]
        min_distance = round(distance_matrix[station_index, x], 2)
        data_list_bicipark.append({"place": place, "place_address": place_address, "station_name": station, "station_id" : station_id, "spots_available" : spots_available, "station_address": station_address,  "distance": min_distance})
        
    return pd.DataFrame(data_list_bicipark)

def fnearest_bicimad_realtime(places, df):
    data_list = []
    df = df.loc[df["dock_bikes"] > 0]
    places_lat_rad = np.radians(places['location.latitude'].to_numpy())
    places_lon_rad = np.radians(places['location.longitude'].to_numpy())
    bicimad_real_time_lat_rad = np.radians(df['latitude'].to_numpy())
    bicimad_real_time_lon_rad = np.radians(df['longitude'].to_numpy())
    dlat = bicimad_real_time_lat_rad[:, np.newaxis] - places_lat_rad
    dlon = bicimad_real_time_lon_rad[:, np.newaxis] - places_lon_rad

    a = np.sin(dlat / 2) ** 2 + np.cos(bicimad_real_time_lat_rad[:, np.newaxis]) * np.cos(places_lat_rad) * np.sin(dlon / 2) ** 2
    c = 2 * np.arcsin(np.sqrt(a))
    distance_matrix = c * 6371000 

    min_distance_indices = np.argmin(distance_matrix, axis=0)

    for x in range(len(places["title"])):
        station_index = min_distance_indices[x]
        station = df['name'].iloc[station_index]
        station_address = df["address"].iloc[station_index]
        bikes_available = df["dock_bikes"].iloc[station_index]
        station_id = df["id"].iloc[station_index]
        place_address = places["address.street-address"][x]
        place = places["title"][x]
        min_distance = round(distance_matrix[station_index, x], 2)
        data_list.append({"place": place, "place_address": place_address, "station_name": station, "bikes_available": bikes_available, "station_id" : station_id, "station_address": station_address,  "distance": min_distance})
        
    nearest_bicimad_realtime = pd.DataFrame(data_list)
    return nearest_bicimad_realtime

def fnearest_bicimad_realtime_parking(places, df):
    data_list = []
    df = df[df["free_bases"] > 0]
    bicimad_real_time_lat_rad = np.radians(df['latitude'].to_numpy())
    bicimad_real_time_lon_rad = np.radians(df['longitude'].to_numpy())
    places_lat_rad = np.radians(places['location.latitude'].to_numpy())
    places_lon_rad = np.radians(places['location.longitude'].to_numpy())
    dlat = bicimad_real_time_lat_rad[:, np.newaxis] - places_lat_rad
    dlon = bicimad_real_time_lon_rad[:, np.newaxis] - places_lon_rad

    a = np.sin(dlat / 2) ** 2 + np.cos(bicimad_real_time_lat_rad[:, np.newaxis]) * np.cos(places_lat_rad) * np.sin(dlon / 2) ** 2
    c = 2 * np.arcsin(np.sqrt(a))
    distance_matrix = c * 6371000 

    min_distance_indices = np.argmin(distance_matrix, axis=0)

    for x in range(len(places["title"])):
        station_index = min_distance_indices[x]
        station = df['name'].iloc[station_index]
        station_address = df["address"].iloc[station_index]
        free_bases = df["free_bases"].iloc[station_index]
        station_id = df["id"].iloc[station_index]
        place_address = places["address.street-address"][x]
        place = places["title"][x]
        min_distance = round(distance_matrix[station_index, x], 2)
        data_list.append({"place": place, "place_address": place_address, "station_name": station, "free_bases": free_bases, "station_id" : station_id, "station_address": station_address,  "distance": min_distance})
        
    return pd.DataFrame(data_list)