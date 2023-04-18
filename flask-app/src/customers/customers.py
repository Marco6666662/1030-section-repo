from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db
from datetime import datetime


customers = Blueprint('customers', __name__)

# Get customer by id from the DB
# John - 7
@customers.route('/customers/<cust_id>', methods=['GET'])
def get_customerbyID(cust_id):
    cursor = db.get_db().cursor()
    cursor.execute('select * from customers where cust_id = {0}'.format(cust_id))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Get all the products from the database
# John - 1
@customers.route('/products', methods=['GET'])
def get_products():
    cursor = db.get_db().cursor()
    cursor.execute('select prod_id, name, rating, price from products')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Get product by id from the DB
# John - 1
@customers.route('/products/<prod_id>', methods=['GET'])
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

# Update product information by id
# John - 9
@customers.route('/products/<prod_id>/update', methods=['PUT'])
def add_new_product(prod_id):
    the_data = request.json

    update_values = []
    for key, value in the_data.items():
        update_values.append(f'{key} = "{value}"')

    update_query = ', '.join(update_values)

    the_query = f'UPDATE products SET {update_query} WHERE prod_id = "{prod_id}"'

    current_app.logger.info(the_query)

    cursor = db.get_db().cursor()
    cursor.execute(the_query)
    db.get_db().commit()

    return "successfully update product info!"

# Register a customer
# John - 7
@customers.route('/customers/register', methods=['POST'])
def add_new_customer():
    the_data = request.json
    cust_id = the_data['cust_id']
    street = the_data['street']
    city = the_data['city']
    state = the_data['state']
    zip_code = the_data['zip_code']
    first = the_data['first_name']
    last = the_data['last_name']
    email = the_data['email']
    dob = the_data['dob']
    phone = the_data['phone']

    # Parse the dob string into a datetime object
    dob = datetime.strptime('Wed, 01 Jan 2003 00:00:00 GMT', '%a, %d %b %Y %H:%M:%S %Z')

    # Convert the datetime object into a string in the desired format
    dob = dob.strftime('%Y-%m-%d')

    current_app.logger.info(the_data)

    the_query = 'insert into customers (cust_id, street, city, state, zip_code, first_name, last_name, email, dob, phone)'
    the_query += 'values ("' + cust_id + '","'  + street + '", "' + city + '", "' + state + '", "' + zip_code + '", "' + first + '", "' + last + '", "' + email + '", "' + dob + '", "' + phone + '")'

    current_app.logger.info(the_query)

    cursor = db.get_db().cursor()
    cursor.execute(the_query)
    db.get_db().commit()

    return "success!"


# Update customer information by id
# John - 7
@customers.route('/customers/<cust_id>/update', methods=['PUT'])
def update_cust(cust_id):
    the_data = request.json

    update_values = []
    for key, value in the_data.items():
        update_values.append(f'{key} = "{value}"')

    update_query = ', '.join(update_values)

    the_query = f'UPDATE customers SET {update_query} WHERE cust_id = "{cust_id}"'

    current_app.logger.info(the_query)

    cursor = db.get_db().cursor()
    cursor.execute(the_query)
    db.get_db().commit()

    return "successfully register!"

# Delete customer information by id
# John - 7
@customers.route('/customers/<cust_id>/delete', methods=['DELETE'])
def delete_customer(cust_id):

    the_query = f'DELETE FROM customers WHERE cust_id = "{cust_id}"'

    current_app.logger.info(the_query)

    cursor = db.get_db().cursor()
    cursor.execute(the_query)
    db.get_db().commit()

    return "successfully delete!"

# Get a order of a specific customer from the DB
# John -6
@customers.route('/orders/<cust_id>/<order_id>', methods=['GET'])
def get_cust_order(cust_id, order_id):
    cursor = db.get_db().cursor()
    cursor.execute('select * from orders where cust_id = {0} and order_id = {1}'.format(cust_id, order_id))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Get all the retailers from the database
# John - 3
@customers.route('/retailers', methods=['GET'])
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

# Get retailer by id from the DB
# John - 3
@customers.route('/retailers/<ret_id>', methods=['GET'])
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

# Update retailer information by id
# John - 7
@customers.route('/retailers/<ret_id>/update', methods=['PUT'])
def update_retailer(ret_id):
    the_data = request.json

    update_values = []
    for key, value in the_data.items():
        update_values.append(f'{key} = "{value}"')

    update_query = ', '.join(update_values)

    the_query = f'UPDATE retailers SET {update_query} WHERE ret_id = "{ret_id}"'

    current_app.logger.info(the_query)

    cursor = db.get_db().cursor()
    cursor.execute(the_query)
    db.get_db().commit()

    return "successfully update retailer info!"

# Get products that offered by retailer from the database
# John - 4
@customers.route('/retailer_product_search', methods=['GET'])
def get_retailers_prod():
    cursor = db.get_db().cursor()
    prod_id = request.args.get('prod_id')
    ret_id = request.args.get('ret_id')
    if prod_id and ret_id:
        cursor.execute('SELECT * FROM retailers_products WHERE prod_id = {0} AND ret_id = {1}'.format(prod_id, ret_id))
    elif prod_id:
        cursor.execute('SELECT * FROM retailers_products WHERE prod_id = {0}'.format(prod_id))
    elif ret_id:
        cursor.execute('SELECT * FROM retailers_products WHERE ret_id = {0}'.format(ret_id))
    else:
        cursor.execute('SELECT * FROM retailers_products')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Get all promotion from the database
# John - 2
@customers.route('/promotion', methods=['GET'])
def get_promotions():
    cursor = db.get_db().cursor()
    cursor.execute('select proj_num, proj_name, prod_id from promotions')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Get specofic promotion from the database
# John - 2
@customers.route('/promotion/<proj_num>/<proj_name>/<prod_id>', methods=['GET'])
def get_promotion(proj_num, proj_name, prod_id):
    cursor = db.get_db().cursor()
    cursor.execute('select *  from promotions where proj_num = {0} and proj_name = "{1}" and prod_id = {2}'.format(proj_num, proj_name, prod_id))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response