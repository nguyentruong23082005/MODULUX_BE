from app.db.session import engine
from sqlalchemy import text

def drop_table():
    print("Dropping projects table...")
    with engine.begin() as conn:
        conn.execute(text("DROP TABLE IF EXISTS projects CASCADE;"))
        conn.execute(text("DROP TABLE IF EXISTS project_images CASCADE;"))
    print("Projects table dropped successfully! It will be recreated on server startup.")

if __name__ == "__main__":
    drop_table()
