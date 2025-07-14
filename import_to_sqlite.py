import sqlite3
import pandas as pd

DB_PATH = "rental_data.db"

def csv_to_sqlite(csv_file, table_name):
    df = pd.read_csv(csv_file, encoding='utf-8-sig')
    conn = sqlite3.connect(DB_PATH)
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    conn.close()
    print(f"{table_name} 테이블에 데이터 업로드 완료")

if __name__ == "__main__":
    csv_to_sqlite("products_with_id.csv", "products")
    csv_to_sqlite("rental_companies_with_id.csv", "rental_companies")
    csv_to_sqlite("prices_with_id.csv", "prices")