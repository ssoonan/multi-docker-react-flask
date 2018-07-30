from flask import Flask

application = Flask(__name__)
app = application


@app.route('/')
def index():
    return "<h1>Hello, Deploy~!</h1>"