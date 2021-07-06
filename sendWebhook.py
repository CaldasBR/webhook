import requests
import json

webhook_url = 'http://167.71.84.108:5000/webhook'

header = {
    'Content-Type':'application/json'
}

data = {
  "ownerIdentity": "bancopanrouterhmg@msging.net",
  "identity": "315644c5-3eba-4b5e-9516-6de9d4e333a6.bancopanrouterhmg@0mn.io",
  "contact": {
    "Identity": "315644c5-3eba-4b5e-9516-6de9d4e333a6.bancopanrouterhmg@0mn.io"
  },
  "messageId": "cd60b7cb-d1e8-4585-90a7-b0e7e1b5e808",
  "storageDate": "2021-07-06T08:20:03.663Z",
  "category": "flow",
  "action": "[F.1.2.0] Transferring to Desk - Process input",
  "extras": {
    "stateId": "d29e6a8c-f2b6-4f2a-b9fc-571ba01145b3",
    "#stateName": "[F.1.2.0] Transferring to Desk - Process input",
    "#stateId": "d29e6a8c-f2b6-4f2a-b9fc-571ba01145b3",
    "#messageId": "cd60b7cb-d1e8-4585-90a7-b0e7e1b5e808",
    "#previousStateId": "d7b96154-4dfa-4286-adfc-b7a7e4fca41f",
    "#previousStateName": "[F.1.2.0] Show Confirmation to Transfer Menu"
  }
}

r = requests.post(webhook_url, data=json.dumps(data),headers=header)
