import os
import json
import pyodbc

# Connecting to SQL Server
def connect_to_db():
    try:
        conn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=localhost\\SQLExpress;'
            'DATABASE=UserDatabase;'
            'Trusted_Connection=yes;'
        )

        return conn
    except pyodbc.Error as e:
        print(f"Error connecting to SQL Server: {e}")
        return None


file_name = 'user_data.txt'

# Check if the file exists
if not os.path.isfile(file_name):
    # Create the file if it doesn't exist
    with open(file_name, 'w') as file:
        pass
    print(f"{file_name} created.")
else:
    print(f"{file_name} already exists.")


# Load data from the file into a dictionary
def load_data(file_name):
    if os.path.getsize(file_name) > 0:  # Check if the file is not empty
        with open(file_name, 'r') as file:
            try:
                data = json.load(file)
                return data
            except json.JSONDecodeError as e:
                print(f"Error loading data: {e}")
                return {}
    else:
        return {}

user_data = load_data(file_name)
print("Loaded data:", user_data)


# User Input, Validation, and Data Storage
def is_valid_user_id(user_id, user_data):
    # Check if user_id is a digit, has exactly 3 digits, and does not already exist in the data
    return user_id.isdigit() and len(user_id) == 3 and user_id not in user_data

def is_valid_name(name):
    return name.isalpha()

def is_valid_age(age):
    return age.isdigit() and int(age) > 0

def is_valid_gender(gender):
    return gender in ['Male', 'Female', 'Other']

def is_valid_year_of_birth(year_of_birth):
    current_year = 2024
    return year_of_birth.isdigit() and 1900 <= int(year_of_birth) <= (current_year - 18)

def collect_user_data(user_data):
    while True:
        user_id = input("Enter User ID: ")
        if not is_valid_user_id(user_id, user_data):
            print("Invalid or duplicate User ID. Try again.")
            continue

        first_name = input("Enter First Name: ")
        if not is_valid_name(first_name):
            print("Invalid First Name. Try again.")
            continue

        last_name = input("Enter Last Name: ")
        if not is_valid_name(last_name):
            print("Invalid Last Name. Try again.")
            continue

        age = input("Enter Age: ")
        if not is_valid_age(age):
            print("Invalid Age. Try again.")
            continue

        gender = input("Enter Gender (Male/Female/Other): ")
        if not is_valid_gender(gender):
            print("Invalid Gender. Try again.")
            continue

        year_of_birth = input("Enter Year of Birth: ")
        if not is_valid_year_of_birth(year_of_birth):
            print("Invalid Year of Birth. Try again.")
            continue

        return {
            "user_id": user_id,
            "first_name": first_name,
            "last_name": last_name,
            "age": int(age),
            "gender": gender,
            "year_of_birth": int(year_of_birth)
        }


# Insert Data into SQL Database
def insert_into_db(user_info):
    try:
        conn = connect_to_db()
        if conn is None:
            return

        cursor = conn.cursor()
        insert_query = """
        INSERT INTO Users (user_id, first_name, last_name, age, gender, year_of_birth)
        VALUES (?, ?, ?, ?, ?, ?)
        """
        cursor.execute(insert_query, (user_info['user_id'], user_info['first_name'], user_info['last_name'], user_info['age'], user_info['gender'], user_info['year_of_birth']))
        conn.commit()
        cursor.close()
        conn.close()
        print("Data inserted successfully into the database.")
    except pyodbc.Error as e:
        print(f"Error inserting data into SQL Server: {e}")


# Check if User ID exists in the SQL Database
def check_user_id_in_db(user_id):
    try:
        conn = connect_to_db()
        if conn is None:
            return False

        cursor = conn.cursor()
        check_query = "SELECT 1 FROM Users WHERE user_id = ?"
        cursor.execute(check_query, (user_id,))
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return result is not None
    except pyodbc.Error as e:
        print(f"Error checking User ID in SQL Server: {e}")
        return False


# Save Data to the File
def save_data_to_file(file_name, user_data):
    try:
        with open(file_name, 'w') as file:
            json.dump(user_data, file, indent=4)
        print("Data saved successfully to file.")
    except IOError as e:
        print(f"Error saving data to file: {e}")


# Main Program Flow

user_info = collect_user_data(user_data)

# Check if User ID already exists in SQL
if check_user_id_in_db(user_info['user_id']):
    print("User ID already exists in the database.")
else:
    # Insert the new user into the SQL database
    insert_into_db(user_info)

    # Store the user data in the text file
    user_data[user_info['user_id']] = {
        "first_name": user_info['first_name'],
        "last_name": user_info['last_name'],
        "age": user_info['age'],
        "gender": user_info['gender'],
        "year_of_birth": user_info['year_of_birth']
    }
    save_data_to_file(file_name, user_data)

    print("User data successfully saved.")
