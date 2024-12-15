import requests
import datetime
import os

PIXELA_ENDPOINT = os.getenv("PIXELA_ENDPOINT")
USER_NAME = os.getenv("USER_NAME")
TOKEN = os.getenv("TOKEN")
GRAPH_ID = "graph1"

user_parameters = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

''' 
response = requests.post(url=PIXELA_ENDPOINT, json=user_parameters)
# Response is already posted, that means a user with our username is created
This code should only be run once (for creating the user)
'''

GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USER_NAME}/graphs"

graph_configuration = {
    'id': GRAPH_ID,
    'name': 'Coding Graph',
    'unit': 'minutes',
    'type': 'int',
    'color': 'shibafu'
}

# Headers are used to give information like api key, so that they wont be visible
headers = {
    "X-USER-TOKEN": TOKEN
}

'''
response = requests.post(url=GRAPH_ENDPOINT, json=graph_configuration, headers=headers)
Graph is already created using this end point
This code should only be run once (for creating the graph)
'''

PIXELA_CREATION_ENDPOINT = f"{PIXELA_ENDPOINT}/{USER_NAME}/graphs/{GRAPH_ID}"

pixel_data = {
    "date": ''.join(map(str, (str(datetime.datetime.now()).split(" ")[0]).split("-"))),  # This expression returns today's date as a string "YYYYMMDD"
    "quantity": "120"
}

'''
response = requests.post(url=PIXELA_CREATION_ENDPOINT, json=pixel_data, headers=headers)
print(response.text)
This data is already posted
'''
today = ''.join(map(str, (str(datetime.datetime.now()).split(" ")[0]).split("-")))

UPDATION_ENDPOINT = f"{PIXELA_ENDPOINT}/{USER_NAME}/graphs/{GRAPH_ID}/{today}"

updated_pixel_data = {
    "date": ''.join(map(str, (str(datetime.datetime.now()).split(" ")[0]).split("-"))),  # This expression returns today's date as a string "YYYYMMDD"
    "quantity": "60"
}

'''
response = requests.put(url=PIXELA_CREATION_ENDPOINT, json=updated_pixel_data, headers=headers)
print(response.text)
This response has already been updated
'''

DELETION_ENDPOINT = UPDATION_ENDPOINT

response = requests.delete(url=DELETION_ENDPOINT, headers=headers)
print(response.text)
