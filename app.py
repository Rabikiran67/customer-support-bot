from flask import Flask, request, jsonify
from chatbot import chatbot_response

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    response = chatbot_response(user_input)
    return jsonify({"reply": response})

if __name__ == "__main__":
    app.run(debug=True)
