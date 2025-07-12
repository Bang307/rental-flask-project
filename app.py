from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # CORS 허용 (프론트와 연동시 필수)

# 홈
@app.route("/")
def home():
    return "Hello, Flask! 서버 정상 실행중"

# 제품 리스트 예시 API
@app.route("/products")
def get_products():
    products = [
        {"id": 1, "name": "상품1", "price": 10000},
        {"id": 2, "name": "상품2", "price": 20000},
        {"id": 3, "name": "상품3", "price": 30000},
    ]
    return jsonify(products)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
