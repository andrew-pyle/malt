from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("geo.html") #changed from "index.html" for demonstration of pi online hosting

@app.route("/hero_thirds")
def hero_thirds():
    return render_template("hero_thirds.html")

@app.route("/test")
def test():
    return render_template("test.html")

@app.route("/number1")
def number1():
    return render_template("number1.html")

@app.route("/geo")
def geo():
    return render_template("geo.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
