import argparse

def specific(df):
    place = input("Choose a place of interest to see the nearest station: ")
    df = df.loc[df["place"] == place]
    return df

def argument_parser():
    parser = argparse.ArgumentParser(description= "Application for rent or park a bike in Madrid")
    help_message = "You have two options. Option 1: 'rent' gives you the nearest bicimad station. Option 2: 'park' gives you the nearest bicipark station."
    help_message2 = "The default option is to display"
    parser.add_argument("-f", "--function", help= help_message, type= str)
    parser.add_argument("-d", "--display", help=help_message2, type=str)
    args = parser.parse_args()
    return args