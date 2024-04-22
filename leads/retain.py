import requests 
import json

def retain(cert_url, email):
    if not cert_url.startswith('https://cert.trustedform.com'):
        print("URL must start with https://cert.trustedform.com")
        return  None
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    auth = ('API', 'f23d0ce6b443fd8ba97f92183af961d5')
    data = {
    "match_lead" : {
        "email": f"{email}"
    },
    "retain": {
        "reference": f"{email}",
        "vendor": "Mass Tort Hub"
    }
    }
    response = requests.post(cert_url, headers=headers, auth=auth, data=json.dumps(data))
    if response.status_code == 200:
        print("Retain successful")
        data = response.json()
        return data
    else:
        return None