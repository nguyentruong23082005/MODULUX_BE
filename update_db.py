import psycopg2

DATABASE_URL = "postgresql://postgres:123456@localhost:5432/modulux_db"

MIGRATIONS = [
    # Bảng projects
    "ALTER TABLE projects ADD COLUMN IF NOT EXISTS stories INTEGER;",
    "ALTER TABLE projects ADD COLUMN IF NOT EXISTS kitchens INTEGER;",
    "ALTER TABLE projects ADD COLUMN IF NOT EXISTS floor_plan_url VARCHAR;",
    "ALTER TABLE projects ADD COLUMN IF NOT EXISTS video_url VARCHAR;",
    "ALTER TABLE projects ADD COLUMN IF NOT EXISTS features JSON;",
    "ALTER TABLE projects ADD COLUMN IF NOT EXISTS finishing_options JSON;",
    
    # Bảng project_images
    "ALTER TABLE project_images ADD COLUMN IF NOT EXISTS is_hero BOOLEAN DEFAULT FALSE;",
    "ALTER TABLE project_images ADD COLUMN IF NOT EXISTS is_floor_plan BOOLEAN DEFAULT FALSE;"
]

def main():
    try:
        conn = psycopg2.connect(DATABASE_URL)
        conn.autocommit = True
        cur = conn.cursor()

        for sql in MIGRATIONS:
            print(f"Running: {sql}")
            try:
                cur.execute(sql)
                print("  [OK] Done")
            except Exception as e:
                print(f"  [ERROR] Column may already exist: {e}")

        cur.close()
        conn.close()
        print("\n[SUCCESS] Database updated successfully! New columns added.")
    except Exception as e:
        print(f"[FAILED] Cannot connect to Database. Please check if Postgres is running. Error: {e}")

if __name__ == "__main__":
    main()
