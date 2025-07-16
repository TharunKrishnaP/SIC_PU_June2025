import pymysql

def connect_db():
    connection = None
    try:
        connection = pymysql.Connect(host="localhost", user="root",\
                                 password="SIC@LT02",database="delivery_data",port=3306,charset="utf8")
        print("Database Connected")
    except Exception as e:
        print(f"Connection failed: {e}")
    return connection

def disconnect_db(connection):
    try:
        connection.close()
        print("Disconnected successfully")
    except:
        print("Failed to disconnect")

def read_table(table_name):
    connection = connect_db()
    if connection is None:
        print("Unable to read table. No database connection.")
        return

    query = f"SELECT * FROM `{table_name}`"
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        print("Data retrieved")
        return rows
        cursor.close()
        disconnect_db(connection)
    except Exception as e:
        print(f"Failed to retrieve: {e}")