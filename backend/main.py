from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

@app.route("/message", methods=["GET"])
def get_message():
    response = []

    db = mysql.connector.connect(
        host="localhost",
        database="Pokemon",
        user="aluno",
        password="aluno123"
    )

    mycursor = db.cursor()
    mycursor.execute("select * from Pokemon")

    for row in mycursor:
        row = {
            "id" : row[0],
            "name" : row[1],
            "height" : row[2],
            "base_experience" : row[3]
        }

        response.append(row)

    return jsonify(response)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5050)


