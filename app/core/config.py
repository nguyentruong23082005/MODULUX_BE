import os
from dotenv import load_dotenv

load_dotenv()

# Database
DATABASE_URL = os.getenv(
  "DATABASE_URL",
  "postgresql://postgres:password@localhost:5432/modulux_db"
)

# JWT Authentication
SECRET_KEY = os.getenv("SECRET_KEY", "yoursecretkeyhere")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(
  os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "1440")
)

# CORS
CORS_ORIGINS = os.getenv("CORS_ORIGINS", "*").split(",")
