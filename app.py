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
    html = f"<h3>Credit Service</h3>"
    return html.format(format)

@app.route("/predict", methods=['POST'])
def mk_predict():
    """Predicts the chance of defaulting"""

    json_payload = request.json
    LOG.info(f"JSON payload: {json_payload}")

    prediction = predict(json_payload)["human_readable_predict"]

    return jsonify(prediction)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)