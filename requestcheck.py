import requests
from getapi import getApiURL
import json

def responseValidation():

    response = requests.get(getApiURL())

    return response.status_code

responseValidation()
