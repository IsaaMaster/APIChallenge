from flask import Flask

app = Flask(__name__)


@app.route("/") 
def getRoutes(): 
    output = [] 
    for rule in app.url_map.iter_rules(): 
        methods = ','.join(sorted(rule.methods)) 
        line = f"{rule.endpoint:30s} {methods:20s} {rule}" 
        output.append(line) 
    return '<pre>' + '\n'.join(sorted(output)) + '</pre>' 

@app.route("/getcities/")
def getCities():
    return {"airports": ["sba", "smx"]}

@app.route("/temperature/<city>")
def temperature(city):
    if city == "sba":
        return {"temperature": "72"}
    elif city == "smx":
        return {"temperature": "50"}
    else:
        return "Invalid Request"

@app.route("/wind_speed/<city>")
def wind_speed(city):
    if city == "sba":
        return {"speed": "2.2", "direction": "NW"}
    elif city == "smx":
        return {"speed": "1.5", "direction": "S"}
    else:
        return "Invalid Request"

@app.route("/cloud_cover/<city>")
def cloud_cover(city):
    if city == "sba":
        return {"cloud_cover": "2"}
    elif city == "smx":
        return {"cloud_cover": "4"}
    else:
        return "Invalid Request"

if __name__ == '__main__': 
    app.run(host='0.0.0.0')
