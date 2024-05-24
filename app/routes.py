from flask import Flask

app = Flask(__name__)

@app.get("/")
def index():
    me = {
        "first_name": "Jay",
        "last_name": "Barr",
        "hobbies": "Concerts",
        "is_online": True
    }
    return me
 