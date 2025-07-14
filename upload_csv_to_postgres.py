import psycopg2
import pandas as pd

# Railway PostgreSQL 접속 URI 입력하세요
PG_URI = "postgresql://postgres:JVXszdkPsDRqPjXdJcEuGJQuKHyvuKJg@shortline.proxy.rlwy.net:52591/railway"

def upload_csv(table_name, csv_file, columns):
    print(f"[{table_name}] 데이터 업로드 시작...")
    try:
        df = pd.read_csv(csv_file)
        df = df.fillna('')  # 빈 값은 빈 문자열로 대체

        with psycopg2.connect(PG_URI) as conn:
            with conn.cursor() as cur:
                for _, row in df.iterrows():
                    values = [row[col] for col in columns]
                    placeholders = ','.join(['%s'] * len(columns))
                    sql = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({placeholders})"
                    cur.execute(sql, values)
            conn.commit()

        print(f"[{table_name}] 데이터 업로드 완료")
    except Exception as e:
        print(f"에러 발생: {e}")

def upload_products():
    upload_csv(
        "products",
        "products_with_id.csv",
        ["id", "name", "model", "brand", "main_category", "sub_category", "image_url", "detail_url", "options"]
    )

def upload_rental_companies():
    upload_csv(
        "rental_companies",
        "rental_companies_with_id.csv",
        ["id", "company", "logo_url"]
    )

def upload_prices():
    upload_csv(
        "prices",
        "prices.csv",
        ["product_id", "company_id", "contract_period", "rental_fee", "benefit"]
    )

if __name__ == "__main__":
    # 올릴 테이블에 해당하는 함수 주석 해제해서 사용하세요

    # upload_products()
    # upload_rental_companies()
     upload_prices()