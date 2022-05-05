##Simple Mock Server for polling Flight Data

###Requirements
- Python3, pip3

###Setup
- create a python virtual environment
```bash
python3 -m venv ./sample-env
```
- clone this repo in the virtual environment
```bash
git clone git@github.com:KyalSinLinLett/flight-data-mock-server.git
```
- activate virtual environment
"inside the directory where the virtual env is created"
```bash
chmod 755 ./bin/activate (only for the first time)
source ./bin/activate
```
- install pip dependencies
```bash
pip3 install -r requirements.txt
```
- run mock server
```bash
python3 src/app.py
```
