import argparse
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

""" Fórmula para coger un único lugar del dataset con su información. 
    Se utiliza fuzzywuzzy para que el input del user no tenga que ser 100% exacto."""

def specific(df):
    place = input("Choose a place of interest to see the nearest station: ")
    df_filtered = df[df["place"].apply(lambda x: fuzz.WRatio(place, x) >= 90)]
    if not df_filtered.empty:
        return df_filtered
    else:
        return "We haven't found a similar location..."

def argument_parser():
    parser = argparse.ArgumentParser(description= "Application for rent or park a bike in Madrid")
    help_message = "You have two options. Option 1: 'rent' gives you the nearest bicimad station with bikes available for rent. Option 2: 'park' gives you the nearest bicimad station with free bases available."
    help_message2 = "You have two options. Option 1: 'one' gives you the nearest bicimad station from a selected place of interest. Option 2: 'all' gives you a whole table with bicimad stations near a given number of selected places of interest."
    help_message3 = "You have two options. Option 1: 'bicimad' operates on bicimad stations. Option 2: 'bicipark' operates on bicipark stations."
    parser.add_argument("-a", "--app", help=help_message3, type=str)
    parser.add_argument("-d", "--display", help=help_message2, type=str)
    parser.add_argument("-f", "--function", help= help_message, type= str)
    args = parser.parse_args()
    return args