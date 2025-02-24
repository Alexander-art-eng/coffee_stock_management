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
    # sold_coffee("Yirgacheffe", "100g", "Beans", 1)
    # sold_coffee("Yirgacheffe", "250g", "Beans", 1)
    # sold_coffee("Buna blend", "1kg", "Beans", 2)
    # sold_coffee("Buna blend", "2.5kg", "Beans", 1)
    # sold_coffee("Koke", "100g", "Beans", 1)
    # sold_coffee("Koke", "250g", "Ground", 3)
    # sold_coffee("Koke", "250g", "Ground", 3)
    # sold_coffee("Koke", "250g", "Beans", 7)
    # sold_coffee("Sidamo", "100g", "Beans", 1)
    # sold_coffee("Sidamo", "250g", "Beans", 1)
    # sold_coffee("Sidamo", "250g", "Ground", 1)
    # sold_coffee("Yetu Tamu", "100g", "Ground", 1)
    # sold_coffee("Yetu Tamu", "250g", "Beans", 1)
    # sold_coffee("Kivu D.R. Congo", "100g", "Ground", 1)
    # sold_coffee("Kivu D.R. Congo", "250g", "Ground", 1)
    # sold_coffee("Glory to Ukraine", "250g", "Beans", 1)
    # sold_coffee("Coffee sets", "400g", "Beans", 2)
    # sold_coffee("Coffee sets", "400g", "Ground", 1)
    # sold_coffee("Warmest Greetings", "250g", "Beans", 1)
    # sold_coffee("Upendo Africa", "250g", "Ground", 1)
    # sold_coffee("Glory to Ukraine", "250g", "Ground", 1)


    # print("Refilling the coffee stock")
    # refill_stock("Love Birds", "250g", "Ground", 1)
    # refill_stock("Love Birds", "250g", "Beans", 1)
    # refill_stock("Upendo Africa", "250g", "Ground", 1)
    # refill_stock("Upendo Africa", "250g", "Beans", 2)
    # refill_stock("Nyeri", "250g", "Ground", 2)
    # refill_stock("Upendo Africa", "250g", "Ground", 1)


    # refill_stock("Koke", "250g", "Beans", 2)
    # refill_stock("Koke", "250g", "Ground", 2)
    # refill_stock("Buna blend", "1kg", "Beans", 1)
    # refill_stock("As ir tu", "250g", "Ground", 2)
    # refill_stock("As ir tu", "250g", "Beans", 1)
    # refill_stock("Sidamo", "250g", "Beans", 2)
    # refill_stock("Sidamo", "250g", "Ground", 1)
    q


    # print("Updated Coffee Stock after sell and refill: \n")
    # display_coffee_stock()

if __name__ == "__main__":
    main()
