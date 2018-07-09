from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    return jsonify({"about": "Hello World! Gesuka is here now RESTful"})

def main():
    pass

if __name__ == '__main__':
    app.run(debug=True)