import psycopg2

from dotenv import dotenv_values

# Load key-value pairs from .env into a dictionary
config = dotenv_values(".env")

try:
    connection = psycopg2.connect(
        host=config.get("DB_HOST"),
        port="5434",
        user=config.get("DB_USER"),
        password=config.get("DB_PASSWORD"),  # Replace with the actual password
        dbname="invoicedb"
    )
    print("Connection successful!")
    connection.close()
except psycopg2.OperationalError as e:
    print(f"Unable to connect to the database: {e}")
