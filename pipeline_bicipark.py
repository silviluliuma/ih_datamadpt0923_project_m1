##Imports

import pandas as pd 
import requests
import numpy as np

##Getting the data

bicipark = pd.read_csv("/data/raw/bicipark_stations.csv", sep=";")
places = requests.get("https://datos.madrid.es/egob/catalogo/300614-0-centros-educativos.json")

##Cleaning the data

split_bicipark = bicipark['geometry.coordinates'].str.strip('[]').str.split(',', expand=True).astype('float64')
split_bicipark.columns = ['longitude', 'latitude']
bicipark= pd.concat([bicipark,split_bicipark],axis=1)
bicipark = bicipark.drop(["Unnamed: 0","zip_code", "enabled", "reserved_places","geometry.type","geometry.coordinates"], axis=1)

places = places.json()
places = places["@graph"]
places = pd.json_normalize(places)
places = places.drop(["@id", "id", "relation", "address.district.@id", "address.area.@id", "address.locality", "address.postal-code", "organization.organization-desc", "organization.accesibility", "organization.schedule", "organization.services", "@type"], axis = 1)


##Operating the data

# La fórmula proporcionada no es eficiente. Vectorizando las operaciones da un resultado inmediato. 

def nearest_bicipark():
    data_list_bicipark = []
    
    """ Latitud y longitud a radianes para realizar las operaciones. Luego los convierto a numpy para evitar error. """ 

    places_lat_rad = np.radians(places['location.latitude'].to_numpy())
    places_lon_rad = np.radians(places['location.longitude'].to_numpy())
    bicipark_lat_rad = np.radians(bicipark['latitude'].to_numpy())
    bicipark_lon_rad = np.radians(bicipark['longitude'].to_numpy())

    dlat = bicipark_lat_rad[:, np.newaxis] - places_lat_rad
    dlon = bicipark_lon_rad[:, np.newaxis] - places_lon_rad

    """ Fórmula de Haversine para calcular las distancias. """ 
    
    a = np.sin(dlat / 2) ** 2 + np.cos(bicipark_lat_rad[:, np.newaxis]) * np.cos(places_lat_rad) * np.sin(dlon / 2) ** 2
    c = 2 * np.arcsin(np.sqrt(a))
    distance_matrix = c * 6371000 

    """ Cálculo del índice del resultado con menor distancia """

    min_distance_indices = np.argmin(distance_matrix, axis=0)

    """ Creación del dataframe del resultado utilizando ese índice"""

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

##Saving the data

result_bicipark = nearest_bicipark()
result_bicipark.to_csv("../data/results/result_bicipark.csv", index=False)