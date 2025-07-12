from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3

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
    rows = query_db("SELECT * FROM products")
    return jsonify(rows)

@app.route('/prices')
def get_prices():
    rows = query_db("SELECT * FROM prices")
    return jsonify(rows)

@app.route('/rental_companies')
def get_rental_companies():
    rows = query_db("SELECT * FROM rental_companies")
    return jsonify(rows)

# 신청 POST 예시
@app.route('/applications', methods=['POST'])
def post_application():
    data = request.json
    # 실제로 저장하려면 insert 쿼리 작성
    print("신청 접수됨:", data)  # 서버 콘솔에 출력만
    return jsonify({"status": "ok", "received": data})

# 헬스체크 (서버 상태 확인용)
@app.route('/')
def health():
    return "Hello, Flask!"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
