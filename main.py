from flask import Flask, render_template, request, jsonify
from google import genai
import os

app = Flask(__name__)

# ✅ CORRECT: variable NAME, not key
api_key = "your api key"

if not api_key:
    raise RuntimeError("GOOGLE_API_KEY not found in environment variables")

client = genai.Client(api_key=api_key)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True)

    if not data or "message" not in data:
        return jsonify({"reply": "Invalid request"}), 400

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=data["message"]
        )
        return jsonify({"reply": response.text})

    except Exception as e:
        print("ERROR:", e)
        return jsonify({"reply": "Gemini error"}), 500


if __name__ == "__main__":
    app.run(debug=True, port=2005)
