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

def create_new_database():
    query = "create database IF NOT EXISTS %s"
    connection = connect_db(pass_word,data_base)
    try:
        cursor = connection.cursor()
        cursor.execute(query,data_base)
        print("Database created")
        cursor.close()
        disconnect_db(connection)
    except:
        print("Database exists")

def create_table():
    query = "create table IF NOT EXISTS %s (id int primary key auto_increment, name varchar(30) not null\
        designation varchar(30), phone_number bigint unique, salary float, commission float default(0) \
            years_of_experience tinyint, technology varchar(30) not null)"
    connection = connect_db(pass_word,data_base)
    try:
        table_name = input("Table name: ")
        cursor = connection.cursor()
        cursor.execute(query,table_name)
        print("Table created")
        cursor.close()
        disconnect_db(connection)
    except:
        print("Table exists")

def read_all_employees():
    query = "select * from %s"
    connection = connect_db(pass_word,data_base)
    try:
        table_name = input("Table name: ")
        cursor = connection.cursor()
        cursor.execute(query,table_name)
        rows = cursor.fetchall()
        for i in rows:
            print(i)
        print("Data retrieved")
        cursor.close()
        disconnect_db(connection)
    except:
        print("Failed to retrieve")

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
    table_name = input("Table name: ")
    query = "INSERT INTO %s (NAME,DESIGNATION,PHONE_NUMBER,SALARY,COMMISSION,YEARS_OF_EXPERIENCE,TECHNOLOGY) VALUES(%s, %s, %s, %s, %s, %s,%s)"
    connection = connect_db(pass_word,data_base)
    try:
        cursor = connection.cursor()
        cursor.execute(query,table_name,details)
        commit(connection)
        cursor.close()
        disconnect_db(connection)
        print("Insertion successful")
    except:
        print("Insertion failed")

def delete_employee():
    query = "delete from %s where id = %s"
    table_name = input("Table name: ")
    connection = connect_db(pass_word,table_name,data_base)
    try:
        cursor = connection.cursor()
        id = input("Enter id: ")
        cursor.execute(query,id)
        commit(connection)
        cursor.close()
        disconnect_db(connection)
        
    except:
        print("Deletion failed")

def invalid():
    print("Invalid choice")

pass_word = input("Enter password: ")
data_base = input("Enter database name: ")

menu = {
    1 : create_new_database,
    2: create_table,
    3: read_all_employees,
    4: insert_employee,
    5: delete_employee
}
print("Operations List: ")
for key, value in menu.items():
    print(f"{str(key)} : {value}")

choice = int(input("Enter choice: "))
menu.get(choice,invalid)()