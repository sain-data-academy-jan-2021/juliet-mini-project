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
    
    
    @patch("source.order.print_table")
    @patch("source.order.get_single_column_from_db_table")
    @patch("builtins.input")
    @patch("builtins.print")
    def test_validated_courier_should_incur_value_error(self, mock_print, mock_input, mock_get_single_column_from_db_table, mock_print_table):
        #Assemble
        mock_print_table.return_value = None
        mock_get_single_column_from_db_table.return_value = [1, 2, 5, 10]
        mock_input.side_effect = ['one', 'Nick', '1']
        
        #Act
        return_value = validated_courier()
        
        #Assert
        mock_print.assert_called_with('Ooops! Please select a valid Courier ID or leave blank.\n')
        self.assertEqual(return_value, 1)
    
    
    @patch("source.order.print_table")
    @patch("source.order.get_single_column_from_db_table")
    @patch("builtins.input")
    @patch("builtins.print")
    def test_validated_courier_should_return_null(self, mock_print, mock_input, mock_get_single_column_from_db_table, mock_print_table):
        #Assemble
        mock_print_table.return_value = None
        mock_get_single_column_from_db_table.return_value = [1, 2, 5, 10]
        mock_input.side_effect = ['']
        
        #Act
        return_value = validated_courier()
        
        #Assert
        self.assertEqual(return_value, 'NULL')

    
    @patch("source.order.print_table")
    @patch('source.order.get_single_column_from_db_table')
    @patch('builtins.input')
    def test_validated_product_should_return_null(self, mock_input, mock_get_single_column_from_db_table, mock_print_table):
        # Assemble
        mock_print_table.return_value = None
        mock_get_single_column_from_db_table.return_value = [12, 14, 15, 17, 18, 20]
        mock_input.side_effect = ['']
        expected = 'NULL'
        
        # Act
        result = validated_product('cake')
        
        # Assert
        self.assertEqual(result, expected)
    
    
    @patch("source.order.print_table")
    @patch('source.order.get_single_column_from_db_table')
    @patch('builtins.input')
    def test_validated_product_should_return_empty_string(self, mock_input, mock_get_single_column_from_db_table, mock_print_table):
        # Assemble
        mock_print_table.return_value = None
        mock_get_single_column_from_db_table.return_value = [12, 14, 15, 17, 18, 20]
        mock_input.side_effect = ['', '', '']
        expected = ''
        
        result = validated_product('cake', 'update')
        self.assertEqual(result, expected)
        
        result = validated_product('sandwich', 'update')
        self.assertEqual(result, expected)
        
        result = validated_product('drink', 'update')
        self.assertEqual(result, expected)
    
    
    @patch("source.order.print_table")
    @patch('source.order.get_single_column_from_db_table')
    @patch('builtins.input')
    def test_validated_product_should_return_zero_string(self, mock_input, mock_get_single_column_from_db_table, mock_print_table):
        # Assemble
        mock_print_table.return_value = None
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

    
    @patch('source.order.load_order_screen')
    @patch('source.order.validated_courier')
    @patch('source.order.validated_product')
    def test_get_courier_and_product_selection_should_return_courier_and_product_selection(self, mock_validated_product, mock_validated_courier, mock_load_order_screen):
        # Assemble
        mock_load_order_screen.return_value = None
        mock_validated_courier.return_value = 3
        mock_validated_product.side_effect = ['5, 9', '32, 49', 'NULL']
        expected = (3, '5, 9', '32, 49', 'NULL')
        
        # Act
        result = get_courier_and_product_selection()
        
        # Assert
        self.assertEqual(mock_load_order_screen.call_count, 4)
        self.assertEqual(mock_validated_product.call_count, 3)
        self.assertEqual(result, expected)
    
    
    @patch('source.order.load_order_screen')
    @patch('source.order.validated_courier')
    @patch('source.order.validated_product')
    def test_get_courier_and_product_selection_should_return_null_courier_and_zero_product_selection(self, mock_validated_product, mock_validated_courier, mock_load_order_screen):
        # Assemble
        mock_load_order_screen.return_value = None
        mock_validated_courier.return_value = 'NULL'
        mock_validated_product.side_effect = ['0', '', '3']
        expected = ('NULL', '0', '', '3')
        
        # Act
        result = get_courier_and_product_selection()
        
        # Assert
        self.assertEqual(mock_load_order_screen.call_count, 4)
        self.assertEqual(mock_validated_product.call_count, 3)
        self.assertEqual(result, expected)
    
    
    @patch('source.order.load_order_screen')
    @patch('source.order.required_field')
    @patch('source.order.clear_terminal')
    @patch('source.order.app_title')
    def test_create_new_order_should_cancel_and_return_user_to_menu(self, mock_app_title, mock_clear_terminal, mock_required_field, mock_load_order_screen):
        # Assemble
        mock_load_order_screen.return_value = None
        mock_required_field.return_value = '0'
        mock_clear_terminal.return_value = None
        mock_app_title.return_value = None
        
        # Act
        result = create_new_order()
        
        # Assert
        self.assertTrue(mock_load_order_screen.called)
        self.assertTrue(mock_required_field.called)
        self.assertTrue(mock_clear_terminal.called)
        self.assertTrue(mock_app_title.called)
    
    
    @patch('source.order.load_order_screen')
    @patch('source.order.required_field')
    @patch('source.order.get_courier_and_product_selection')
    @patch('source.order.empty_order_msg')
    def test_create_new_order_should_call_empty_order_msg_when_zero_products_selected(self, mock_empty_order_msg, mock_get_courier_and_product_selection, mock_required_field, mock_load_order_screen):
        # Assemble
        mock_load_order_screen.return_value = None
        mock_required_field.side_effect = ['Snow White', '07987 654321', '123 Main Street, Storybrooke']
        mock_get_courier_and_product_selection.return_value = (3, 'NULL', 'NULL', 'NULL')
        mock_empty_order_msg.return_value = None
        
        # Act
        result = create_new_order()
        
        # Assert
        self.assertTrue(mock_load_order_screen.called)
        self.assertEqual(mock_required_field.call_count, 3)
        self.assertTrue(mock_get_courier_and_product_selection.called)
        self.assertTrue(mock_empty_order_msg.called)
        

    @patch('source.order.load_order_screen')
    @patch('source.order.required_field')
    @patch('source.order.get_courier_and_product_selection')
    @patch('builtins.print')
    @patch('source.order.return_to_menu')
    @patch('source.order.create_new_record')
    def test_create_new_order_should_throw_connection_error_and_not_create_order(self, mock_create_new_record, mock_return_to_menu, mock_print, mock_get_courier_and_product_selection, mock_required_field, mock_load_order_screen):
        # Assemble
        mock_load_order_screen.return_value = None
        mock_required_field.side_effect = ['Snow White', '07987 654321', '123 Main Street, Storybrooke']
        mock_get_courier_and_product_selection.side_effect = ConnectionError
        mock_return_to_menu.return_value = None
        mock_create_new_record.return_value = None
        
        # Act
        result = create_new_order()
        
        # Assert
        self.assertTrue(mock_load_order_screen.called)
        self.assertEqual(mock_required_field.call_count, 3)
        mock_print.called_with('Unfortunately your order cannot be placed at this time. Please call us to place an order.')
        self.assertTrue(mock_return_to_menu.called)
        self.assertFalse(mock_create_new_record.called)
    
    
    @patch('source.order.load_order_screen')
    @patch('source.order.required_field')
    @patch('source.order.get_courier_and_product_selection')
    @patch('source.order.order_autocalc')
    @patch('source.order.create_new_record')
    @patch('source.order.order_confirmation')
    @patch('source.order.return_to_menu')
    def test_create_new_order_should_throw_connection_error_and_not_create_order(self, mock_return_to_menu, mock_order_confirmation, mock_create_new_record, mock_order_autocalc, mock_get_courier_and_product_selection, mock_required_field, mock_load_order_screen):
        # Assemble
        mock_load_order_screen.return_value = None
        mock_required_field.side_effect = ['Snow White', '07987 654321', '123 Main Street, Storybrooke']
        mock_get_courier_and_product_selection.return_value = (5, 'NULL', '25, 38', '47, 49, 49')
        mock_order_autocalc.return_value = ('JAM-30', '2021-03-02 17:05:54')
        mock_create_new_record.return_value = None
        mock_return_to_menu.return_value = None
        
        # Act
        result = create_new_order()
        
        # Assert
        self.assertTrue(mock_load_order_screen.called)
        self.assertEqual(mock_required_field.call_count, 3)
        self.assertTrue(mock_create_new_record.called)
        mock_order_confirmation.assert_called_with('Snow White', 'JAM-30', '2021-03-02 17:05:54', 5, 'NULL', '25, 38', '47, 49, 49')
        self.assertTrue(mock_return_to_menu.called)
    
    
    @patch('builtins.print')
    @patch('source.order.print_table')
    @patch('source.order.get_single_column_from_db_table')
    @patch('source.order.return_to_menu')
    def test_update_order_status_should_return_to_menu_if_error_thrown_in_print_table(self, mock_return_to_menu, mock_get_single_column_from_db_table, mock_print_table, mock_print):
        # Assemble
        mock_print_table.side_effect = ConnectionError
        mock_get_single_column_from_db_table.return_value = [1, 3, 4, 6]
        mock_return_to_menu.return_value = None
        
        # Act
        result = update_order_status()
        
        # Assert
        mock_print.assert_called_with('-------- UPDATE ORDER STATUS --------\n')
        self.assertTrue(mock_print_table.called)
        self.assertFalse(mock_get_single_column_from_db_table.called)
        self.assertTrue(mock_return_to_menu.called)
    
    
    @patch('builtins.print')
    @patch('source.order.print_table')
    @patch('source.order.get_single_column_from_db_table')
    @patch('source.order.return_to_menu')
    def test_update_order_status_should_return_to_menu_if_error_thrown_in_get_single_column_from_db_table(self, mock_return_to_menu, mock_get_single_column_from_db_table, mock_print_table, mock_print):
        # Assemble
        mock_print_table.return_value = None
        mock_get_single_column_from_db_table.side_effect = ConnectionError
        mock_return_to_menu.return_value = None
        
        # Act
        result = update_order_status()
        
        # Assert
        mock_print.assert_called_with('-------- UPDATE ORDER STATUS --------\n')
        self.assertTrue(mock_print_table.called)
        self.assertTrue(mock_get_single_column_from_db_table.called)
        self.assertTrue(mock_return_to_menu.called)
    

    # value error is thrown if order_id can't be converted to an integer
    # if order_id is 0 then return user to menu
    # if order_id is invalid then print 'order id could not be found...' msg and return to menu
    # if order_id is valid then:
        # user should be looped round until they enter a valid new status
        # if no error during db call, order record should be updated in db and conf msg printed
        # if there is an error during db call, then user is returned to menu



if __name__ == '__main__':
    unittest.main()