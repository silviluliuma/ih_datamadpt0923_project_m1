##IMPORTS

import pandas as pd 
import requests
import numpy as np

##Getting the data

bicimad = pd.read_csv("/data/raw/bicimad_stations.csv", sep="\t")
places = requests.get("https://datos.madrid.es/egob/catalogo/300614-0-centros-educativos.json")

##Cleaning the data

split_bicimad = bicimad['geometry.coordinates'].str.strip('[]').str.split(',', expand=True).astype('float64')
split_bicimad.columns = ['longitude', 'latitude']
bicimad= pd.concat([bicimad,split_bicimad],axis=1)
bicimad = bicimad.drop(["Unnamed: 0", "geometry.coordinates", "light", "number", "activate", "no_available", "geometry.type"], axis = 1) 

places = places.json()
places = places["@graph"]
places = pd.json_normalize(places)
places = places.drop(["@id", "id", "relation", "address.district.@id", "address.area.@id", "address.locality", "address.postal-code", "organization.organization-desc", "organization.accesibility", "organization.schedule", "organization.services", "@type"], axis = 1)


##Operating the data

# La fórmula proporcionada no es eficiente. Vectorizando las operaciones da un resultado inmediato. 

def nearest_bicimad():
    data_list = []
    
    """ Latitud y longitud a radianes para realizar las operaciones. Luego los convierto a numpy para evitar error. """ 

    places_lat_rad = np.radians(places['location.latitude'].to_numpy())
    places_lon_rad = np.radians(places['location.longitude'].to_numpy())
    bicimad_lat_rad = np.radians(bicimad['latitude'].to_numpy())
    bicimad_lon_rad = np.radians(bicimad['longitude'].to_numpy())

    dlat = bicimad_lat_rad[:, np.newaxis] - places_lat_rad
    dlon = bicimad_lon_rad[:, np.newaxis] - places_lon_rad

    """ Fórmula de Haversine para calcular las distancias. """ 
    
    a = np.sin(dlat / 2) ** 2 + np.cos(bicimad_lat_rad[:, np.newaxis]) * np.cos(places_lat_rad) * np.sin(dlon / 2) ** 2
    c = 2 * np.arcsin(np.sqrt(a))
    distance_matrix = c * 6371000 

    """ Cálculo del índice del resultado con menor distancia """

    min_distance_indices = np.argmin(distance_matrix, axis=0)

    """ Creación del dataframe del resultado utilizando ese índice"""

    for x in range(len(places["title"])):
        station_index = min_distance_indices[x]
        station = bicimad['name'].iloc[station_index].split('- ')[1]
        station_address = bicimad["address"].iloc[station_index]
        place_address = places["address.street-address"][x]
        place = places["title"][x]
        min_distance = round(distance_matrix[station_index, x], 2)
        data_list.append({"place": place, "place_address": place_address, "station_name": station, "station_address": station_address,  "distance": min_distance})
        
    return pd.DataFrame(data_list)

##Saving the data

result_bicimad = nearest_bicimad()
result_bicimad.to_csv("../data/results/result_bicimad.csv", index=False)

