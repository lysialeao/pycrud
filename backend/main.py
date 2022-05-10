from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/message", methods=["GET"])
def get_message():
    response = {
        "message": "Hello World"
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5050)
