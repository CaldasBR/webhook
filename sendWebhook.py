import requests
import json

webhook_url = 'http://167.71.84.108:5000/webhook'

header = {
    'Content-Type':'application/json'
}

data = {
    'name':'Filipe Caldas'
    ,'channel URL': 'Test URL externa'
}

r = requests.post(webhook_url, data=json.dumps(data),headers=header)
