import requests
import json

webhook_url = 'http://127.0.0.1:5000/webhook'

header = {
    'Content-Type':'application/json'
}

data = {
    'name':'Filipe Caldas'
    'channel URL': 'Test URL'
}

r = requests.post(webhook_url, data=json.dumps(data),headers=json.dumps(header))
