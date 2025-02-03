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
    display_coffee_stock()

    # Example operations
    # # print("Selling Coffee Pack")
    # sold_coffee("Yirgacheffe", "250g", "Ground", 1)
    # sold_coffee("Buna blend", "500g", "Beans", 1)
    # sold_coffee("Upendo Africa", "250g", "Ground", 1)
    # sold_coffee("Glory to Ukraine", "250g", "Ground", 1)


    print("Refilling the coffee stock")
    # refill_stock("Yirgacheffe", "250g", "Ground", 2)
    # refill_stock("Nyeri", "250g", "Ground", 2)
    # refill_stock("Upendo Africa", "250g", "Ground", 1)
    refill_stock("Koke", "250g", "Beans", 2)
    refill_stock("Koke", "250g", "Ground", 2)
    refill_stock("Buna blend", "1kg", "Beans", 1)
    refill_stock("As ir tu", "250g", "Ground", 2)
    refill_stock("As ir tu", "250g", "Beans", 1)
    refill_stock("Sidamo", "250g", "Beans", 2)
    refill_stock("Sidamo", "250g", "Ground", 1)


    print("Updated Coffee Stock after sell and refill: \n")
    display_coffee_stock()

if __name__ == "__main__":
    main()
