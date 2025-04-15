
from flask import Flask

app = Flask(__name__)



@app.route("/getcities/")
def getCities():
    return {"airpots": ["SBA", "SMX"]}


@app.route("/temperature/<city>")
def temperature(city):
    if city == "SBA":
        return {"tempature": "72"}
    elif city == "SMX":
        return {"tempature": "50"}
    else:
        return "Invalid Request"

@app.route("/wind_speed/<city>")
def wind_speed(city):
    if city == "SBA": 
        return {"speed": "2.2", "direction": "NW"}
    elif city == "SMX": 
        return {"speed": "1.5", "direction": "S"}
    else:
        return "Invalid Request"




@app.route("/cloud_cover/<city>")
def cloud_cover(city):
    if city == "SBA":
        return {"cloud_cover": "2"}
    elif city == "SMX":
        return {"cloud_cover": "4"}
    else:
        return "Invalid Request"
