import pytest
from unittest.mock import patch, MagicMock
from coffee_management.inventory import (
    sold_coffee, refill_stock,
)

# Mock data
mock_coffee_details = {
    'coffee_pack': 'Test Coffee',
    'sizes': '500g',
    'type': 'Ground',
    'quantity': 10
}

# Mock functions
def mock_fetch_one(query, params):
    if "COUNT" in query:
        return {'count': 1}  # Simulating that the coffee exists
    return {'quantity': mock_coffee_details['quantity']}  # Returning stock quantity

def mock_execute_query(query, params):
    pass  # Mock database execution

@patch('coffee_management.inventory.fetch_one', side_effect=mock_fetch_one)
@patch('coffee_management.inventory.execute_query', side_effect=mock_execute_query)
def test_sold_coffee(mock_fetch_one, mock_execute_query, capfd):
    """
    Test the sold_coffee function by checking printed messages instead of raised exceptions.
    """
    # Test selling coffee with valid details
    sold_coffee('Test Coffee', '500g', 'Ground', 5)
    out, _ = capfd.readouterr()  # Capture printed output
    assert "Sold 5 of Test Coffee, 500g, Ground." in out

    # Test selling coffee with negative quantity
    sold_coffee('Test Coffee', '500g', 'Ground', -5)
    out, _ = capfd.readouterr()
    assert "Error: Quantity sold can't be a negative value" in out

    # Test selling coffee with invalid details
    with patch('coffee_management.inventory.validate_coffee_details', return_value=False):
        sold_coffee('Invalid Coffee', '500g', 'Ground', 5)
        out, _ = capfd.readouterr()
        assert "Error: Invalid coffee details provided" in out

    # Test selling coffee with insufficient stock
    with patch('coffee_management.inventory.fetch_one') as mock_fetch:
        mock_fetch.side_effect = [
            {'count': 1},  # First call for validation
            {'quantity': 2}  # Second call for stock check
        ]
        sold_coffee('Test Coffee', '500g', 'Ground', 5)
        out, _ = capfd.readouterr()
        assert "Error: Not enough stock for Test Coffee, 500g, Ground. Transaction Cancelled." in out


# Test refill_stock function
@patch('coffee_management.inventory.fetch_one', side_effect=mock_fetch_one)
@patch('coffee_management.inventory.execute_query', side_effect=mock_execute_query)
def test_refill_stock(mock_fetch_one, mock_execute_query, capfd):
    # Test refilling coffee with valid details
    refill_stock('Test Coffee', '500g', 'Ground', 5)
    mock_execute_query.assert_called()

    # Test refilling coffee with negative quantity
    refill_stock('Test coffee', '500g', 'Ground', -5)
    out, _ = capfd.readouterr()
    assert "Error: Quantity refilled can't be a negative value" in out

    # Test refilling coffee with invalid details
    with patch('coffee_management.inventory.validate_coffee_details', return_value=False):
        refill_stock('Invalid coffee', '500g', 'Ground', 5)
        out, _ = capfd.readouterr()
        assert "Error: Invalid coffee details provided" in out