import os
import csv
import json
from app.database import get_connection
from app.config import CSV_DIR, CSV_FILE, BATCH_SIZE

def import_users():
    file_path = os.path.join(CSV_DIR, CSV_FILE)

    if not os.path.exists(file_path):
        return {"error": f"CSV file not found at {file_path}"}

    inserted_count = 0

    # Connect to PostgreSQL
    conn = get_connection()
    cur = conn.cursor()

    with open(file_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        batch = []

        for row in reader:
            # Mandatory fields
            first_name = row.pop("name.firstName", "").strip()
            last_name = row.pop("name.lastName", "").strip()
            age = int(row.pop("age", 0))
            name = f"{first_name} {last_name}"

            address = {}
            additional_info = {}

            # Split row into address and additional_info
            for key, value in row.items():
                if key.startswith("address."):
                    # Nested address fields
                    nested_keys = key.split(".")[1:]  # remove 'address'
                    d = address
                    for nk in nested_keys[:-1]:
                        if nk not in d:
                            d[nk] = {}
                        d = d[nk]
                    d[nested_keys[-1]] = value.strip()
                else:
                    # Other fields go to additional_info
                    # handle nested fields like contact.email
                    nested_keys = key.split(".")
                    d = additional_info
                    for nk in nested_keys[:-1]:
                        if nk not in d:
                            d[nk] = {}
                        d = d[nk]
                    d[nested_keys[-1]] = value.strip()

            # Add to batch
            batch.append((name, age, json.dumps(address), json.dumps(additional_info)))

            # Insert batch when batch size reached
            if len(batch) >= BATCH_SIZE:
                insert_batch(cur, batch)
                inserted_count += len(batch)
                batch = []

        # Insert remaining rows
        if batch:
            insert_batch(cur, batch)
            inserted_count += len(batch)

    conn.commit()
    cur.close()
    conn.close()

    return {"message": f"CSV imported successfully! Total records: {inserted_count}"}


def insert_batch(cur, batch):
    """Helper function to insert batch of users"""
    cur.executemany("""
        INSERT INTO users (name, age, address, additional_info)
        VALUES (%s, %s, %s, %s)
    """, batch)
