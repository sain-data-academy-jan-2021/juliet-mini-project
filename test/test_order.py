import unittest
from unittest.mock import patch
from source.database import get_highest_item_id_from_db_table

# Function to test
# Generates order id and sets order date & time
def order_autocalc():
    try:
        order_number = get_highest_item_id_from_db_table('order') + 1
        order_number = 'JAM-' + str(order_number)
        
    except TypeError:
        order_number = 'JAM-1'
        
    return order_number



class TestOrder(unittest.TestCase):
    
    @patch("test.test_order.get_highest_item_id_from_db_table")
    def test_order_autocalc(self, mock_get_highest_item_id_from_db_table):
        # Assemble
        mock_get_highest_item_id_from_db_table.return_value = 10
        expected = 'JAM-11'
        
        # Act
        result = order_autocalc()
        
        # Assert
        self.assertEqual(result, expected)
    


if __name__ == '__main__':
    unittest.main()