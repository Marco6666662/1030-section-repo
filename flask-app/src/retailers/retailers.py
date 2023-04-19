from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db


retailers = Blueprint('retailers', __name__)

# Return a list of all products stock offered by each retailer with their id
@retailers.route('/retailers_products/', methods=['GET'])
def get_retailers_products():
    cursor = db.get_db().cursor()
    cursor.execute('select * from products join retailers_products on products.prod_id=retailers_products.prod_id')
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
def post_prod_id(prod_id):
    req_data = request.get_json()
    current_app.logger.info(req_data)

    date_listed = req_data['date_listed']
    name = req_data['name']
    _class = req_data['class']
    category = req_data['category']
    price = req_data['price']
    description = req_data['description']

    cursor = db.get_db().cursor()
    cursor.execute(f'insert into products (date_listed, name, class, category, price, description, prod_id) \
                   values ({date_listed}, {name}, {_class}, {category}, {price}, {description}, {prod_id});')
    db.get_db().commit()
    return 'Success'

# Update the price of a product
@retailers.route('/products/<prod_id>', methods=['PUT'])
def update_prod_id(prod_id):
    req_data = request.get_json()
    current_app.logger.info(req_data)

    price = req_data['price']

    cursor = db.get_db().cursor()
    cursor.execute(f'update products set price = {price} where prod_id = {prod_id};')
    db.get_db().commit()
    return 'Success'

# Delete a product that is discontinued
@retailers.route('/products/<prod_id>', methods=['DELETE'])
def delete_prod_id(prod_id):
    cursor = db.get_db().cursor()
    cursor.execute(f'delete from products where prod_id = {prod_id};')
    
    return 'Success'

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

# persona story 4
@retailers.route('/order_products', methods=['GET'])
def get_order_products():
    cursor = db.get_db().cursor()
    cursor.execute('select * from order_products')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# persona story 4
@retailers.route('/order_products/<prod_id>', methods=['GET'])
def get_product_orders(prod_id):
    cursor = db.get_db().cursor()
    cursor.execute(f'select * from order_products where prod_id = {prod_id}')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# persona story 5
@retailers.route('/orders/<order_id>', methods=['PUT'])
def update_order(order_id):
    current_app.logger.info('Processing form data')
    req_data = request.get_json()
    current_app.logger.info(req_data)
    
    order_status = req_data['order_status']
    
    update_stmt = f'UPDATE orders SET order_status = {order_status} WHERE order_id = {order_id};'
    
    current_app.logger.info(update_stmt)
    
    cursor = db.get_db().cursor()
    cursor.execute(update_stmt)
    db.get_db().commit()
    return "Success"

# persona story 6
@retailers.route('/retailers/<ret_id>', methods=['GET','PUT'])
def retailer_info(ret_id):
    if request.method == 'GET':
        cursor = db.get_db().cursor()
        cursor.execute(f'select * from retailers where ret_id = {ret_id}')
        row_headers = [x[0] for x in cursor.description]
        json_data = []
        theData = cursor.fetchall()
        for row in theData:
            json_data.append(dict(zip(row_headers, row)))
        the_response = make_response(jsonify(json_data))
        the_response.status_code = 200
        the_response.mimetype = 'application/json'
        return the_response
    else:
        current_app.logger.info('Processing form data')
        req_data = request.json
        current_app.logger.info(req_data)
        
        state = req_data['state']
        city = req_data['city']
        street = req_data['street']
        zip_code = req_data['zip_code']
        
        update_stmt = f'UPDATE retailers SET state = "{state}", city = "{city}", street = "{street}", zip_code = "{zip_code}" WHERE ret_id = {ret_id};'
        
        current_app.logger.info(update_stmt)
        
        cursor = db.get_db().cursor()
        cursor.execute(update_stmt)
        db.get_db().commit()
        return "Success"

# persona story 7
@retailers.route('/retailers_products/<ret_id>/<prod_id>', methods=['PUT'])
def update_product_stock(ret_id, prod_id):
    current_app.logger.info('Processing form data')
    req_data = request.get_json()
    current_app.logger.info(req_data)
    
    stock = req_data['stock']
    
    update_stmt = f'UPDATE retailers_products SET stock = {stock} WHERE ret_id = {ret_id} AND prod_id = {prod_id};'
    
    current_app.logger.info(update_stmt)
    
    cursor = db.get_db().cursor()
    cursor.execute(update_stmt)
    db.get_db().commit()
    return "Success"
