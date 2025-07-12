from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('rental_data.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def home():
    return "Hello, Flask API server is running!"

@app.route("/products")
def products():
    conn = get_db_connection()
    products = conn.execute('SELECT * FROM products').fetchall()
    conn.close()
    return jsonify([dict(row) for row in products])

@app.route("/prices")
def prices():
    conn = get_db_connection()
    prices = conn.execute('SELECT * FROM prices').fetchall()
    conn.close()
    return jsonify([dict(row) for row in prices])

@app.route("/rental_companies")
def rental_companies():
    conn = get_db_connection()
    companies = conn.execute('SELECT * FROM rental_companies').fetchall()
    conn.close()
    return jsonify([dict(row) for row in companies])

if __name__ == "__main__":
    app.run(debug=True)
