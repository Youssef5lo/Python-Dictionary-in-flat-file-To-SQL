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
