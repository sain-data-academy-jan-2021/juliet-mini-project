import unittest
from unittest.mock import patch
from source.database import get_highest_item_id_from_db_table
from source.order import validated_courier, get_single_column_from_db_table, validated_product

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
        
    @patch("source.order.get_single_column_from_db_table")
    @patch("builtins.input")
    def test_validated_courier_should_return_courier_id(self, mock_input, mock_get_single_column_from_db_table):
        #Assemble
        mock_get_single_column_from_db_table.return_value = [1, 2, 5, 10]
        mock_input.side_effect = ["2"]
        
        #Act
        return_value = validated_courier()
        
        #Assert
        self.assertEqual(return_value, 2)
        
    
    @patch("source.order.get_single_column_from_db_table")
    @patch("builtins.input")
    @patch("builtins.print")
    def test_validated_courier_should_return_courier_id_following_one_failed_attempt(self, mock_print, mock_input, mock_get_single_column_from_db_table):
        #Assemble
        mock_get_single_column_from_db_table.return_value = [1, 2, 5, 10]
        mock_input.side_effect = ["13", "2"]
        
        #Act
        return_value = validated_courier()
        
        #Assert
        mock_print.assert_called_with('Ooops! Please select a valid Courier ID or leave blank.\n')
        self.assertEqual(return_value, 2)
    
    
    @patch("source.order.get_single_column_from_db_table")
    @patch("builtins.input")
    @patch("builtins.print")
    def test_validated_courier_should_incur_value_error(self, mock_print, mock_input, mock_get_single_column_from_db_table):
        #Assemble
        mock_get_single_column_from_db_table.return_value = [1, 2, 5, 10]
        mock_input.side_effect = ['one', 'Nick', '1']
        
        #Act
        return_value = validated_courier()
        
        #Assert
        mock_print.assert_called_with('Ooops! Please select a valid Courier ID or leave blank.\n')
        self.assertEqual(return_value, 1)
    
    
    @patch("source.order.get_single_column_from_db_table")
    @patch("builtins.input")
    @patch("builtins.print")
    def test_validated_courier_should_return_null(self, mock_print, mock_input, mock_get_single_column_from_db_table):
        #Assemble
        mock_get_single_column_from_db_table.return_value = [1, 2, 5, 10]
        mock_input.side_effect = ['']
        
        #Act
        return_value = validated_courier()
        
        #Assert
        self.assertEqual(return_value, 'NULL')

    
    @patch('source.order.get_single_column_from_db_table')
    @patch('builtins.input')
    def test_validated_product_should_return_null(self, mock_input, mock_get_single_column_from_db_table):
        # Assemble
        mock_get_single_column_from_db_table.return_value = [12, 14, 15, 17, 18, 20]
        mock_input.side_effect = ['']
        expected = 'NULL'
        
        # Act
        result = validated_product('cake')
        
        # Assert
        self.assertEqual(result, expected)
    
    
    @patch('source.order.get_single_column_from_db_table')
    @patch('builtins.input')
    def test_validated_product_should_return_empty_string(self, mock_input, mock_get_single_column_from_db_table):
        # Assemble
        mock_get_single_column_from_db_table.return_value = [12, 14, 15, 17, 18, 20]
        mock_input.side_effect = ['', '', '']
        expected = ''
        
        result = validated_product('cake', 'update')
        self.assertEqual(result, expected)
        
        result = validated_product('sandwich', 'update')
        self.assertEqual(result, expected)
        
        result = validated_product('drink', 'update')
        self.assertEqual(result, expected)
    
    
    @patch('source.order.get_single_column_from_db_table')
    @patch('builtins.input')
    def test_validated_product_should_return_zero_string(self, mock_input, mock_get_single_column_from_db_table):
        # Assemble
        mock_get_single_column_from_db_table.return_value = [12, 14, 15, 17, 18, 20]
        mock_input.side_effect = ['0']
        expected = '0'
        
        # Act
        result = validated_product('cake', 'update')
        
        # Assert
        self.assertEqual(result, expected)
    
    
    @patch('source.order.print_table')
    @patch('source.order.get_single_column_from_db_table')
    @patch('builtins.input')
    def test_validated_product_should_ensure_user_enters_valid_product_id(self, mock_input, mock_get_single_column_from_db_table, mock_print_table):
        # Assemble
        mock_print_table.return_value = None
        mock_get_single_column_from_db_table.return_value = [12, 14, 15, 17, 18, 20]
        mock_input.side_effect = ['14', '12', '']
        expected = '12, 14'
        
        # Act
        result = validated_product('cake', 'create')
        
        # Assert
        self.assertEqual(result, expected)
    
    

if __name__ == '__main__':
    unittest.main()