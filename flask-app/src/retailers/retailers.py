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