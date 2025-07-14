import pandas as pd

# 원본 파일 경로
input_file = "products.csv"
output_file = "products_with_id.csv"

df = pd.read_csv(input_file)

# id 컬럼 추가 (자동 증가 번호)
df.insert(0, "id", range(1, len(df) + 1))

# 컬럼명 변경 (DB컬럼명에 맞게 변경)
df = df.rename(columns={
    "name": "name",
    "model": "model",
    "brand": "brand",
    "main_category": "main_category",
    "sub_category": "sub_category",
    "image_url": "image_url",
    "detail_url": "detail_url",
    "options": "options"
})

df.to_csv(output_file, index=False, encoding="utf-8-sig")
print(f"products_with_id.csv 생성 완료: {output_file}")