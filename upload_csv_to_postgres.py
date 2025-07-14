import psycopg2
import pandas as pd

PG_URI = "postgresql://postgres:JVXszdkPsDRqPjXdJcEuGJQuKHyvuKJg@shortline.proxy.rlwy.net:52591/railway"

def upload_csv(table_name, csv_file, columns):
    print(f"[{table_name}] 데이터 업로드 시작...")
    try:
        df = pd.read_csv(csv_file)
        df = df.fillna('')

        if 'contract_period' in df.columns:
            df['contract_period'] = df['contract_period'].astype(str).str.extract(r'(\d+)').astype(int)

        for col in ['rental_fee', 'benefit']:
            if col in df.columns:
                df[col] = df[col].astype(str).str.replace(',', '').astype(float)

        with psycopg2.connect(PG_URI) as conn:
            with conn.cursor() as cur:
                for _, row in df.iterrows():
                    values = [row[col].item() if hasattr(row[col], 'item') else row[col] for col in columns]
                    placeholders = ','.join(['%s'] * len(columns))
                    sql = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({placeholders})"
                    cur.execute(sql, values)
            conn.commit()

        print(f"[{table_name}] 데이터 업로드 완료")
    except Exception as e:
        print(f"에러 발생: {e}")

def upload_prices():
    upload_csv(
        "prices",
        "prices_with_id.csv",
        ["product_id", "company_id", "contract_period", "rental_fee", "benefit"]
    )

if __name__ == "__main__":
    upload_prices()