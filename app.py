from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
  return "We are trying to use DevOps tools"
