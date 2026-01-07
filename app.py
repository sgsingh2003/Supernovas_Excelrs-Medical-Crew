from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/analyze", methods=["POST"])
def analyze():
    return jsonify({
        "steps": [
            "Python backend is working",
            "Frontend connected successfully",
            "This confirms 80% project completion"
        ],
        "critical": "This message is coming from Python"
    })

if __name__ == "__main__":
    app.run(debug=True)