import os
from pprint import pprint

import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("VTKEY")
headers = {
    "accept": "application/json"
}

site_to_check = input("Input domain name (example.com): ")
url = f"https://www.virustotal.com/vtapi/v2/domain/report"

params = {
    'apikey': api_key,
    'domain': site_to_check
}
response = requests.get(url, headers=headers, params=params)

pprint(response.json(), indent=4)