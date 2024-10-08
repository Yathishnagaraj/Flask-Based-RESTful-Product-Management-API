from flask import Flask, jsonify, request, send_from_directory
import os

app = Flask(__name__)

# In-memory data storage for demonstration (no product prices)
products = [
    {"id": 1, "name": "Orbit"},
    {"id": 2, "name": "Happydent"}
]

# Route for root
@app.route('/')
def home():
    return "Welcome to the Products API"

# Handle favicon request
@app.route('/favicon.ico')
def favicon():
    return '', 204

# Get all products
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products), 200

# Get a product by ID
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    if product:
        return jsonify(product), 200
    return jsonify({"error": "Product not found"}), 404

# Create a new product
@app.route('/products', methods=['POST'])
def create_product():
    new_product = request.json
    new_product["id"] = len(products) + 1
    products.append(new_product)
    return jsonify(new_product), 201

# Update an existing product by ID
@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    if product:
        updated_data = request.json
        product.update(updated_data)
        return jsonify(product), 200
    return jsonify({"error": "Product not found"}), 404

# Delete a product by ID
@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    global products
    products = [p for p in products if p["id"] != product_id]
    return jsonify({"message": "Product deleted"}), 200

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
