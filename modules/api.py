import requests
import json
import os
from dotenv import load_dotenv
import pandas as pd
import numpy as np

def get_token():
    load_dotenv('./.env')
    email = os.environ.get("email")
    password = os.environ.get("password")
    url = "https://openapi.emtmadrid.es/v3/mobilitylabs/user/login/"
    headers = {"email": email, "password" : password}
    response = requests.get(url, headers=headers)
    return response.content

def get_available_bikes():
    load_dotenv('./.env')
    token = os.environ.get("access_token")
    url = "https://openapi.emtmadrid.es/v3/transport/bicimad/stations/"
    headers = {"accessToken" : token}
    response = requests.get(url, headers = headers).json()
    return response