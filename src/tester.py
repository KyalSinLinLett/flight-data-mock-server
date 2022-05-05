import requests
import json
import time

while True:
    result = requests.get("http://localhost:5000/departure").json()
    print(json.dumps(result)[:100])
    time.sleep(15)