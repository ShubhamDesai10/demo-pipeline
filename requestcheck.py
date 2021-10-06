import re
import requests
from getapi import getApiURL

def responseValidation():

    response = requests.get(getApiURL())

    return response.status_code

responseValidation()
