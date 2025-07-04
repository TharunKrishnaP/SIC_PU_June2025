import pymysql

def connect_db(pass_word,data_base):
    connection = None
    try:
        connection = pymysql.Connect(host="localhost", user="root",\
                                 password=pass_word,database=data_base,port=3306,charset="utf8")
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
    connection = connect_db(pass_word,data_base)
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
        designation varchar(30), phone_number bigint unique, salary float, commission float default(0) \
            years_of_experience tinyint, technology varchar(30) not null)"
    connection = connect_db(pass_word,data_base)
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
    connection = connect_db(pass_word,data_base)
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
pass_word = input("Enter password: ")
data_base = input("Enter database name: ")


def read_employee_details():
    name = input("Name: ")
    designation = input("Designation: ")
    phone_number = input("Phone number: ")
    salary = float(input("Salary: "))
    commission = float(input("Commission: "))
    years_of_experience = int(input("Years of Experience: "))
    technology = input("Technology: ")
    return name, designation, phone_number, salary, commission, years_of_experience, technology

def commit(connection):
    input_str = input("Commit? [y/n]").lower()
    if input_str == "y":
        connection.commit()
        print("Changes committed")

def insert_employee():
    details = read_employee_details()
    query = "INSERT INTO EMPLOYEE (NAME,DESIGNATION,PHONE_NUMBER,SALARY,COMMISSION,YEARS_OF_EXPERIENCE,TECHNOLOGY) VALUES(%s, %s, %s, %s, %s, %s,%s)"
    connection = connect_db(pass_word,data_base)
    try:
        cursor = connection.cursor()
        cursor.execute(query,details)
        commit(connection)
        cursor.close()
        disconnect_db(connection)
        print("Insertion successful")
    except:
        print("Insertion failed")

def delete_employee():
    query = "delete from employee where id = %s"
    connection = connect_db(pass_word,data_base)
    try:
        cursor = connection.cursor()
        id = input("Enter id: ")
        cursor.execute(query,id)
        commit(connection)
        cursor.close()
        disconnect_db(connection)
        
    except:
        print("Deletion failed")

create_table()
delete_employee()
insert_employee()