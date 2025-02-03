# inventory.py
"""
Inventory module: Handles selling and refilling coffee stock.
"""
from coffee_management.database import execute_query, fetch_one

# custom exception classes
class NegativeQuantityError(ValueError):
    pass
class InvalidCoffeeDetailsError(ValueError):
    pass
class InsufficientStockError(ValueError):
    pass


def sold_coffee(coffee_name, size, coffee_type, quantity_sold):
    """
    Sells coffee stock and updates the database.
    """
    try:
        if quantity_sold < 0:
            raise NegativeQuantityError("Quantity sold can't be a negative value")
        if not validate_coffee_details(coffee_name, size, coffee_type):
            raise InvalidCoffeeDetailsError("Invalid coffee details provided")

        # Check current stock
        current_stock = fetch_one("""
            SELECT quantity FROM coffee_stock
            WHERE coffee_pack = %s AND sizes = %s AND type = %s
        """, (coffee_name, size, coffee_type))
        current_quantity = current_stock['quantity']

        if current_quantity < quantity_sold:
            raise InsufficientStockError(f"Not enough stock for {coffee_name}, {size}, {coffee_type}. Transaction Cancelled.")

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
    except NegativeQuantityError as e:
        print(f"Error: {e}")
    except InvalidCoffeeDetailsError as e:
        print(f"Error: {e}")
    except InsufficientStockError as e:
        print(f"Error: {e}")

def refill_stock(coffee_name, size, coffee_type, quantity_refilled):
    """
    Refills coffee stock and updates the database.
    """
    try:
        if quantity_refilled < 0:
            raise NegativeQuantityError("Quantity refilled can't be a negative value")
        if not validate_coffee_details(coffee_name, size, coffee_type):
            raise InvalidCoffeeDetailsError("Invalid coffee details provided")

        # Increase the quantity in the database
        execute_query("""
            UPDATE coffee_stock
            SET quantity = quantity + %s
            WHERE coffee_pack = %s AND sizes = %s AND type = %s
        """, (quantity_refilled, coffee_name, size, coffee_type))
        print(f"Refilled {quantity_refilled} of {coffee_name}, {size}, {coffee_type}.")
    except (NegativeQuantityError, InvalidCoffeeDetailsError) as e:
        print(f"Error: {e}")

def validate_coffee_details(coffee_name, size, coffee_type):
    """
    Validates if the coffee details exist in the database.
    """
    count = fetch_one("""
        SELECT COUNT(*) as count FROM coffee_stock
        WHERE coffee_pack = %s AND sizes = %s AND type = %s
    """, (coffee_name, size, coffee_type))['count']
    return count > 0
