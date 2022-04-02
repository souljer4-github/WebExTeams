import requests
import json
from getpass import getpass
from pprint import pprint

TOKEN = input('Please paste your token: ')

BASEURL = "https://webexapis.com"
room = "/v1/rooms"

body = {}


headers = {
    'Authorization': 'Bearer ' + TOKEN,
    'content-Type': 'application/json'
}
getrooms = BASEURL + room
response = requests.get(getrooms, headers=headers, data=body)
responseJSON = response.json()
pprint(responseJSON)

