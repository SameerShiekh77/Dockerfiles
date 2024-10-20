import psycopg2
from psycopg2 import sql

# Connect to PostgreSQL
def connect_to_db():
    try:
        conn = psycopg2.connect(
            dbname="docker",
            user="docker",
            password="docker",
            host="localhost"
        )
        return conn
    except Exception as error:
        print(f"Error connecting to the database: {error}")
        return None

# Create a table
def create_table(conn):
    try:
        cur = conn.cursor()
        create_table_query = '''CREATE TABLE IF NOT EXISTS employees (
                                id SERIAL PRIMARY KEY,
                                name VARCHAR(100),
                                position VARCHAR(100),
                                salary INT
                            );'''
        cur.execute(create_table_query)
        conn.commit()
        print("Table created successfully")
    except Exception as error:
        print(f"Error creating table: {error}")
    finally:
        cur.close()

# Insert data
def insert_data(conn):
    try:
        cur = conn.cursor()
        insert_query = '''INSERT INTO employees (name, position, salary)
                          VALUES (%s, %s, %s);'''
        cur.execute(insert_query, ("John Doe", "Developer", 60000))
        conn.commit()
        print("Data inserted successfully")
    except Exception as error:
        print(f"Error inserting data: {error}")
    finally:
        cur.close()

# Main function
if __name__ == "__main__":
    conn = connect_to_db()
    if conn:
        create_table(conn)
        insert_data(conn)
        conn.close()
