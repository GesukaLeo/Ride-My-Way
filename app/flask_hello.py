from flask import flask

app = flask(__name__)

@app route("/")
def hello():
    return "Hello World!"

def main():
    pass

if __name__ == '__main__':
    app run(debug=True)