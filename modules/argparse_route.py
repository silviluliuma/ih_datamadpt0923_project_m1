import argparse
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

def argument_parser():
    parser = argparse.ArgumentParser(description= "This application provides each biciMAD worker with a route for the district assigned to them.")
    help_message = "You have to select the district assigned to you today. Remember to enter the input with the format '01'."
    parser.add_argument("-d", "--district", help=help_message, type=str)
    args = parser.parse_args()
    return args