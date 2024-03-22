import requests
import pytz
from datetime import datetime

def get_public_ip():
    try:
        response = requests.get('https://api64.ipify.org?format=json')
        data = response.json()
        return data['ip']
    except Exception as e:
        return str(e)

import requests

# Replace 'YOUR_API_KEY' with your actual ipapi API key
api_key = 'YOUR_API_KEY'
url = f'http://api.ipapi.com/api/check?access_key={api_key}'

try:
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        current_ip = data['ip']
        print(f'Your current IP address is: {current_ip}')
    else:
        print(f'Error: {response.status_code}')
except Exception as e:
    print(f'An error occurred: {e}')
    

def read_lead():
    response = requests.get("https://api.leadid.com/SinglePreAudit?lac={ C5352934-D93D-AB9A-DFDC-F6820CE4B0BC }&lec={ B76E6CBB-1BD1-2698-6798-9023C8BF9539 }&id={ EC0C8691-75C7-BD90-28E1-0E0AD126E7DC }&format=json")
    response.raise_for_status()
    data = response.json()
    print(data)
# Get and print the public IP address
public_ip = get_public_ip()
print("Public IP Address:", public_ip)


"103.132.28.164"
"103.132.28.164"


def get_cst_time():
    pass 


def pennsylvania_time():
    et = pytz.timezone('US/Eastern')
    # Get the current time in ET
    current_time_et = datetime.now(et)
    # Format the current time as a string
    current_time_str = current_time_et.strftime('%Y-%m-%d %H:%M:%S %Z%z')
    print('Current Eastern Time (Pennsylvania):', current_time_str)
    return current_time_et
