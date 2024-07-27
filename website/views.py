import flask
import time
import requests
import os
import sys
import time
import json
import sqlite3
from website import app
from flask import render_template, session, jsonify, request, Response, redirect, url_for, send_from_directory

# --Home Page --------------------------------#

# reload(sys)
# sys.setdefaultencoding('utf8')
# print("efwr", sys.getdefaultencoding())
# app.config.from_object(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')
    try:
        # Example data
        return render_template('index.html')
    except UnicodeDecodeError as e:
        # Log the error for debugging
        app.logger.error(f"UnicodeDecodeError: {e}")
        return "There was an error rendering the template."
