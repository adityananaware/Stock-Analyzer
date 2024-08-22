from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

API_KEY = 'your_api_key'
BASE_URL = 'https://www.alphavantage.co/query'

@app.route('/api/stock', methods=['GET'])
def get_stock_fundamentals():
    symbol = request.args.get('symbol')
    function = 'OVERVIEW'
    url = f"{BASE_URL}?function={function}&symbol={symbol}&apikey={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
