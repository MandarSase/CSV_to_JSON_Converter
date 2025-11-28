import psycopg2
from app.config import PG_HOST, PG_PORT, PG_USER, PG_PASSWORD, PG_DATABASE

def get_connection():
    return psycopg2.connect(
        host=PG_HOST,
        port=PG_PORT,
        user=PG_USER,
        password=PG_PASSWORD,
        database=PG_DATABASE
    )
