# Coffee Management System

## Overview

The Coffee Management System is a Python application designed to manage coffee inventory using a MySQL database. It allows users to view the current stock of coffee, sell coffee packs, and refill stock quantities. The application uses a structured data format to maintain coffee details, including types, sizes, prices, and quantities.

## Features

- **Display Coffee Stock**: View the current inventory of coffee packs in a tabular format.
- **Sell Coffee**: Reduce the quantity of coffee packs when sold, updating the database accordingly.
- **Refill Stock**: Increase the quantity of coffee packs in stock, with changes reflected in the database.
- **Data Structure**: Utilizes a nested dictionary to store coffee details, with persistent storage in a MySQL database.

## Database Setup

1. **Install MySQL**: Ensure you have MySQL installed on your machine. You can download it from [MySQL's official website](https://dev.mysql.com/downloads/mysql/).

2. **Create Database**: Create a database named `coffee_stock_db` in your MySQL server. You can do this using the MySQL command line or a GUI tool like MySQL Workbench.

3. **Create Table**: Run the following SQL command to create the necessary table for storing coffee stock:
   ```sql
   CREATE TABLE coffee_stock (
       id INT AUTO_INCREMENT PRIMARY KEY,
       coffee_pack VARCHAR(255) NOT NULL,
       sizes VARCHAR(50) NOT NULL,
       type VARCHAR(50) NOT NULL,
       price DECIMAL(10, 2) NOT NULL,
       quantity DECIMAL(10, 2) NOT NULL
   );
   ```

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd coffee_management
   ```

2. Install the required packages using `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To run the application and display the coffee stock, execute the following command:
```bash
python coffee_management/main.py
```

To display more information about the test, run:
```bash
pytest -v tests/test_inventory.py
```

## Code Structure

- `coffee_management/`
  - `data_structure.py`: Contains the data structure for managing coffee stock and the initialization function, including database connection logic.
  - `inventory.py`: Contains logic for managing coffee inventory, including selling and refilling stock, with database updates.
  - `display.py`: Contains logic to display the coffee stock in a tabular format.
- `tests/`
  - `test_inventory.py`: Contains unit tests for the inventory management functions.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.
