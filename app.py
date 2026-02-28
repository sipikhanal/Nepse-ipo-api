from flask import Flask, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

@app.route('/api/ipo-listings', methods=['GET'])
def ipo_listings():
    # Check if the file exists (created by GitHub Actions)
    if os.path.exists('ipo_data.json'):
        with open('ipo_data.json', 'r') as f:
            data = json.load(f)
        return jsonify(data)
    
    return jsonify({"error": "Data initializing... please check back in a few minutes."}), 404

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
