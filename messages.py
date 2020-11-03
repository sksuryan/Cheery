import json
import requests

URL = 'https://wholesome-cheery-api.herokuapp.com'

def returnRandomMessage():
    data = requests.get(f'{URL}/get')
    data = json.loads(data.text)

    return data['message']

def addUserMessage(msg):
    data = requests.post(f'{URL}/post', json={'message': msg})