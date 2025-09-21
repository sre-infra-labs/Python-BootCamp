import os
import psycopg2
import socket

# Get values from environment variables
host = os.getenv("PGHOST", "localhost")
port = int(os.getenv("PGPORT", "5432"))
user = os.getenv("PGUSER", "postgres")
password = os.getenv("PGPASSWORD")
dbname = os.getenv("PGDATABASE", "postgres")

if not password:
    raise Exception("Environment variable PGPASSWORD is not set.")

# Connection parameters
conn_params = {
    "host": host,
    "port": port,
    "dbname": dbname,
    "user": user,
    "password": password,
    "sslmode": "require",  # Enforce SSL encryption
    # Optional: "sslrootcert": "/path/to/ca.pem" if needed
}

try:
    # Connect to PostgreSQL over SSL
    conn = psycopg2.connect(**conn_params)
    cur = conn.cursor()

    # Get PostgreSQL version
    cur.execute("SELECT inet_server_addr() AS server_ip, inet_server_port() AS server_port, version() AS server_version, name, setting, short_desc, vartype from pg_settings where name = 'ssl';")
    print("✅ Connected to PostgreSQL server.")

    row = cur.fetchone()

    # print(f"Type of row: {type(row)}")
    print(f"metadata row => {row}")
    print(f"🔹 Server IP Address   : {row[0]}")
    print(f"🔹 PostgreSQL Version : {row[2]}")
    print(f"🔹 SSL Encryption Used: {row[4]}")

    # Get current connection details
    cur.execute("SELECT pid, ssl, version, cipher FROM pg_stat_ssl WHERE pid = pg_backend_pid();")
    row = cur.fetchone()

    print(f"encryption row => {row}")
    print(f'Encrypted Connection: {row[1]}')
    print(f'Encryption Type: {row[2]}')
    print(f'Encrypted Algorithm: {row[3]}')

    cur.close()
    conn.close()

except Exception as e:
    print(f"❌ Connection failed: {e}")