from flask import Flask, jsonify, render_template, request
from pymongo import MongoClient
import subprocess
import os

app = Flask(__name__)

# MongoDB Configuration
MONGO_URI = "mongodb://localhost:27017"  # Replace with your MongoDB URI
DB_NAME = "TwitterData"
COLLECTION_NAME = "TrendingTopics"

# Route to run Selenium script
@app.route('/run-selenium', methods=['POST'])
def run_selenium_script():
    try:
        # Run the Selenium script (ensure the script is executable and in the same directory)
        result = subprocess.run(['python', 'selenium_script.py'], capture_output=True, text=True)
        if result.returncode != 0:
            return jsonify({"error": "Failed to run Selenium script", "details": result.stderr}), 500
        
        return jsonify({"message": "Selenium script executed successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to fetch latest results
@app.route('/fetch-results', methods=['GET'])
def fetch_results():
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    collection = db[COLLECTION_NAME]
    latest_entry = collection.find_one(sort=[("_id", -1)])  # Fetch the latest document
    if not latest_entry:
        return jsonify({"error": "No records found"}), 404

    return jsonify(latest_entry)

# Route to serve the HTML page
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
