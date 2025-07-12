from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 이 한 줄이면 모든 도메인에서 접근 가능

# 예시 엔드포인트
@app.route("/products")
def get_products():
    # DB 또는 샘플 데이터 불러와서 리턴
    ...
    return jsonify(products)

@app.route("/prices")
def get_prices():
    ...
    return jsonify(prices)

@app.route("/rental_companies")
def get_companies():
    ...
    return jsonify(companies)

# 신청(post) 예시
@app.route("/applications", methods=["POST"])
def post_application():
    data = request.json
    print("신청 데이터:", data)
    # 실제로 DB에 저장하려면 이곳에 코드 추가
    return jsonify({"status": "ok"})
