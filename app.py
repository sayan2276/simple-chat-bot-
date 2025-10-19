from flask import Flask, request, jsonify, render_template, session
import google.generativeai as genai
import os

app = Flask(__name__)
app.secret_key = "secretkey"  # for session memory

# Configure Gemini API
os.environ["GOOGLE_API_KEY"] = "AIzaSyAlsLs1LvGQdAC3hQOsZfL4hcE2hrw8fNM"
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
model = genai.GenerativeModel("models/gemini-2.5-flash")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_message = request.json.get("message", "")
        history = session.get("history", [])
        history.append({"role": "user", "parts": [user_message]})

        response = model.generate_content(history)
        reply = response.text.strip()

        history.append({"role": "model", "parts": [reply]})
        session["history"] = history[-10:]  # keep last 10 messages

        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"reply": f"Error: {str(e)}"})

if __name__ == "__main__":
    app.run(debug=True)
