"""
Script migration cho bang videos de ho tro Video CMS day du.
Chay: python run_video_cms_migration.py
"""

import psycopg2

DATABASE_URL = "postgresql://postgres:123456@localhost:5432/modulux_db"

MIGRATIONS = [
    "ALTER TABLE videos ADD COLUMN IF NOT EXISTS location VARCHAR DEFAULT 'home';",
    "ALTER TABLE videos ADD COLUMN IF NOT EXISTS poster_url VARCHAR;",
    "ALTER TABLE videos ADD COLUMN IF NOT EXISTS thumbnail_label VARCHAR;",
    "ALTER TABLE videos ADD COLUMN IF NOT EXISTS is_active BOOLEAN DEFAULT TRUE;",
    "UPDATE videos SET location = 'home' WHERE location IS NULL OR location = '' OR location NOT IN ('home', 'faq', 'both');",
    "UPDATE videos SET poster_url = COALESCE(NULLIF(poster_url, ''), thumbnail_url) WHERE poster_url IS NULL OR poster_url = '';",
    "UPDATE videos SET thumbnail_label = COALESCE(NULLIF(thumbnail_label, ''), title, 'Video') WHERE thumbnail_label IS NULL OR thumbnail_label = '';",
    "UPDATE videos SET is_active = TRUE WHERE is_active IS NULL;",
    "CREATE INDEX IF NOT EXISTS idx_videos_active_order ON videos (is_active, display_order);",
    "CREATE INDEX IF NOT EXISTS idx_videos_location_active_order ON videos (location, is_active, display_order);",
]


def main():
    try:
        conn = psycopg2.connect(DATABASE_URL)
        conn.autocommit = True
        cur = conn.cursor()

        for sql in MIGRATIONS:
            print(f"Running: {sql}")
            cur.execute(sql)
            print("  Done")

        cur.close()
        conn.close()
        print("\nVideo CMS migration completed successfully!")
    except Exception as error:
        print(f"\nVideo CMS migration failed: {error}")


if __name__ == "__main__":
    main()
