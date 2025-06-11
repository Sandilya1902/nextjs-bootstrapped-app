from flask import Flask, request, jsonify
from flask_cors import CORS
import time
import datetime
import logging

app = Flask(__name__)
CORS(app, origins="http://localhost:8000")

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@app.route('/upload-health', methods=['POST'])
def upload_health():
    print("Received health data...") # Add console.log
    data = request.get_json()
    logging.info(f"Received data: {data}")
    # Process the data (e.g., store in a database)
    return jsonify({'message': 'Health data received'}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
