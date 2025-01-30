from tkinter.font import names

from coffee_management.database import execute_query

def add_new_stock(coffee_pack, size, coffee_type, price, quantity):
    """
    Adds new stock to the coffee inventory in the database
    :param coffee_pack: the coffee pack name to add to the inventory
    :param size: the size of the coffee_pack
    :param coffee_type: Whether Beans or Ground
    :param price: the price of the coffee pack
    :param quantity: the number of the coffee stock to add
    :return:
    """
    execute_query("""
        INSERT INTO coffee_stock (coffee_pack, sizes, type, price, quantity)
        VALUES (%s, %s, %s, %s, %s)
    """, (coffee_pack, size, coffee_type, price, quantity))
    print(f"New Coffee added to the stock: {coffee_pack} - {size} - {coffee_type} - {price} - {quantity}")

# if __name__ == "__main__":
#     add_new_stock("Gyvenimo kava", "250g", "Ground", 15.00, 2)
#     add_new_stock("Gyvenimo kava", "250g", "Beans", 15.00, 1)