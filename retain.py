import requests
import json

def send_trustedform_request(cert_url, email):
    if not url.startswith('https://cert.trustedform.com'):
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
    }
    response = requests.post(cert_url, headers=headers, auth=auth, data=json.dumps(data))
    if response.status_code == 200:
        print("Request successful")
        data = response.json()
        return data
    else:
        return None

# Example usage
url = 'https://cert.trustedform.com/25929dd366aceba47dec38a9aed4ccc509aafbef'

result = send_trustedform_request(url, email="john@gmail.com")
if result is not None:
    print("Response:", result)
