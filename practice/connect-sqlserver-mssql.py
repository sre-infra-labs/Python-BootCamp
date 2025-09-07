import os
import pyodbc
import socket

# Get connection info from environment
host = os.getenv("MSSQL_HOST", "localhost")
port = os.getenv("MSSQL_PORT", "1433")
user = os.getenv("MSSQL_USER", "sa")
password = os.getenv("MSSQL_PASSWORD")
dbname = os.getenv("MSSQL_DB", "master")

if not password:
    raise Exception("Environment variable MSSQL_PASSWORD is not set.")

# Construct connection string
conn_str = (
    f"DRIVER={{ODBC Driver 18 for SQL Server}};"
    f"SERVER={host},{port};"
    f"DATABASE={dbname};"
    f"UID={user};"
    f"PWD={password};"
    f"ApplicationIntent=ReadOnly;"
    f"Encrypt=yes;"         # Enforce SSL encryption
    f"TrustServerCertificate=yes;"  # Skip certificate validation (set to 'no' in prod with CA)
)

try:
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()

    # Get SQL Server version and hostname
    cursor.execute(f"SELECT '{host}' as srv_ip, @@servername as srv_name, @@VERSION AS version, SUSER_SNAME() AS username;")
    row = cursor.fetchone()

    print("✅ Connected to SQL Server.")
    # print(f"row => {row}")
    print(f"🔹 Connection IP : {row.srv_ip}")
    print(f"🔹 SQL Server Name : {row.srv_name}")
    print(f"🔹 SQL Server Version : {row.version}")
    print(f"🔹 Connected As User  : {row.username}")

    # Resolve actual IP of SQL Server
    resolved_ip = socket.gethostbyname(host)
    print(f"🔹 Server IP Address  : {resolved_ip}")

    conn.close()

except Exception as e:
    print(f"❌ Connection failed: {e}")