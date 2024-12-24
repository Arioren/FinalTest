from flask import Flask, jsonify
import requests

base_url = 'http://127.0.0.1:5001/api/terror_data'

def get_statistics(endpoint: str):
    url = f"{base_url}/{endpoint}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return jsonify(data)
    else:
        return jsonify({"error": "Failed to retrieve data"}), 500
