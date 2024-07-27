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


# --Connect db --------------------------------#
def connect_db():
    print("Connecting to database...")
    try:
        with sqlite3.connect("users.db") as con:
            print("Connected to database...")
            cur = con.cursor()

            # Create table if it doesn't exist
            cur.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    email TEXT PRIMARY KEY,
                    name TEXT,
                    org TEXT,
                    roles TEXT
                )
            """)

            # Check if record already exists
            email = 'sample@gmail.com'
            cur.execute("SELECT COUNT(*) FROM users WHERE email = ?", (email,))
            count = cur.fetchone()[0]
            if count == 0:
                # Insert data into the table
                cur.execute("""
                    INSERT INTO users (email, name, org, roles) VALUES
                    (?, ?, ?, ?)
                """, (email, 'hit', 'ker', 'admin'))
                print("Data inserted successfully.")
            else:
                print("The record already exists in the database.")

            # Commit the transaction
            con.commit()

    except sqlite3.Error as e:
        print(f"The error '{e}' occurred")


connect_db()

# --Home Page --------------------------------#


# reload(sys)
# sys.setdefaultencoding('utf8')
# print("efwr", sys.getdefaultencoding())
app.config.from_object(__name__)


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
