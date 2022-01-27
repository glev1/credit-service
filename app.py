import ast
import logging
from flask import Flask, request, jsonify
from flask.logging import create_logger

from src.main.mlib import predict

app = Flask(__name__)
LOG = create_logger(app)
LOG.setLevel(logging.INFO)

@app.route('/')
def home():
    """Return a HTTP greeting"""
    html = '''<h1 style="color:green;" >Welcome to the Give Me Some Credit Web Application</h1>
            <p>Banks play a crucial role in market economies. They decide who can get finance and on what terms and can make <br>
            or break investment decisions. For markets and society to function, individuals and companies need access to credit. <br>
            <p>Here, you can predict the probability that somebody will experience financial disstress in the next two years.</p>
            <p>For more information, access <a href="https://github.com/glev1/credit-service">Credit Service Repo</a>.'''
    return html.format(format)

@app.route("/predict", methods=['POST'])
def mk_predict():
    """Predicts the chance of defaulting"""

    json_payload = request.json
    LOG.info(f"JSON payload: {json_payload}")

    prediction = predict(json_payload)["human_readable_predict"]

    return jsonify(prediction)

@app.route("/webpredict/<profile>")
def mk_web_predict(profile):
    """Predicts the chance of defaulting"""
    payload = ast.literal_eval(profile)

    LOG.info(f"JSON payload: {payload}")
    prediction = predict(payload)["human_readable_predict"]

    return jsonify(prediction)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)