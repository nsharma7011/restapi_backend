from flask import Flask, request, jsonify

app = Flask(__name__)

USER_ID = "Nikhil_sharma"
EMAIL = "nikhil@xyz.com"
ROLL_NUMBER = "101"

def find_highest_alphabet(alphabets):
    if not alphabets:
        return []
    return [max(alphabets, key=lambda x: x.lower())]

@app.route('/bfhl', methods=['POST'])
def process_request():
    try:
        data = request.json.get("data", [])
        numbers = [item for item in data if item.isdigit()]
        alphabets = [item for item in data if item.isalpha()]
        highest_alphabet = find_highest_alphabet(alphabets)

        response = {
            "is_success": True,
            "user_id": USER_ID,
            "email": EMAIL,
            "roll_number": ROLL_NUMBER,
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_alphabet": highest_alphabet
        }
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"is_success": False, "error": str(e)}), 400

@app.route('/bfhl', methods=['GET'])
def get_operation_code():
    return jsonify({"operation_code": 1}), 200

if __name__ == '__main__':
    app.run(debug=True)