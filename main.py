# Using flask to make an api
# import necessary libraries and functions
from crypt import methods
from flask import Flask, jsonify, request, make_response
from flask_cors import CORS, cross_origin
import json
import os
  
# creating a Flask app
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
  
@app.route('/<string:mock_api>', methods = ['GET'])
@cross_origin()
def details(mock_api):
    res = None
    filepath = 'mock-api/{}.json'.format(mock_api)
    if not os.path.exists(filepath):
        return make_response(jsonify({'message': 'API not found'}), 404)

    with open(filepath) as json_file:
        res = json.load(json_file)

    return make_response(jsonify(res), 200)
  
  
# driver function
if __name__ == '__main__':
  
    app.run(debug = True)