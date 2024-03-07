# app/app.py
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/check_number', methods=['POST'])
def check_number():
    data = request.get_json()
    if 'integer' in data and isinstance(data['integer'], int):
        input_number = data['integer']
        response_data = {
            'integer': input_number,
            'value': 'high' if input_number > 100 else 'low'
        }
        return jsonify(response_data)
    else:
        return jsonify({'error': 'Invalid input'}), 400

if __name__ == '__main__':
    app.run(debug=True)
