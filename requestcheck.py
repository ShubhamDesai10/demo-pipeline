import requests
from getapi import getApiURL


response = requests.get(getApiURL())

print(response)