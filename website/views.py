import flask
import time
import requests
import os
import sys
import time
import json
import sqlite3
from website import app

# --Home Page --------------------------------#

app.config.from_object(__name__)

@app.route('/', methods=['GET'])
def index():
    return 'Welcome to the Simple Flask App!'
