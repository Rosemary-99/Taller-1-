from flask import Flask, request, render_template

import pandas as pd

from prediction_model import PredictionModel


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("main.html")

@app.route("/predictartist", methods=["POST"])
def make_predictions_artist():
    X = request.json["name"]

    predicion_model = PredictionModel()
    results = predicion_model.make_predictions_artist(X)
    
    return results.to_json(orient="records")


@app.route("/predicttrack", methods=["POST"])
def make_predictions_track():
    X = request.json["name"]

    predicion_model = PredictionModel()
    results = predicion_model.make_predictions_track(X)
    print(len(results))
    return results.to_json(orient="records")


if __name__ == "__main__":
    app.run(debug=True)