# run api : source venv/bin/activate
from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__, static_folder='images')

@app.route('/', methods=['GET'])
def home():
    return "Welcome to APIShop"

@app.route('/products/', methods=['GET'])
def products():
    data = {
        "list": [
            {
            "id": 1,
            "name": "trainers",
            "brand": "Adidas",
            "price": 80,
            "currency": "€",
            "image": "http://127.0.0.1/products/image?name=Adidas.jpg"
            },
            {
            "id": 2,
            "name": "trainers",
            "brand": "Adidas 2",
            "price": 65,
            "currency": "€",
            "image": "http://127.0.0.1/products/image?name=Adidas-2.jpg"
            }
        ],
        "page": 1,
        "pageSize": 2,
        "size": "20"
        }
    return data

@app.route('/products/image', methods=['GET'])
def images(): #Example http://127.0.0.1:5000/products/image?name=Adidas.jpg
    name = request.args.get("name")
    userImage = 'images/' + name
    return render_template("image.html", user_image = userImage)
    
app.run(debug=True, threaded=True, port=5000)