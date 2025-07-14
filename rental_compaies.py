import pandas as pd

input_file = "rental_companies.csv"
output_file = "rental_companies_with_id.csv"

df = pd.read_csv(input_file)

df.insert(0, "id", range(1, len(df) + 1))

df = df.rename(columns={
    "company": "company",
    "logo_url": "logo_url"
})

df.to_csv(output_file, index=False, encoding="utf-8-sig")
print(f"rental_companies_with_id.csv 생성 완료: {output_file}")