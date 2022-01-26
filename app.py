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
def predict():
    """Predicts the chance of defaulting"""
    
    json_payload = request.json
    LOG.info(f"JSON payload: {json_payload}")
    prediction = predict(json_payload)
    return jsonify(prediction)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)

# @app.route('/predict/<inc>/<age>/<rev>/<debt>/<dep>/<cred>'+
#             '/<estate>/<lowdue>/<middue>/<highdue>')
# def predictroute(inc, age, rev, debt, dep, cred, estate,
#                 lowdue, middue, highdue):
#     """Predicts the chance of defaulting"""
    
#     print("Predict of defaulting for profile:\n"+ 
#             f"Monthly income: ${inc:.2f}\n"+
#             f"Age: {age} years\n"+
#             f"Revolving utilization of unsercured lines: {rev*100:.2f}%\n"+
#             f"Debt ratio: {debt*100:.2f}%\n"+
#             f"Number of dependents: {dep}\n"+
#             f"Number of open loans and lines of credit: {cred}\n"+
#             f"Number of mortgage and real estate loans: {estate}\n"+
#             f"Number of times 30-59 days past due: {lowdue} times\n"+
#             f"Number of 60-89 days past due: {middue}\n"+
#             f"Number of times 90 days or more past due: {highdue}")

#     feats =[rev, debt, inc, age, lowdue, cred, highdue,
#             estate, middue, dep]

#     result = predict(feats)
#     return jsonify(result)

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=8080, debug=True)