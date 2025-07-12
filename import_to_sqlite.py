import pandas as pd
import sqlite3

# 파일 경로
products_file = 'merged_products.xlsx'
prices_file = 'merged_prices.xlsx'
rental_companies_file = 'merged_rental_companies_dedup.xlsx'
db_file = 'rental_data.db'

# DB 연결
conn = sqlite3.connect(db_file)

def add_id_column(df):
    df = df.copy()
    df.insert(0, "id", range(1, len(df)+1))
    return df

# products
df_products = pd.read_excel(products_file)
df_products = add_id_column(df_products)
df_products.to_sql("products", conn, if_exists="replace", index=False)

# prices
df_prices = pd.read_excel(prices_file)
df_prices = add_id_column(df_prices)
df_prices.to_sql("prices", conn, if_exists="replace", index=False)

# rental_companies
df_rental_companies = pd.read_excel(rental_companies_file)
df_rental_companies = add_id_column(df_rental_companies)
df_rental_companies.to_sql("rental_companies", conn, if_exists="replace", index=False)

conn.close()
print("DB 변환 및 id 컬럼 추가 완료!")
