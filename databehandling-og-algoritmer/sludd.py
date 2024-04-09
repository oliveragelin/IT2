from flask import Flask
import json
import requests

app = Flask(__name__)

base_url = "https://wttr.in/{sted}' ?format=j1"

@app.get("/<string:sted>")
def rute_index(sted):
    res = requests.get(base_url)
    data = res.json()
    akkurat_naa = data["current_condition"][0]["weatherDesc"][0]["value"]
    return f"<h1>{akkurat_naa}</h1>"

app.run(port=500, debug=True)