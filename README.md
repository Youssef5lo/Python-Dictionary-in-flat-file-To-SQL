# User Data Management System

## Overview

This project is a Python-based application that handles user data, validates inputs, performs file operations, and stores the data in both a flat file and a Microsoft SQL Server database. The application also provides functionality for retrieving and displaying stored user information.

## Features

- **File Handling**: Checks if a file exists, loads existing data, and creates the file if it doesn't exist.
- **User Input and Validation**: Collects user data with validation for User ID, names, age, gender, and year of birth.
- **Data Storage**: Stores user data in a dictionary and persists it in a flat file (`user_data.txt`) and an SQL database.
- **SQL Integration**: Inserts, retrieves, and displays data from a Microsoft SQL Server database.
- **Error Handling**: Implements robust error handling for file operations, input validation, and SQL operations.
- **Windows Authentication**: Uses Windows Authentication for connecting to the SQL Server.

## Technologies Used

- **Python 3.x**
- **pyodbc**: Python library for connecting to an SQL Server database.
- **Microsoft SQL Server**: Used for data storage and retrieval.
- **JSON**: Used for storing user data in a structured format in a flat file.

## Setup and Installation

### Prerequisites

- Python 3.x installed on your system.
- Microsoft SQL Server installed and running on your local machine or accessible remotely.
- `pyodbc` library installed. You can install it using pip:
  ```sh
  pip install pyodbc
  ```
## Database Setup
Create a database named UserDatabase in your SQL Server.

Create a table named Users using the following schema:

```sql
CREATE DATABASE UserDatabase;
USE UserDatabase;
CREATE TABLE Users (
    user_id VARCHAR(3) PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    age INT,
    gender VARCHAR(50),
    year_of_birth INT
);
```
## Application Setup
Clone the repository:
```sh
git clone https://github.com/Youssef5lo/Python-Dictionary-in-flat-file-To-SQL.git
cd Python-Dictionary-in-flat-file-To-SQL
```
Modify the database connection details in the main.py script to match your SQL Server configuration:

```python
import pyodbc

def connect_to_db():
    try:
        conn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=localhost\\SQLExpress;'  # Adjust this line as necessary
            'DATABASE=UserDatabase;'
            'Trusted_Connection=yes;'
        )
        print("Connection successful!")
        return conn
    except pyodbc.Error as e:
        print(f"Error connecting to SQL Server: {e}")
        return None
```
### Run the application:

```sh
python main.py
```
## Usage
Add User Data: Follow the prompts to enter user details such as User ID, First Name, Last Name, Age, Gender, and Year of Birth. The application will validate the inputs before storing them.
View User Data: Retrieve and display stored data by selecting the appropriate option in the application.
Error Handling: The application will guide you through resolving input errors or connection issues.
## Project Structure
```graphql

.
├── main.py            # Main application script
├── user_data.txt      # Flat file storing user data in JSON format
└── README.md          # Project documentation
```
### Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue if you have any suggestions or improvements.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contact
If you have any questions or feedback, feel free to contact me at youssefmagdy2504@gmail.com.


