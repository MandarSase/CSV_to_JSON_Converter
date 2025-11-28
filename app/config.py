import os
from dotenv import load_dotenv

load_dotenv()

PG_HOST = os.getenv("PG_HOST")
PG_PORT = os.getenv("PG_PORT")
PG_USER = os.getenv("PG_USER")
PG_PASSWORD = os.getenv("PG_PASSWORD")
PG_DATABASE = os.getenv("PG_DATABASE")

CSV_DIR = os.getenv("CSV_DIR")
CSV_FILE = os.getenv("CSV_FILE")
BATCH_SIZE = int(os.getenv("BATCH_SIZE"))
