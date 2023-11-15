import pandas as pd 
import requests
import numpy as np

from modules import functions
from modules import argparse
from modules import api

from fuzzywuzzy import fuzz
from fuzzywuzzy import process

#bicimad
bicimad = pd.read_csv("./data/raw/bicimad_stations.csv", sep="\t")
split_bicimad = bicimad['geometry.coordinates'].str.strip('[]').str.split(',', expand=True).astype('float64')
split_bicimad.columns = ['longitude', 'latitude']
bicimad= pd.concat([bicimad,split_bicimad],axis=1)
bicimad = bicimad.drop(["Unnamed: 0", "geometry.coordinates", "light", "number", "activate", "no_available", "geometry.type"], axis = 1) 

#bicipark
bicipark = pd.read_csv("./data/raw/bicipark_stations.csv", sep=";")
split_bicipark = bicipark['geometry.coordinates'].str.strip('[]').str.split(',', expand=True).astype('float64')
split_bicipark.columns = ['longitude', 'latitude']
bicipark= pd.concat([bicipark,split_bicipark],axis=1)
bicipark = bicipark.drop(["Unnamed: 0","zip_code", "enabled", "reserved_places","geometry.type","geometry.coordinates"], axis=1)

#places
places = requests.get("https://datos.madrid.es/egob/catalogo/300614-0-centros-educativos.json")
places = places.json()
places = places["@graph"]
places = pd.json_normalize(places)
places = places.drop(["@id", "id", "relation", "address.district.@id", "address.area.@id", "address.locality", "address.postal-code", "organization.organization-desc", "organization.accesibility", "organization.schedule", "organization.services", "@type"], axis = 1)

data_bikes = api.get_available_bikes()
bicimad_real_time = pd.DataFrame(data_bikes["data"])
bicimad_real_time[["longitude", "latitude"]] = bicimad_real_time["geometry"].apply(lambda x: pd.Series(x["coordinates"]))
bicimad_real_time = bicimad_real_time.drop(["geofence", "integrator", "reservations_count", "tipo_estacionPBSC", "virtual_bikes", "virtual_bikes_num", "code_district", "code_suburb", "bikesGo", "geometry", "light", "no_available", "number", "virtualDelete", "geofenced_capacity"], axis = 1)

def main():
    if argparse.argument_parser().app=="bicimad":
        if argparse.argument_parser().display == "one":
            if argparse.argument_parser().function == "rent":
                BICIMAD_RESULT = functions.fnearest_bicimad_realtime(places, bicimad_real_time)
                RESULT = argparse.specific(BICIMAD_RESULT)
                RESULT.to_csv("./data/results/BICIMAD_ONE_RESULT.csv")
            elif argparse.argument_parser().function == "park":
                BICIPARK_RESULT = functions.fnearest_bicimad_realtime_parking(places, bicimad_real_time)
                RESULT = argparse.specific(BICIPARK_RESULT)
                RESULT.to_csv("./data/results/BICIMAD_PARKING_ONE_RESULT.csv")
        elif argparse.argument_parser().display == "all":
            if argparse.argument_parser().function == "rent":
                BICIMAD_RESULT = functions.fnearest_bicimad_realtime(places, bicimad_real_time) 
                BICIMAD_RESULT.to_csv("./data/results/BICIMAD_RESULT.csv")
            elif argparse.argument_parser().function == "park":
                BICIPARK_RESULT = functions.fnearest_bicimad_realtime_parking(places, bicimad_real_time)
                BICIPARK_RESULT.to_csv("./data/results/BICIMAD_PARKING_RESULT.csv")
    elif argparse.argument_parser().app == "bicipark":
        if argparse.argument_parser().display == "one":
            BICIPARK_RESULT = functions.nearest_bicipark(places, bicipark)
            RESULT = argparse.specific(BICIPARK_RESULT)
            RESULT.to_csv("./data/results/BICIPARK_ONE_RESULT.csv")
        elif argparse.argument_parser().display == "all":
            BICIPARK_RESULT = functions.nearest_bicipark(places, bicipark)
            BICIPARK_RESULT.to_csv("./data/results/BICIPARK_RESULT.csv")


if __name__ == "__main__":
    main()