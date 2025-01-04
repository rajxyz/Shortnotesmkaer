from flask import Flask, request, jsonify
from logic import extract_content

app = Flask(__name__)

@app.route('/extract', methods=['POST'])
def extract():
    # Get data from the request
    data = request.get_json()

    # Extract text and type from the request
    text = data.get("text")
    extract_type = data.get("type")

    if not text or not extract_type:
        return jsonify({"error": "Text and extraction type are required"}), 400

    # Call the relevant extraction logic
    result = extract_content(text, extract_type)

    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)
