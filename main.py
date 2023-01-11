import requests
import json
import pandas as pd

api_url = "https://www.boredapi.com/api/activity/"

response = requests.get(api_url)
activity = json.loads(response.text)["activity"]

print("Recommended Activity:",activity)

