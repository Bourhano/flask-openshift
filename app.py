import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome again!"

@app.route('/how are you')
def hello():
    return 'I am good, how about you???'

@app.route('/check')
def read_file():
    f = open("/bourhan_data/file.txt")
    text = f.read()
    return type(text)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
