from flask import Flask
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "Welcome to APIShop"

app.run(threaded=True, port=5000)