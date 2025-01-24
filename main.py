"""
Main entry point for the coffee stock management program.
"""

from coffee_management.display import display_coffee_stock
from coffee_management.inventory import sold_coffee, refill_stock
from coffee_management.data_structure import initialize_stock

def main():
    """
    Main program logic.
    """
    print(f"\n{'-' * 12} Welcome to the Coffee Stock Management {'-' * 12} \n")

    # Initialize stock in the database
    # initialize_stock()

    # Display stock
    print("The initial coffee pack inventory")
    display_coffee_stock()

    # Example operations
    print("Selling Coffee Pack")
    sold_coffee("Buna Blend", "100g", "Ground", 3)
    # print("Refilling the coffee stock")
    # refill_stock("Buna Blend", "100g", "Ground", 3)

    print("Updated Coffee Stock after sell and refill: \n")
    display_coffee_stock()

if __name__ == "__main__":
    main()
