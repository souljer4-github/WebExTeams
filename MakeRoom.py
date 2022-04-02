import requests
import json
from getpass import getpass
from pprint import pprint

TOKEN = input('Please paste your token: ')

BASEURL = "https://webexapis.com"
room = "/v1/rooms"

body = {
    'title': 'Jason\'s Room'
}
bodyJSON = json.dumps(body)

headers = {
    'Authorization': 'Bearer ' + TOKEN,
    'content-Type': 'application/json'
}
createRoom = BASEURL + room
response = requests.post(createRoom, headers=headers, data=bodyJSON)
responseJSON = response.json()
pprint(responseJSON)

