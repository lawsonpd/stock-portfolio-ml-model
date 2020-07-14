from flask import Flask, jsonify, request
from predict import get_portfolio_predictions, get_trade_api, get_s3_conn
import os

import json

alpaca_api_key_id = os.getenv('ALPACA_API_KEY_ID')
alpaca_secret_key = os.getenv('ALPACA_SECRET_KEY')
aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')

# Flask app
app = Flask(__name__)

# Routes
@app.route('/predict', methods=['POST'])
def predict():
    req = request.get_json(force=True)

    tickers = req['tickers']

    trade_api = get_trade_api(alpaca_api_key_id, alpaca_secret_key)

    s3_conn = get_s3_conn(aws_access_key_id, aws_secret_access_key)

    user_portfolio_metrics = get_portfolio_predictions(tickers, trade_api, s3_conn)

    output = jsonify(results=user_portfolio_metrics)

    return output



@app.route('/vars-7567875983945734', methods=['GET'])
def test_vars():
    vars = {
        'alpaca key id': alpaca_api_key_id, 
        'aws key id': aws_access_key_id
    }
    
    vars_json = json.dumps(vars)
    
    return vars_json



if __name__ == '__main__':
    app.run(port = 5000, debug=True)