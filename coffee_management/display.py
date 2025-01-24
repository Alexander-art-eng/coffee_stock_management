"""
Module: display
This module contains logic to display the coffee stock in a tabular format.
"""

from prettytable import PrettyTable
from coffee_management.data_structure import fetch_stock

def display_coffee_stock():
    """
    Displays the coffee inventory in a table format using PrettyTable.
    """
    coffee_stock = fetch_stock()
    if not coffee_stock:
        print("from display_coffee_stock: Coffee stock is empty. Please initialize the stock.")
        return

    print(f"{'-' * 6} Below is the Inventory for the Coffee packs in Inventory {'-' * 6}")

    table = PrettyTable()
    table.field_names = ["Coffee Pack", "Size", "Type", "Price (€)", "Quantity"]

    for name, sizes in coffee_stock.items():
        for size, types in sizes.items():
            for coffee_type, details in types.items():
                table.add_row([
                    name,
                    size,
                    coffee_type,
                    f"{details['price']:.2f}",
                    details["quantity"]
                ])
    print(table)
