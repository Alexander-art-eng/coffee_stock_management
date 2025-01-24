# data_structure.py
"""
This module manages the inventory of the coffee stock, including initializing the stock.
"""

from coffee_management.database import execute_query, fetch_one

# Global variable to store the coffee stock
coffee_stock = {}

def initialize_stock():
    """
    Initializes the coffee stock with a nested dictionary structure.
    """
    global coffee_stock
    if coffee_stock:
        return coffee_stock  # Return the existing stock if already initialized
    coffee_stock = {
        "Buna Blend": {
            "100g": {
                "Ground": {"price": 7.0, "quantity": 0.0},
                "Beans": {"price": 7.0, "quantity": 0.0}
            },
            "250g": {
                "Ground": {"price": 13.0, "quantity": 0.0},
                "Beans": {"price": 13.0, "quantity": 0.0}
            },
            "500g": {
                "Ground": {"price": 19.50, "quantity": 0.0},
                "Beans": {"price": 19.50, "quantity": 2.0}
            },
            "1kg": {
                "Ground": {"price": 37.0, "quantity": 0.0},
                "Beans": {"price": 37.0, "quantity": 1.0}
            },
            "2.5kg": {
                "Ground": {"price": 85.0, "quantity": 0.0},
                "Beans": {"price": 37.0, "quantity": 6.0}
            },
        },
        "Koke": {
            "100g": {
                "Ground": {"price": 7.0, "quantity": 0.0},
                "Beans": {"price": 7.0, "quantity": 1.0}
            },
            "250g": {
                "Ground": {"price": 15.70, "quantity": 1.0},
                "Beans": {"price": 15.70, "quantity": 5.0}
            },
            "500g": {
                "Ground": {"price": 31.0, "quantity": 0.0},
                "Beans": {"price": 31.0, "quantity": 0.0}
            },
            "1kg": {
                "Ground": {"price": 57.0, "quantity": 0.0},
                "Beans": {"price": 57.0, "quantity": 0.0}
            },
        },
        "Sidamo": {
            "100g": {
                "Ground": {"price": 7.0, "quantity": 0.0},
                "Beans": {"price": 7.0, "quantity": 1.0}
            },
            "250g": {
                "Ground": {"price": 14.0, "quantity": 1.0},
                "Beans": {"price": 14.0, "quantity": 0.0}
            },
            "500g": {
                "Ground": {"price": 24.60, "quantity": 0.0},
                "Beans": {"price": 24.60, "quantity": 0.0}
            },
            "1kg": {
                "Ground": {"price": 45.0, "quantity": 0.0},
                "Beans": {"price": 45.0, "quantity": 0.0}
            },
        },
        "Yirgacheffe": {
            "100g": {
                "Ground": {"price": 7.0, "quantity": 0.0},
                "Beans": {"price": 7.0, "quantity": 1.0}
            },
            "250g": {
                "Ground": {"price": 15.70, "quantity": 1.0},
                "Beans": {"price": 15.70, "quantity": 3.0}
            },
            "500g": {
                "Ground": {"price": 31.0, "quantity": 0.0},
                "Beans": {"price": 31.0, "quantity": 0.0}
            },
            "1kg": {
                "Ground": {"price": 57.0, "quantity": 0.0},
                "Beans": {"price": 57.0, "quantity": 0.0}
            },
        },
        "Yetu Tamu": {
            "100g": {
                "Ground": {"price": 7.0, "quantity": 1.0},
                "Beans": {"price": 7.0, "quantity": 0.0}
            },
            "250g": {
                "Ground": {"price": 13.0, "quantity": 1.0},
                "Beans": {"price": 13.0, "quantity": 2.0}
            },
            "500g": {
                "Ground": {"price": 24.60, "quantity": 0.0},
                "Beans": {"price": 24.60, "quantity": 0.0}
            },
            "1kg": {
                "Ground": {"price": 45.0, "quantity": 0.0},
                "Beans": {"price": 45.0, "quantity": 0.0}
            },
        },
        "House of Signatures": {
            "250g": {
                "Ground": {"price": 16.0, "quantity": 0.0},
                "Beans": {"price": 16.0, "quantity": 0.0}
            },
            "500g": {
                "Ground": {"price": 31.0, "quantity": 0.0},
                "Beans": {"price": 31.0, "quantity": 0.0}
            },
            "1kg": {
                "Ground": {"price": 60.0, "quantity": 0.0},
                "Beans": {"price": 60.0, "quantity": 0.0}
            },
        },
        "Kivu D.R. Congo": {
            "100g": {
                "Ground": {"price": 7.0, "quantity": 1.0},
                "Beans": {"price": 7.0, "quantity": 3.0}
            },
            "250g": {
                "Ground": {"price": 15.70, "quantity": 4.0},
                "Beans": {"price": 15.70, "quantity": 1.0}
            },
            "500g": {
                "Ground": {"price": 31.0, "quantity": 0.0},
                "Beans": {"price": 31.0, "quantity": 0.0}
            },
            "1kg": {
                "Ground": {"price": 57.0, "quantity": 0.0},
                "Beans": {"price": 57.0, "quantity": 0.0}
            },
        },
        "Glory to Ukraine": {
            "250g": {
                "Ground": {"price": 15.0, "quantity": 2.0},
                "Beans": {"price": 15.0, "quantity": 2.0}
            }
        },
        "Rebuild Ukraine": {
            "250g": {
                "Ground": {"price": 15.0, "quantity": 0.0},
                "Beans": {"price": 15.0, "quantity": 0.0}
            }
        },
        "Coffee sets": {
            "400g": {
                "Ground": {"price": 30.0, "quantity": 2.0},
                "Beans": {"price": 30.0, "quantity": 4.0}
            }
        },
        "Aciu": {
            "250g": {
                "Ground": {"price": 15.50, "quantity": 0.0},
                "Beans": {"price": 15.50, "quantity": 0.0}
            }
        },
        "Love Birds": {
            "250g": {
                "Ground": {"price": 15.50, "quantity": 0.0},
                "Beans": {"price": 15.50, "quantity": 0.0}
            }
        },
        "As ir Tu": {
            "250g": {
                "Ground": {"price": 15.0, "quantity": 0.0},
                "Beans": {"price": 15.0, "quantity": 0.0}
            }
        },
        "Decafe Nyeri": {
            "250g": {
                "Ground": {"price": 15.0, "quantity": 0.0},
                "Beans": {"price": 15.0, "quantity": 0.0}
            }
        },
        "Upendo Africa": {
            "100g": {
                "Ground": {"price": 7.0, "quantity": 0.0},
                "Beans": {"price": 7.0, "quantity": 0.0}
            },
            "250g": {
                "Ground": {"price": 15.70, "quantity": 4.0},
                "Beans": {"price": 15.70, "quantity": 1.0}
            }
        },
        "Warmest Greetings": {
            "250g": {
                "Ground": {"price": 15.0, "quantity": 0.0},
                "Beans": {"price": 15.0, "quantity": 1.0},
            }
        },
        "Nyeri": {
            "100g": {
                "Ground": {"price": 7.0, "quantity": 0.0},
                "Beans": {"price": 7.0, "quantity": 0.0},
            },
            "250g": {
                "Ground": {"price": 16.30, "quantity": 1.0},
                "Beans": {"price": 16.30, "quantity": 2.0},
            }
        }
    }

    # Check if the database already has stock
    stock_count = fetch_one("SELECT COUNT(*) as count FROM coffee_stock")['count']

    if stock_count == 0:
        # Insert initial stock into the database
        for coffee, sizes in coffee_stock.items():
            for size, types in sizes.items():
                for coffee_type, details in types.items():
                    execute_query("""
                        INSERT INTO coffee_stock (coffee_pack, sizes, type, price, quantity)
                        VALUES (%s, %s, %s, %s, %s)
                    """, (coffee, size, coffee_type, details['price'], details['quantity']))
        print("Coffee stock initialized in the database.")
    else:
        print("Coffee stock is already initialized in the database.")

def fetch_stock():
    """
    Fetches the coffee stock from the database.
    Returns:
        dict: A nested dictionary structure of the coffee stock.
    """
    rows = execute_query("SELECT * FROM coffee_stock", fetch=True)

    coffee_stock = {}
    for row in rows:
        coffee_name = row['coffee_pack']
        size = row['sizes']
        coffee_type = row['type']
        price = row['price']
        quantity = row['quantity']

        if coffee_name not in coffee_stock:
            coffee_stock[coffee_name] = {}
        if size not in coffee_stock[coffee_name]:
            coffee_stock[coffee_name][size] = {}
        coffee_stock[coffee_name][size][coffee_type] = {"price": price, "quantity": quantity}

    return coffee_stock
