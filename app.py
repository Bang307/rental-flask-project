import sqlite3
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

DB_PATH = 'rental_data.db'

def query_db(query, args=(), one=False):
    with sqlite3.connect(DB_PATH) as conn:
        conn.row_factory = sqlite3.Row
        cur = conn.execute(query, args)
        rv = cur.fetchall()
        return (rv[0] if rv else None) if one else [dict(row) for row in rv]

@app.route('/products')
def get_products():
    return jsonify(query_db("SELECT * FROM products"))

@app.route('/rental_companies')
def get_rental_companies():
    return jsonify(query_db("SELECT * FROM rental_companies"))

@app.route('/prices')
def get_prices():
    return jsonify(query_db("SELECT * FROM prices"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)