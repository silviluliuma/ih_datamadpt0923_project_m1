import requests
import json
import os
from dotenv import load_dotenv
import pandas as pd

def get_token():
    load_dotenv('../.env')
    email = os.environ.get("email")
    password = os.environ.get("password")
    url = "https://openapi.emtmadrid.es/v3/mobilitylabs/user/login/"
    headers = {"email": email, "password" : password}
    response = requests.get(url, headers=headers)
    return response.content

get_token()

def get_available_bikes():
    load_dotenv('../.env')
    token = os.environ.get("access_token")
    url = f"https://openapi.emtmadrid.es/v3/transport/bicimad/stations/"
    headers = {"accessToken" : token}
    response = requests.get(url, headers = headers).json()
    return response

get_available_bikes()