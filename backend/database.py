import os

try:
    import psycopg2
except ImportError:
    psycopg2 = None  # in case it's not installed

DATABASE_URL = os.environ.get("DATABASE_URL")

def get_db_connection():
    """Establish a connection to PostgreSQL if configured."""
    if not DATABASE_URL:
        print("⚠️ DATABASE_URL is not set. Returning None (mock DB connection).")
        return None

    if not psycopg2:
        print("⚠️ psycopg2 not available. Returning None.")
        return None

    try:
        return psycopg2.connect(DATABASE_URL)
    except psycopg2.OperationalError as e:
        print(f"❌ Database connection failed: {e}")
        return None
