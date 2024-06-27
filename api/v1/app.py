#!/usr/bin/python3
"""A flask application that runs the endpoints"""
from models import app, db
from flask import Flask, render_template, make_response, jsonify

# @app.teardown_appcontext
# def close_db(error):
#     """Closes the data"""
#     db.sesssion.remove()

@app.errorhandler(404)
def not_found(error):
    """Custom error message"""
    response = jsonify({'error': 'Not Found'})
    return make_response(response)


if __name__ == "__main__":
    """Module runner"""
    # host = getenv("EFCC_MYSQL_HOST")
    # port = getenv("EFCC_MYSQL_PORT")
    # if not host:
    #     host = '0.0.0.0'
    # if not port:
    #     port = '5000'
    # app.run(host=host, port=port, threaded=True, debug=True)
    app.run(host='0.0.0.0', port=5000, debug=True)
