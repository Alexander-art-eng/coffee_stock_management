# database.py
"""
Database module: Handles database connection and queries.
"""

import mysql.connector

# Database connection function
def connect_to_db():
    """
    Connects to the MySQL database.
    Returns:
        connection: A MySQL database connection object.
    """
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="sA!EXAyLP2@m59x%GPE9",
        database="coffee_stock_db"
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
