
from flask import Flask, jsonify
from datetime import datetime
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route('/time', methods=['GET'])
def get_time():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return jsonify({"time": current_time})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
