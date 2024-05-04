import psycopg2
from psycopg2 import Error
import csv

# Function to create a database connection
def create_connection():
    try:
        connection = psycopg2.connect(
            host="localhost", 
            dbname="postgres", 
            user="postgres",
            password="1234qwer", 
            port=5432)  

        return connection
    except Error as e:
        print("Error while connecting to PostgreSQL:", e)
        return None

# Function to create tables
def create_tables(connection):
    create_contacts_table = """
    CREATE TABLE IF NOT EXISTS Contacts (
        contact_id SERIAL PRIMARY KEY,
        first_name VARCHAR(50) NOT NULL,
        last_name VARCHAR(50),
        phone_number VARCHAR(15) NOT NULL,
        email VARCHAR(100),
        address VARCHAR(50)
    )
    """

    #get data from table 
    #get_data = """
    #SELECT last_name FROM contacts WHERE first_name = 'Tamerlan';
    #"""

    try:
        cursor = connection.cursor()
        cursor.execute(create_contacts_table)
        print("[INFO] Tables created successfully.")
        #print(cursor.fetchone())
        #cursor.execute(get_data)
        connection.commit()
    except Error as e:
        print("Error creating tables:", e)

# Function to insert from console
def insert_from_console(connection):
    cursor = connection.cursor()
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    phone_num = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    
    try:
        cursor.execute("INSERT INTO contacts (first_name, last_name, phone_number, email, address) VALUES (%s, %s, %s, %s, %s)", (first_name, last_name, phone_num, email, address))
        connection.commit()
        print("[INFO] Data was successfully inserted")
    except Error as e:
        print("Error insearting data:", e)

# Function to insert from csv
def insert_from_csv(connection, file_path):
    cursor = connection.cursor()

    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header if exists
        for row in reader:
            first_name, last_name, phone_number, email, address = row
            cursor.execute("INSERT INTO contacts (first_name, last_name, phone_number, email, address) VALUES (%s, %s, %s, %s, %s)", (first_name, last_name, phone_number, email, address))

    connection.commit()

# Function to update data 
def update_data(connection):
    cursor = connection.cursor()
    print("UPDATING DATA: ")
    upid = input("ID: ")
    print("What do you want to change?")
    print("Fist name : Last name : Phone number : Email : Address")
    upins = input(":: ")
    if upins == "First name":
        upins = "first_name"
    elif upins == "Last name":
        upins = "last_name"
    elif upins == "Phone number":
        upins = "phone_number"
    elif upins == "Email":
        upins = "email"
    elif upins == "Address":
        upins = "address"
    else: 
        print("Ok, bye")
        exit()
    new_data = input("New data: ")
    cursor.execute(f"UPDATE contacts SET {upins} = %s WHERE contact_id = %s", (new_data, upid)) 
    print("[INFO] Data was successfully updated")

    connection.commit()

# Function to delete data 
def delete_data(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM contacts")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    print("DELETION DATA: ")
    print("Enter an id to DELETE a contact")
    upid = input("ID: ")
    cursor.execute("DELETE FROM contacts WHERE contact_id = %s", (upid))
    print("[INFO] Data was successfully deleted")

    connection.commit()

def insert_user(connection):
    cursor = connection.cursor()
    first_name = input("Enter first name: ")
    cursor.execute("SELECT EXISTS(SELECT first_name FROM contacts WHERE first_name = %s)",(first_name,))
    exists = cursor.fetchone()[0]
    if exists:
        update_data(connection)
    else:
        insert_from_console(connection)
    
    connection.commit()

def print_table(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM contacts")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def get_paginated_data(connection):
    cursor = connection.cursor()
    table_name = "contacts"
    limit = input("Enter limit: ")
    offset = input("Enter offset: ")
    cursor.execute("SELECT * FROM contacts LIMIT %s OFFSET %s", (limit, offset))
    result = cursor.fetchall()
    for row in result:
        print(row)

# Main function
def main():
    # Create a database connection
    connection = create_connection()
    if connection is not None:
        # Create tables
        create_tables(connection)
        csv_file_path = 'data.csv' 
        #choise action
        ins = input("Select action: csv/console/ins user/show table/update data/get/delete contact? Or press to any bottom: ")
        if ins == "csv":
            insert_from_csv(connection, csv_file_path)
        elif ins == "console":
            insert_from_console(connection)
        elif ins == "update dataupdate":
            update_data(connection)
        elif ins == "delete contact":
            delete_data(connection)
        elif ins == "ins user":
            insert_user(connection)
        elif ins == "show table":
            print_table(connection)
        elif ins == "get":
            get_paginated_data(connection)
        else:
            print("Ok, bye")

        # Close the connection
        connection.close()
    else:
        print("Failed to connect to PostgreSQL.")

if __name__ == "__main__":
    main()
