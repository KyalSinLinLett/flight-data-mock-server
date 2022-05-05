import flask
from flask import jsonify
import requests
import time
import random
import json
import os.path
from os import path
from decouple import config

app = flask.Flask(__name__)
app.config["DEBUG"] = True

RT_FLIGHT_ENDPOINT_URL = config("RT_FLIGHT_ENDPOINT_URL")
ACCESS_KEY = config("ACCESS_KEY")
TARGET_AIRPORT = config("TARGET_AIRPORT")
ARRIVAL_QUERY = config("ARRIVAL_QUERY")
DEPARTURE_QUERY = config("DEPARTURE_QUERY")

######################
# getting flight data
def get_flight_data():
    """
    Fetches realtime flight data at every 60s intervals and returns a list of flight data
    """
    
    count = 0

    while (count < 5):
        print("getting arrival data " + str(count))
        arr_result = requests.get(RT_FLIGHT_ENDPOINT_URL + ARRIVAL_QUERY).json()
        print("getting departure data " + str(count))
        dep_result = requests.get(RT_FLIGHT_ENDPOINT_URL + DEPARTURE_QUERY).json()

        if (arr_result and dep_result):
            arr_content = json.dumps(arr_result)
            print("Arrival Content:", arr_content[:100])
            with open('./arrivals.json', "a") as f:
                f.write(arr_content if count == 4 else arr_content + "\n")
                f.close()

            dep_content = json.dumps(dep_result)
            print("Departure Content:", dep_content[:100])
            with open('./departure.json', "a") as f:
                f.write(dep_content if count == 4 else dep_content + "\n")
                f.close()
            
        time.sleep(60)
        count += 1
    
######################

if not (os.path.exists('./departure.json') or os.path.exists('./arrivals.json')):
    flight_data = get_flight_data()

@app.route('/arrival', methods=['GET'])
def arrival():
    arrival_data = []
    with open("./arrivals.json", "r") as f:
        for arr_content in f.readlines():
            arrival_data.append(json.loads(arr_content))
        f.close()

    print(len(arrival_data))

    return jsonify(arrival_data[random.randrange(0, 4, 1)])

@app.route('/departure', methods=['GET'])
def departure():
    departure_data = []
    with open("./departure.json", "r") as f:
        for dep_content in f.readlines():
            departure_data.append(json.loads(dep_content))
        f.close()

    print(len(departure_data))

    return jsonify(departure_data[random.randrange(0, 4, 1)])

app.run()
