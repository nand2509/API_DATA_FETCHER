from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fetch_data', methods=['POST'])
def fetch_data():
    data = request.json
    api_url = data.get('api_url')
    api_key = data.get('api_key')

    if not api_url:
        return jsonify({'error': 'API URL is required'}), 400

    headers = {}
    if api_key:
        headers['Authorization'] = f'Bearer {api_key}'  # Common API key header format

    try:
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()
        return jsonify({'data': response.json()})
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
