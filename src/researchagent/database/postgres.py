import os
import psycopg
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:postgres@localhost:5432/shod"
)


def get_connection():
    return psycopg.connect(DATABASE_URL)


if __name__ == "__main__":
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT version();")
            version = cursor.fetchone()

            print("PostgreSQL connected ✅")
            print(version[0]) # type: ignore