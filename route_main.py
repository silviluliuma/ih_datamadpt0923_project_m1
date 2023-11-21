#Imports 
import requests
import json
import os
from dotenv import load_dotenv
import pandas as pd
import folium
import openrouteservice as ors
from geopy.distance import great_circle
from modules import route
from modules import argparse_route

stations_real_time = route.get_stations()

def main():
    args = argparse_route.argument_parser()
    if args.district:
        m = route.get_route_map(stations_real_time, args.district)
        m.save(f"./data/maps/ROUTE_MAP_{args.district}_DISTRICT.html")
    else:
        x = input("What district have you been assigned to today? ")
        m = route.get_route_map(stations_real_time, x)
        m.save(f"./data/maps/ROUTE_MAP_{x}_DISTRICT.html")

if __name__ == "__main__":
    main()