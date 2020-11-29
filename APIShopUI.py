from flask import Flask, render_template, request, jsonify, send_from_directory
import os

image_folder_static = 'images'

app = Flask(__name__, static_folder=image_folder_static)

@app.route('/', methods=['GET'])
def home():
    return "Welcome to APIShop"

@app.route('/products/', methods=['GET'])
def products():
    data = {
        "list": [
            {
            "id": 1,
            "name": "white-black trainers",
            "brand": "Adidas",
            "price": 80,
            "currency": "€",
            "image": "https://api-shop-ui.herokuapp.com/products/get_images/?name=adidas1.jpeg"
            },
            {
            "id": 2,
            "name": "white-green trainers",
            "brand": "Adidas",
            "price": 65,
            "currency": "€",
            "image": "https://api-shop-ui.herokuapp.com/products/get_images/?name=adidas2.jpeg"
            },
            {
            "id": 3,
            "name": "black trainers",
            "brand": "Adidas",
            "price": 70,
            "currency": "€",
            "image": "https://api-shop-ui.herokuapp.com/products/get_images/?name=adidas3.jpeg"
            },
            {
            "id": 4,
            "name": "sport trainers",
            "brand": "Adidas",
            "price": 85,
            "currency": "€",
            "image": "https://api-shop-ui.herokuapp.com/products/get_images/?name=adidas4.jpeg"
            },
            {
            "id": 5,
            "name": "white trainers",
            "brand": "Adidas",
            "price": 75,
            "currency": "€",
            "image": "https://api-shop-ui.herokuapp.com/products/get_images/?name=adidas5.jpeg"
            }
        ],
        "page": 1,
        "pageSize": 5,
        "size": "20"
        }
    return data

@app.route('/products/images/', methods=['GET'])
def images():
    name = request.args.get("name")
    pathImage = '/' + image_folder_static + '/' + name
    return render_template("image.html", user_image = pathImage)

@app.route('/products/get_images/', methods=['GET'])
def get_image(): 
    name = request.args.get("name")
    return send_from_directory(app.static_folder, filename=name, mimetype='image/jpg')

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
