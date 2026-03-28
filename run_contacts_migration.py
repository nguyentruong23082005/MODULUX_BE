"""
Script migration thêm cột cho bảng contacts hỗ trợ 3 loại enquiry.
Chạy: python run_contacts_migration.py
"""
import psycopg2

DATABASE_URL = "postgresql://postgres:123456@localhost:5432/modulux_db"

MIGRATIONS = [
    # Phân loại form
    "ALTER TABLE contacts ADD COLUMN IF NOT EXISTS enquiry_type VARCHAR DEFAULT 'general';",
    # Trường chung
    "ALTER TABLE contacts ADD COLUMN IF NOT EXISTS country_code VARCHAR;",
    # Project Enquiry fields
    "ALTER TABLE contacts ADD COLUMN IF NOT EXISTS building_type VARCHAR;",
    "ALTER TABLE contacts ADD COLUMN IF NOT EXISTS living_units VARCHAR;",
    "ALTER TABLE contacts ADD COLUMN IF NOT EXISTS area VARCHAR;",
    "ALTER TABLE contacts ADD COLUMN IF NOT EXISTS arrange_tour BOOLEAN DEFAULT FALSE;",
    "ALTER TABLE contacts ADD COLUMN IF NOT EXISTS preferred_day VARCHAR;",
    "ALTER TABLE contacts ADD COLUMN IF NOT EXISTS preferred_time VARCHAR;",
    "ALTER TABLE contacts ADD COLUMN IF NOT EXISTS file_url VARCHAR;",
    # General Enquiry fields
    "ALTER TABLE contacts ADD COLUMN IF NOT EXISTS get_brochure BOOLEAN DEFAULT FALSE;",
]


def main():
    conn = psycopg2.connect(DATABASE_URL)
    conn.autocommit = True
    cur = conn.cursor()

    for sql in MIGRATIONS:
        print(f"Running: {sql}")
        cur.execute(sql)
        print("  ✓ Done")

    cur.close()
    conn.close()
    print("\n✅ Contacts migration completed successfully!")


if __name__ == "__main__":
    main()
