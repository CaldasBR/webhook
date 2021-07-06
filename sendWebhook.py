import requests
import json

webhook_url = 'http://167.71.84.108:5000/webhook'

header = {
    'Content-Type':'application/json'
}

data = {
    "type":"text/plain"
    ,"content":"aloooo"
    ,"id":"bc86a5ad-b847-4872-bf46-64c0356b716c"
    ,"from":"315644c5-3eba-4b5e-9516-6de9d4e333a6.bancopanrouterhmg@0mn.io/default"
    ,"to":"bancopanrouterhmg@msging.net"
    ,"metadata":{
        "#uniqueId":"c2a7c016-e1a5-4122-8ddf-e9cf24def049"
        ,"date_created":"1625559617643"
        ,"uber-trace-id":"24cabc654458601e%3A24cabc654458601e%3A0%3A1"
        ,"#envelope.storageDate":"2021-07-06T08:20:17Z"
    }
}

r = requests.post(webhook_url, data=json.dumps(data),headers=header)
