import pandas as pd

prices_file = "prices.csv"
products_file = "products_with_id.csv"
companies_file = "rental_companies_with_id.csv"
output_file = "prices_with_id.csv"

prices = pd.read_csv(prices_file)
products = pd.read_csv(products_file)
companies = pd.read_csv(companies_file)

# products 이름 -> id 매핑
product_name_to_id = dict(zip(products["name"], products["id"]))
# companies 이름 -> id 매핑
company_name_to_id = dict(zip(companies["company"], companies["id"]))

# 매핑 안되는 경우는 -1 처리 (확인용)
prices["product_id"] = prices["name"].map(product_name_to_id).fillna(-1).astype(int)
prices["company_id"] = prices["company"].map(company_name_to_id).fillna(-1).astype(int)

# 컬럼명 DB형에 맞게 변경 및 순서 조정
prices = prices.rename(columns={
    "contract_period": "contract_period",
    "rental_fee": "rental_fee",
    "benefit": "benefit"
})

# id 컬럼 추가
prices.insert(0, "id", range(1, len(prices) + 1))

# 필요한 컬럼만 선택해서 저장 (id, product_id, company_id, contract_period, rental_fee, benefit)
prices = prices[["id", "product_id", "company_id", "contract_period", "rental_fee", "benefit"]]

prices.to_csv(output_file, index=False, encoding="utf-8-sig")
print(f"prices_with_id.csv 생성 완료: {output_file}")