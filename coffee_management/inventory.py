# inventory.py
"""
Inventory module: Handles selling and refilling coffee stock.
"""

from coffee_management.database import execute_query, fetch_one

def sold_coffee(coffee_name, size, coffee_type, quantity_sold):
    """
    Sells coffee stock and updates the database.
    """
    if quantity_sold < 0:
        raise ValueError("Quantity sold can't be a negative value")
    if not validate_coffee_details(coffee_name, size, coffee_type):
        raise ValueError("Invalid coffee details provided")

    # Reduce the quantity in the database
    execute_query("""
        UPDATE coffee_stock
        SET quantity = quantity - %s
        WHERE coffee_pack = %s AND sizes = %s AND type = %s
    """, (quantity_sold, coffee_name, size, coffee_type))

    # Check if the stock goes negative
    new_quantity = fetch_one("""
        SELECT quantity FROM coffee_stock
        WHERE coffee_pack = %s AND sizes = %s AND type = %s
    """, (coffee_name, size, coffee_type))['quantity']

    if new_quantity < 0:
        print(f"Error: Not enough stock for {coffee_name}, {size}, {coffee_type}. Transaction canceled.")
        execute_query("ROLLBACK")
    else:
        print(f"Sold {quantity_sold} of {coffee_name}, {size}, {coffee_type}.")

def refill_stock(coffee_name, size, coffee_type, quantity_refilled):
    """
    Refills coffee stock and updates the database.
    """
    if quantity_refilled < 0:
        raise ValueError("Quantity refilled can't be a negative value")
    if not validate_coffee_details(coffee_name, size, coffee_type):
        raise ValueError("Invalid coffee details provided")

    # Increase the quantity in the database
    execute_query("""
        UPDATE coffee_stock
        SET quantity = quantity + %s
        WHERE coffee_pack = %s AND sizes = %s AND type = %s
    """, (quantity_refilled, coffee_name, size, coffee_type))
    print(f"Refilled {quantity_refilled} of {coffee_name}, {size}, {coffee_type}.")

def validate_coffee_details(coffee_name, size, coffee_type):
    """
    Validates if the coffee details exist in the database.
    """
    count = fetch_one("""
        SELECT COUNT(*) as count FROM coffee_stock
        WHERE coffee_pack = %s AND sizes = %s AND type = %s
    """, (coffee_name, size, coffee_type))['count']
    return count > 0
