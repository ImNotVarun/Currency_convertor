from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__, static_folder='static')


@app.route('/')
def index():
    return send_from_directory('static', 'index.html')


@app.route('/static/index.css')
def static_files():
    return send_from_directory('static', 'index.css')


@app.route('/convert', methods=['POST'])
def convert():
    data = request.json
    if data is None:
        return jsonify({'error': 'No JSON data received'}), 400

    amount = data.get('amount')
    conversion_type = data.get('type')

    if amount is None or conversion_type is None:
        return jsonify({'error': 'Missing required fields in JSON data'}), 400
    try:
        amount = float(amount)
    except ValueError:
        return jsonify({'error': 'Invalid amount value'}), 400

    result = {}

    if conversion_type == "INR_to_USD":
        result = {"converted amount": round(amount / 83, 2)}
    elif conversion_type == "USD_to_INR":
        result = {"converted amount": round(amount * 83, 2)}
    else:
        result = {"error": "Invalid conversion type"}

    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
