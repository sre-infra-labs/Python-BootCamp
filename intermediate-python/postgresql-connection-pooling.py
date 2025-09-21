import os
import time
import threading
from psycopg2 import pool, OperationalError

# Get password from environment variable
pg_password = os.environ.get("PGPASSWORD")
if not pg_password:
    raise ValueError("Environment variable PGPASSWORD is not set")

# Set up the connection pool
try:
    connection_pool = pool.ThreadedConnectionPool(
        minconn=1,
        maxconn=3,  # Limit total concurrent connections
        user="postgres",
        password=pg_password,
        host="localhost",
        port="5432",
        database="postgres"
    )
    print("Connection pool created successfully")
except OperationalError as e:
    print(f"Error creating pool: {e}")
    exit()

# Function that uses a connection from the pool
def use_connection(task_id):
    conn = None  # Ensure conn is defined
    try:
        print(f"Task {task_id} acquiring connection")
        conn = connection_pool.getconn()
        if conn:
            print(f"Task {task_id} acquired a connection")
            with conn.cursor() as cur:
                cur.execute("SELECT now()")
                result = cur.fetchone()
                print(f"Task {task_id} got time: {result[0]}")
        else:
            print(f"Task {task_id} failed: connection pool exhausted")
    except Exception as e:
        print(f"Task {task_id} failed: {e}")
    finally:
        if conn:
            connection_pool.putconn(conn)
            print(f"Task {task_id} released the connection")

# Simulate concurrent usage
threads = []
for i in range(6):
    t = threading.Thread(target=use_connection, args=(i,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

# Close pool
connection_pool.closeall()
print("All connections closed.")