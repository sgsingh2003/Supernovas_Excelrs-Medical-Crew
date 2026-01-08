from flask import Flask, request, jsonify
import sys
import os

# Allow Flask to find src/
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
)

from mycrewapp.crew import run_medical_crew

app = Flask(__name__)

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()

    user_problem = data.get("problem", "")

    if not user_problem:
        return jsonify({"error": "No problem provided"}), 400

    try:
        result = run_medical_crew(user_problem)

        return jsonify({
            "status": "success",
            "medical_report": str(result)
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True)