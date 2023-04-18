from flask import Blueprint, request, jsonify, make_response
import json
from src import db


retailers = Blueprint('retailers', __name__)

# Get all the products from the database
@retailers.route('/retailers', methods=['GET'])
def get_retailers():
    cursor = db.get_db().cursor()
    cursor.execute('select * from retailers')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Get customer by id from the DB
@retailers.route('/retailers/<ret_id>', methods=['GET'])
def get_retailerbyID(ret_id):
    cursor = db.get_db().cursor()
    cursor.execute('select * from retailers where ret_id = {0}'.format(ret_id))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Return a list of all products stock offered by each retailer with their id
@retailers.route('/retailers_products/', methods=['GET'])
def get_retailers_products():
    cursor = db.get_db().cursor()
    cursor.execute('select * from products join offered_by on products.prod_id=offered_by.product_id')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Add new product
@retailers.route('/products/<prod_id>', methods=['POST'])
def post_prod_id(date_listed, name, _class, category, price, description, brought_id, order_id, prod_id):
    cursor = db.get_db().cursor()
    cursor.execute(f'insert into products (date_listed, name, class, category, price, description, brought_id, order_id, prod_id) \
                   values ({date_listed}, {name}, {_class}, {category}, {price}, {description}, {brought_id}, {order_id}, {prod_id});')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Update the price of a product
@retailers.route('/products/<prod_id>', methods=['PUT'])
def update_prod_id(prod_id, price):
    cursor = db.get_db().cursor()
    cursor.execute(f'update products set price = {price} where prod_id = {prod_id};')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Delete a product that is discontinued
@retailers.route('/products/<prod_id>', methods=['DELETE'])
def delete_prod_id(prod_id):
    cursor = db.get_db().cursor()
    cursor.execute(f'delete from products where prod_id = {prod_id};')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Return all detailed information for a particular product
@retailers.route('/products/<prod_id>', methods=['GET'])
def get_productbyID(prod_id):
    cursor = db.get_db().cursor()
    cursor.execute('select * from products where prod_id = {0}'.format(prod_id))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response