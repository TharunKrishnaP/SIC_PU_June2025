import pymysql

def connect_db():
    connection = None
    try:
        connection = pymysql.Connect(host="localhost", user="root",\
                                 password="Bumblebee",database="EMP_DB",port=3306,charset="utf8")
        print("Database Connected")
    except:
        print("Connection failed")
    return connection

def disconnect_db(connection):
    try:
        connection.close()
        print("Disconnected successfully")
    except:
        print("Failed to disconnect")

def create_db():
    query = "create database IF NOT EXISTS emp_db"
    connection = connect_db()
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        print("Database created")
        cursor.close()
        disconnect_db(connection)
    except:
        print("Database exists")

def create_table():
    query = "create table IF NOT EXISTS employee(id int primary key auto_increment, name varchar(30) not null\
        designation varchar(30), phone_no bigint unique, salary float, commission float default(0) \
            years_of_exp tinyint, technology varchar(30) not null)"
    connection = connect_db()
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        print("Table created")
        cursor.close()
        disconnect_db(connection)
    except:
        print("Table exists")

def read_all_employees():
    query = "select * from employee"
    connection = connect_db()
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        for i in rows:
            print(i)
        print("Data retrieved")
        cursor.close()
        disconnect_db(connection)
    except:
        print("Failed to retrieve")
