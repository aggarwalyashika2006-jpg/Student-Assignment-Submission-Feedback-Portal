from flask import Flask, request, jsonify
from flask_cors import CORS
from sentence_transformers import SentenceTransformer, util
import joblib

app = Flask(__name__)
CORS(app)  # 🔥 FIX

sbert = SentenceTransformer("all-MiniLM-L6-v2")

try:
    grade_model = joblib.load("grade_model.pkl")
except:
    grade_model = None

@app.route("/")
def home():
    return "AI Backend is Running 🚀"

@app.route("/similarity", methods=["POST"])
def similarity():
    data = request.get_json()

    q = sbert.encode(data.get("text", ""), convert_to_tensor=True)
    C = sbert.encode(data.get("corpus", []), convert_to_tensor=True)

    score = float(util.cos_sim(q, C)[0].max())

    return jsonify({"plagiarism_score": score})

@app.route("/grade", methods=["POST"])
def grade():
    if grade_model is None:
        return jsonify({"error": "Model not trained"}), 500

    text = request.get_json().get("text", "")
    pred = float(grade_model.predict([text])[0])

    return jsonify({"grade_suggestion": pred})

if __name__ == "__main__":
    app.run(debug=True)