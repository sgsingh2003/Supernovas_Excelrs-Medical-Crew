from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import os

def medical_ai_agent(symptoms):
    steps = []

    steps.append("Understanding patient symptoms")
    steps.append("Mapping symptoms to possible conditions")
    steps.append("Generating medical advice")
    steps.append("Creating final report")

    report = f"""
    Medical AI Agent Report

    Step 1: Symptom Analysis
    Reported symptoms: {symptoms}

    Step 2: Possible Conditions
    - Viral infection
    - Stress or fatigue
    - Mild respiratory issue

    Step 3: Recommended Actions
    - Take rest and stay hydrated
    - Monitor symptoms for 24–48 hours
    - Seek medical help if condition worsens

    This report was generated autonomously by the Medical AI Agent.
    """

    return {
        "steps": steps,
        "report": report
    }


# Base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Flask app with correct template folder
app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates")
)
CORS(app)

# Home route
@app.route("/")
def home():
    return render_template("index.html")



# Run server
@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    symptoms = data.get("problem", "")

    if not symptoms:
        return jsonify({"error": "No symptoms provided"}), 400

    result = medical_ai_agent(symptoms)

    return jsonify({
        "status": "success",
        "agent_steps": result["steps"],
        "medical_report": result["report"]
    })

if __name__ == "__main__":
    app.run(debug=True)