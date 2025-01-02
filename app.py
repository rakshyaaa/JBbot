from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    response = generate_response(user_message)
    return jsonify({"response": response})

def generate_response(message):
    if "jellybean" in message.lower():
        return "Jellybean is Rakshya Pandey, currently pusuing master's in Computer Science at ULL"
    if "skills" in message.lower():
        return "She is skilled in Python, Angular, and web development."
    elif "experience" in message.lower():
        return "She has experience building full-stack web applications."
    elif "education" in message.lower():
        return "I hold a bachelor's degree in Computer Science."
    else:
        return "I'm Jellybean, happy to assist you!"

if __name__ == "__main__":
    app.run(debug=True)
