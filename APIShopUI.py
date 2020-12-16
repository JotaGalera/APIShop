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
            "name": "Originals",
            "brand": "Adidas",
            "price": 72.0,
            "currency": "€",
            "image": "https://api-shop-ui.herokuapp.com/products/get_images/?name=adidas1.jpeg"
            },
            {
            "id": 2,
            "name": "Stan Smith",
            "brand": "Adidas",
            "price": 55.25,
            "currency": "€",
            "image": "https://api-shop-ui.herokuapp.com/products/get_images/?name=adidas2.jpeg"
            },
            {
            "id": 3,
            "name": "Ultraboost 20",
            "brand": "Adidas",
            "price": 63.0,
            "currency": "€",
            "image": "https://api-shop-ui.herokuapp.com/products/get_images/?name=adidas3.jpeg"
            },
            {
            "id": 4,
            "name": "Gazelle",
            "brand": "Adidas",
            "price": 80.75,
            "currency": "€",
            "image": "https://api-shop-ui.herokuapp.com/products/get_images/?name=adidas4.jpeg"
            },
            {
            "id": 5,
            "name": "Continental 80",
            "brand": "Adidas",
            "price": 72.0,
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

@app.route('/products/details/', methods=['GET'])
def get_product_detail(): 
    product_id = request.args.get("product_id")

    if product_id == "1":
        return product_detail_one()
    elif product_id == "2":
        return product_detail_two()
    elif product_id == "3":
        return product_detail_three()
    elif product_id == "4":
        return product_detail_four()
    elif product_id == "5":
        return product_detail_five()
    else:
        return "Invalid product"

def product_detail_one():
    data = {
            "id": 1,
            "name": "Originals",
            "color": "White & black",
            "brand": "Adidas",
            "original_price": 80.0,
            "discount": 10.0,
            "total_price": 72.0,
            "currency": "€",
            "images": ["https://api-shop-ui.herokuapp.com/products/get_images/?name=adidas1detail1.jpg","https://api-shop-ui.herokuapp.com/products/get_images/?name=adidas1detail2.jpg","https://api-shop-ui.herokuapp.com/products/get_images/?name=adidas1detail3.jpg"]
            }
    return data

def product_detail_two():
    data = {
            "id": 2,
            "name": "Stan Smith",
            "color": "White & green",
            "brand": "Adidas",
            "original_price": 65.0,
            "discount": 15.0,
            "total_price": 55.25,
            "currency": "€",
            "images": ["https://api-shop-ui.herokuapp.com/products/get_images/?name=adidas2detail1.jpg","https://api-shop-ui.herokuapp.com/products/get_images/?name=adidas2detail2.jpg","https://api-shop-ui.herokuapp.com/products/get_images/?name=adidas2detail3.jpg"]
            }
    return data

def product_detail_three():
    data = {
            "id": 3,
            "name": "Ultraboost 20",
            "color": "Black",
            "brand": "Adidas",
            "original_price": 70.0,
            "discount": 10.0,
            "total_price": 63.0,
            "currency": "€",
            "images": ["https://api-shop-ui.herokuapp.com/products/get_images/?name=adidas3detail1.jpg","https://api-shop-ui.herokuapp.com/products/get_images/?name=adidas3detail2.jpg","https://api-shop-ui.herokuapp.com/products/get_images/?name=adidas3detail3.jpg"]
            }
    return data

def product_detail_four():
    data = {
            "id": 4,
            "name": "Gazelle",
            "color": "Black",
            "brand": "Adidas",
            "original_price": 85.0,
            "discount": 5.0,
            "total_price": 80.75,
            "currency": "€",
            "image": ["https://api-shop-ui.herokuapp.com/products/get_images/?name=adidas4detail1.jpg","https://api-shop-ui.herokuapp.com/products/get_images/?name=adidas4detail2.jpg","https://api-shop-ui.herokuapp.com/products/get_images/?name=adidas4detail3.jpg"]
            }
    return data

def product_detail_five():
    data = {
            "id": 5,
            "name": "Continental 80",
            "color": "White",
            "brand": "Adidas",
            "original_price": 80.0,
            "discount": 10.0,
            "total_price": 72.0,
            "currency": "€",
            "image": ["https://api-shop-ui.herokuapp.com/products/get_images/?name=adidas5detail1.jpg","https://api-shop-ui.herokuapp.com/products/get_images/?name=adidas5detail2.jpg","https://api-shop-ui.herokuapp.com/products/get_images/?name=adidas5detail3.jpg"]
            }
    return data

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
