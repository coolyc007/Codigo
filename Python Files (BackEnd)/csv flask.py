


from flask import *

app = Flask(__name__)

@app.route("/")
def index():
    return send_csv([{"id":34,"foo":"bar"},{"id":23,"foo":"buzz"}],"precipitation.csv",["id","foo"])