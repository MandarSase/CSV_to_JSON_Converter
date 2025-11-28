import os
from app.config import CSV_DIR, CSV_FILE

def read_csv():
    path = os.path.join(CSV_DIR, CSV_FILE)
    
    with open(path, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    headers = [h.strip() for h in lines[0].split(",")]

    records = []
    for line in lines[1:]:
        values = [v.strip() for v in line.split(",")]
        records.append(dict(zip(headers, values)))

    return records
