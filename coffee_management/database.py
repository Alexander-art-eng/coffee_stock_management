# database.py
"""
Database module: Handles database connection and queries.
"""

import mysql.connector
from dotenv import load_dotenv
import os

# Load environment from .env
load_dotenv()

# Acess the environment variables
db_host = os.getenv('DB_HOST')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')

# Database connection function
def connect_to_db():
    """
    Connects to the MySQL database.
    Returns:
        connection: A MySQL database connection object.
    """
    return mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )

def execute_query(query, params=None, fetch=False):
    """
    Executes a database query.
    Args:
        query (str): SQL query to execute.
        params (tuple, optional): Parameters for the query.
        fetch (bool, optional): Whether to fetch results. Defaults to False.
    Returns:
        list/dict: Fetched results if fetch is True, else None.
    """
    connection = connect_to_db()
    cursor = connection.cursor(dictionary=True) if fetch else connection.cursor()

    try:
        cursor.execute(query, params)
        if fetch:
            results = cursor.fetchall()
            return results
        else:
            connection.commit()
    finally:
        cursor.close()
        connection.close()

def fetch_one(query, params=None):
    """
    Fetches a single row from the database.
    Args:
        query (str): SQL query to execute.
        params (tuple, optional): Parameters for the query.
    Returns:
        dict: Fetched row as a dictionary.
    """
    results = execute_query(query, params, fetch=True)
    return results[0] if results else None
