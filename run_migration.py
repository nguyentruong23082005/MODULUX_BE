"""
Script chạy migration thêm cột CMS cho bảng banners.
Chạy: python run_migration.py
"""
import psycopg2

DATABASE_URL = "postgresql://postgres:123456@localhost:5432/modulux_db"

MIGRATIONS = [
    "ALTER TABLE banners ADD COLUMN IF NOT EXISTS subtitle VARCHAR;",
    "ALTER TABLE banners ADD COLUMN IF NOT EXISTS description TEXT;",
    "ALTER TABLE banners ADD COLUMN IF NOT EXISTS image_url VARCHAR;",
    "ALTER TABLE banners ADD COLUMN IF NOT EXISTS cta_text VARCHAR DEFAULT 'Learn more';",
    "ALTER TABLE banners ADD COLUMN IF NOT EXISTS cta_link VARCHAR DEFAULT '/about';",
    'ALTER TABLE banners ADD COLUMN IF NOT EXISTS "order" INTEGER DEFAULT 0;',
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
    print("\n✅ All migrations completed successfully!")

if __name__ == "__main__":
    main()
