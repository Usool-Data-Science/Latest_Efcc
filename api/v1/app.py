#!/usr/bin/python3
"""A flask application that runs the endpoints"""
from models import app

if __name__ == "__main__":
    """Module runner"""

    app.run(host='0.0.0.0', port=5000, debug=True)
