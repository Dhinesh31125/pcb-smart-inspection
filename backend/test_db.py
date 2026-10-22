
import os
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL

# Read the database password from an environment variable.
db_password = os.getenv("PCB_DB_PASSWORD")

if not db_password:
    raise RuntimeError("PCB_DB_PASSWORD environment variable is not set.")

# Build the MySQL connection URL safely.
connection_url = URL.create(
    drivername="mysql+pymysql",
    username="root",
    password=db_password,
    host="localhost",
    port=3306,
    database="pcb_inspection",
)

engine = create_engine(connection_url)

try:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT DATABASE(), VERSION()"))
        database, version = result.one()

        print("Connection successful!")
        print("Database:", database)
        print("MySQL version:", version)
finally:
    engine.dispose()
