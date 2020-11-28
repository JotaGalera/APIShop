from flask import Flask, render_template, request, jsonify, send_from_directory
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
            "image": "https://api-shop-ui.herokuapp.com/products/images/?name=Adidas.jpg"
            },
            {
            "id": 2,
            "name": "trainers",
            "brand": "Adidas 2",
            "price": 65,
            "currency": "€",
            "image": "https://api-shop-ui.herokuapp.com/products/images/?name=Adidas-2.jpg"
            }
        ],
        "page": 1,
        "pageSize": 2,
        "size": "20"
        }
    return data

@app.route('/products/images/', methods=['GET'])
def images(): #Example http://127.0.0.1:5000/products/images/?name=Adidas.jpg
    name = request.args.get("name")
    pathImage = '/images/' + name
    return render_template("image.html", user_image = pathImage)

@app.route('/products/get_images/', methods=['GET'])
def get_image(): 
    name = request.args.get("name")
    path = '/images/'
    return send_from_directory(app.static_folder, filename=name, mimetype='image/jpg')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
