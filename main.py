import pandas as pd 
import requests
import numpy as np

from modules import functions
from modules import argparse

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

def main():
    BICIMAD_RESULT = functions.nearest_bicimad(places, bicimad) 
    BICIMAD_RESULT.to_csv("./data/results/BICIMAD_RESULT.csv")
    BICIPARK_RESULT = functions.nearest_bicipark(places, bicipark)
    BICIPARK_RESULT.to_csv("./data/results/BICIPARK_RESULT.csv")

if __name__ == "__main__":
    main()