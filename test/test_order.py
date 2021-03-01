import unittest
from unittest.mock import patch
from datetime import datetime

from source.order import validated_courier, get_single_column_from_db_table, validated_product, order_autocalc, order_confirmation


class TestOrder(unittest.TestCase):
        
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
    def test_validated_product_should_ensure_user_enters_valid_product_id_for_create(self, mock_input, mock_get_single_column_from_db_table, mock_print_table):
        # Assemble
        mock_print_table.return_value = None
        mock_get_single_column_from_db_table.return_value = [12, 14, 15, 17, 18, 20]
        mock_input.side_effect = ['14', '12', '']
        expected = '12, 14'
        
        # Act
        result = validated_product('cake', 'create')
        
        # Assert
        self.assertEqual(result, expected)
    
    
    @patch('source.order.print_table')
    @patch('source.order.get_single_column_from_db_table')
    @patch('builtins.input')
    def test_validated_product_should_ensure_user_enters_valid_product_id_for_update(self, mock_input, mock_get_single_column_from_db_table, mock_print_table):
        # Assemble
        mock_print_table.return_value = None
        mock_get_single_column_from_db_table.return_value = [12, 14, 15, 17, 18, 20]
        mock_input.side_effect = ['14', '12', '']
        expected = '12, 14'
        
        # Act
        result = validated_product('cake', 'update')
        
        # Assert
        self.assertEqual(result, expected)
    
    
    @patch('source.order.print_table')
    @patch('source.order.get_single_column_from_db_table')
    @patch('builtins.input')
    def test_validated_product_should_incur_value_error_for_create(self, mock_input, mock_get_single_column_from_db_table, mock_print_table):
        # Assemble
        mock_print_table.return_value = None
        mock_get_single_column_from_db_table.return_value = [12, 14, 15, 17, 18, 20]
        mock_input.side_effect = ['Lemon square', '12', '17', '']
        expected = '12, 17'
        
        # Act
        result = validated_product('cake')
        
        # Assert
        self.assertEqual(result, expected)
    
    
    @patch('source.order.print_table')
    @patch('source.order.get_single_column_from_db_table')
    @patch('builtins.input')
    def test_validated_product_should_incur_value_error_for_update(self, mock_input, mock_get_single_column_from_db_table, mock_print_table):
        # Assemble
        mock_print_table.return_value = None
        mock_get_single_column_from_db_table.return_value = [12, 14, 15, 17, 18, 20]
        mock_input.side_effect = ['Lemon square', '12', '17', '']
        expected = '12, 17'
        
        # Act
        result = validated_product('cake', 'update')
        
        # Assert
        self.assertEqual(result, expected)
    
    
    @patch("source.order.get_highest_item_id_from_db_table")
    def test_order_autocalc_should_generate_order_number_and_order_date(self, mock_get_highest_item_id_from_db_table):
        # Assemble
        mock_get_highest_item_id_from_db_table.return_value = 10
        expected = ('JAM-11', datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S'))
        
        # Act
        result = order_autocalc()
        
        # Assert
        self.assertEqual(result, expected)

    
    @patch("source.order.get_highest_item_id_from_db_table")
    def test_order_autocalc_should_generate_jam1_order_number_and_order_date_when_order_table_is_empty(self, mock_get_highest_item_id_from_db_table):
        # Assemble
        mock_get_highest_item_id_from_db_table.return_value = 0
        expected = ('JAM-1', datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S'))
        
        # Act
        result = order_autocalc()
        
        # Assert
        self.assertEqual(result, expected)
    
    
    @patch('source.order.clear_terminal')
    @patch('source.order.app_title')
    @patch('builtins.print')
    def test_order_confirmation_should_print_order_confirmation(self, mock_print, mock_app_title, mock_clear_terminal):
        # Assemble
        mock_clear_terminal.return_value = None
        mock_app_title.return_value = None
        test_order_details = f'''Thanks for your order, Samantha Stevens!\n
YOUR ORDER SUMMARY
Order Number: JAM-10
Order date: 2021-03-01 16:45:20
Courier: 1
Sandwiches: 3, 5
Cakes: NULL
Drinks: 20, 25
Order status: PREPARING'''
        
        # Act
        result = order_confirmation('Samantha Stevens', 'JAM-10', '2021-03-01 16:45:20', 1, '3, 5', 'NULL', '20, 25')
        
        # Assert
        mock_print.assert_called_with(test_order_details)




if __name__ == '__main__':
    unittest.main()