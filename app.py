from flask import Flask
app = Flask(__name__)

@app.route("/")
def hame():
  return "hellow frfhgfhgfh"
