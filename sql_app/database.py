import os
import psycopg2

from dotenv import load_dotenv

load_dotenv()


def get_data_from_db():
    conn = psycopg2.connect(
        host=os.getenv('POSTGRES_HOST'),
        database=os.getenv('POSTGRES_DATABASE'),
        user=os.getenv('POSTGRES_USER'),
        password=os.getenv('POSTGRES_PASSWORD')
    )
    cur = conn.cursor()
    try:
        cur.execute("""
            SELECT order_id, customer_id, contact_name
            FROM orders
            JOIN customers USING (customer_id)
            LIMIT 10
            """)
    except psycopg2.Error as e:
        return e.diag.message_primary
    data = cur.fetchall()
    cur.close()
    conn.close()
    return data
