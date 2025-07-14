import pandas as pd

# products_with_id.csv에는 'id'와 'name' 컬럼이 있어야 함
products = pd.read_csv("products_with_id.csv")
prices = pd.read_csv("prices.csv")

# products의 이름과 id를 dict로 매핑
name_to_id = dict(zip(products['name'], products['id']))

# prices CSV 내 'name' 컬럼을 'product_id'로 변환
prices['product_id'] = prices['name'].map(name_to_id)

# 매핑되지 않은 행 확인
missing = prices[prices['product_id'].isnull()]
if not missing.empty:
    print("매핑 안 된 제품명:\n", missing['name'])

# 필요한 컬럼으로 재구성
prices_fixed = prices[['product_id', 'company_id', 'contract_period', 'rental_fee', 'benefit']]

# 저장
prices_fixed.to_csv("prices_fixed.csv", index=False)