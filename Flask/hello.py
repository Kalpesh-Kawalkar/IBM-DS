from flask import Flask
app = Flask(__name__)
@app.route("/")
def index():
    return "hello world"


# Commands for Command line
python3 -- version
pip install "Flask==2.2.2"
flask --app server --debug run
curl -X GET -i -w '\n' localhost:5000
