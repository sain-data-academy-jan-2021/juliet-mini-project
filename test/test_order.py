import unittest
from unittest.mock import patch
from datetime import datetime

from source.order import *

class TestOrder(unittest.TestCase):
        
    @patch("source.order.print_table")
    @patch("source.order.get_single_column_from_db_table")
    @patch("builtins.input")
    def test_validated_courier_should_return_courier_id(self, mock_input, mock_get_single_column_from_db_table, mock_print_table):
        #Assemble
        mock_print_table.return_value = None
        mock_get_single_column_from_db_table.return_value = [1, 2, 5, 10]
        mock_input.side_effect = ["2"]
        
        #Act
        return_value = validated_courier()
        
        #Assert
        self.assertEqual(return_value, 2)
        
    
    @patch("source.order.print_table")
    @patch("source.order.get_single_column_from_db_table")
    @patch("builtins.input")
    @patch("builtins.print")
    def test_validated_courier_should_return_courier_id_following_one_failed_attempt(self, mock_print, mock_input, mock_get_single_column_from_db_table, mock_print_table):
        #Assemble
        mock_print_table.return_value = None
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
    
    
    @patch('source.order.clear_terminal')
    @patch('source.order.app_title')
    @patch('source.order.return_to_menu')
    @patch('builtins.print')
    def test_empty_order_msg(self, mock_print, mock_return_to_menu, mock_app_title, mock_clear_terminal):
        # Assemble
        mock_clear_terminal.return_value = None
        mock_app_title.return_value = None
        mock_return_to_menu.return_value = None
        
        # Act
        result = empty_order_msg()
        
        # Assert
        mock_print.assert_called_with('We\'re sorry. Your order could not be placed as you didn\'t select any products.')
    
    
    @patch("source.order.get_highest_item_id_from_db_table")
    @patch('source.order.datetime')
    def test_order_autocalc_should_generate_order_number_and_order_date(self, mock_datetime, mock_get_highest_item_id_from_db_table):
        # Assemble
        mock_get_highest_item_id_from_db_table.return_value = 10
        mock_datetime.strftime.return_value = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
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
        self.assertEqual(mock_print.call_count, 2)
        mock_print.assert_any_call('-------- JAM\'S ORDER CONFIRMATION --------\n')
        mock_print.assert_any_call(test_order_details)
    
    
    @patch('source.order.clear_terminal')
    @patch('source.order.app_title')
    @patch('builtins.print')
    def test_load_order_screen_where_state_is_create(self, mock_print, mock_app_title, mock_clear_terminal):
        # Assemble
        mock_clear_terminal.return_value = None
        mock_app_title.return_value = None
        test_section_heading = 'Placeholder Heading'
        
        # Act
        result = load_order_screen(test_section_heading)
        
        # Assert
        self.assertEqual(mock_print.call_count, 3)
        mock_print.assert_any_call('-------- PLACE A NEW ORDER --------\n')
        mock_print.assert_any_call(test_section_heading)
        mock_print.assert_any_call('(* indicates a required field)\n')
    
    
    @patch('source.order.clear_terminal')
    @patch('source.order.app_title')
    @patch('builtins.print')
    def test_load_order_screen_where_state_is_update(self, mock_print, mock_app_title, mock_clear_terminal):
        # Assemble
        mock_clear_terminal.return_value = None
        mock_app_title.return_value = None
        test_section_heading = 'Placeholder Heading'
        
        # Act
        result = load_order_screen(test_section_heading, 'update')
        
        # Assert
        self.assertEqual(mock_print.call_count, 4)
        mock_print.assert_any_call('-------- UPDATE ORDER DETAILS --------\n')
        mock_print.assert_any_call('Complete the fields below to update your order details. Leave fields blank if no changes are required.\n')
        mock_print.assert_any_call(test_section_heading)
        mock_print.assert_any_call('(* indicates a required field)\n')
    
    
    @patch('source.order.clear_terminal')
    @patch('source.order.app_title')
    @patch('builtins.print')
    def test_load_order_screen_where_section_heading_is_not_a_string(self, mock_print, mock_app_title, mock_clear_terminal):
        # Assemble
        mock_clear_terminal.return_value = None
        mock_app_title.return_value = None
        test_section_heading1 = False
        test_section_heading2 = 2.4
        test_section_heading3 = ['Placeholder Heading']
        
        # Act & Assert
        result1 = load_order_screen(test_section_heading1)
        self.assertEqual(mock_print.call_count, 3)
        mock_print.assert_any_call('-------- PLACE A NEW ORDER --------\n')
        mock_print.assert_any_call(f'{test_section_heading1}')
        mock_print.assert_any_call('(* indicates a required field)\n')
        mock_print.reset_mock()

        result2 = load_order_screen(test_section_heading2)
        self.assertEqual(mock_print.call_count, 3)
        mock_print.assert_any_call('-------- PLACE A NEW ORDER --------\n')
        mock_print.assert_any_call(f'{test_section_heading2}')
        mock_print.assert_any_call('(* indicates a required field)\n')
        mock_print.reset_mock()
        
        result3 = load_order_screen(test_section_heading3)
        self.assertEqual(mock_print.call_count, 3)
        mock_print.assert_any_call('-------- PLACE A NEW ORDER --------\n')
        mock_print.assert_any_call(f'{test_section_heading3}')
        mock_print.assert_any_call('(* indicates a required field)\n')




if __name__ == '__main__':
    unittest.main()