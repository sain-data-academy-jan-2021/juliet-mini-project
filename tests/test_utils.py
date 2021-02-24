# To run this unit test: python -m unittest tests.test_utils 

import unittest
from source.utils import *

class TestUtils(unittest.TestCase):
    
    # Tests for get_col_names_for_printing()
    def test_get_col_names_for_printing_with_product_types(self):
        # Assemble
        item_type1 = 'sandwich'
        item_type2 = 'cake'
        item_type3 = 'drink'
        expected = 'id, name, price'
        
        # Act
        result1 = get_col_names_for_printing(item_type1)
        result2 = get_col_names_for_printing(item_type2)
        result3 = get_col_names_for_printing(item_type3)
        
        # Assert
        self.assertEqual(result1, expected)
        self.assertEqual(result2, expected)
        self.assertEqual(result3, expected)
    
    
    def test_get_col_names_for_printing_with_courier(self):
        # Assemble
        item_type = 'courier'
        expected = 'id, name, phone'
        
        # Act
        result = get_col_names_for_printing(item_type)
        
        # Assert
        self.assertEqual(result, expected)
    
    
    def test_get_col_names_for_printing_with_order(self):
        # Assemble
        item_type = 'order'
        expected = 'id, order_number, order_date, order_status, courier, customer_name, customer_phone, customer_address, sandwiches, cakes, drinks'
        
        # Act
        result = get_col_names_for_printing(item_type)
        
        # Assert
        self.assertEqual(result, expected)
    
    
    def test_get_col_names_for_printing_with_incorrect_num_of_args(self):
        # Assemble
        item_type1 = 'sandwich'
        item_type2 = 'cake'
        expected = TypeError
        
        # Act & Assert
        with self.assertRaises(TypeError):
            get_col_names_for_printing()
        
        with self.assertRaises(TypeError):
            get_col_names_for_printing(item_type1, item_type2)
    
    
    def test_get_col_names_for_printing_with_other_data_types(self):
        # Assemble
        item_type1 = ''
        item_type2 = True
        item_type3 = 1
        item_type4 = ['cake']
        expected = 'id, order_number, order_date, order_status, courier, customer_name, customer_phone, customer_address, sandwiches, cakes, drinks'
        
        # Act
        result1 = get_col_names_for_printing(item_type1)
        result2 = get_col_names_for_printing(item_type2)
        result3 = get_col_names_for_printing(item_type3)
        result4 = get_col_names_for_printing(item_type4)
        
        # Assert
        self.assertEqual(result1, expected)
        self.assertEqual(result2, expected)
        self.assertEqual(result3, expected)
        self.assertEqual(result4, expected)
    
    
    # Tests for reformat_col_names()
    def test_reformat_col_names_with_list_of_strings(self):
        # Assemble
        col_names_lst = ['id', 'product_type', 'COURIER NAME']
        expected = ['Id', 'Product Type', 'Courier Name']
        
        # Act
        result = reformat_col_names(col_names_lst)
        
        # Assert
        self.assertEqual(result, expected)
    
    
    def test_reformat_col_names_with_empty_list(self):
        # Assemble
        col_names_lst = []
        expected = []
        
        # Act
        result = reformat_col_names(col_names_lst)
        
        # Assert
        self.assertEqual(result, expected)
    
    
    def test_reformat_col_names_with_list_of_other_data_types(self):
        # Assemble
        col_names_lst1 = [1, 2]
        col_names_lst2 = [True, False]
        col_names_lst3 = [{1: 'name'}]
        col_names_lst4 = [['product_name'], ['price']]
        expected = AttributeError
        
        # Act & Assert        
        with self.assertRaises(AttributeError):
            reformat_col_names(col_names_lst1)
        
        with self.assertRaises(AttributeError):
            reformat_col_names(col_names_lst2)
        
        with self.assertRaises(AttributeError):
            reformat_col_names(col_names_lst3)
        
        with self.assertRaises(AttributeError):
            reformat_col_names(col_names_lst4)
    
    
    def test_reformat_col_names_with_other_data_types(self):
        # Assemble
        col_names_lst1 = 'product_type'
        col_names_lst2 = 0
        col_names_lst3 = False
        expected = []
        
        # Act
        result1 = reformat_col_names(col_names_lst1)
        result2 = reformat_col_names(col_names_lst2)
        result3 = reformat_col_names(col_names_lst3)
        
        # Assert
        self.assertEqual(result1, expected)
        self.assertEqual(result2, expected)
        self.assertEqual(result3, expected)
    

    def test_reformat_col_names_with_incorrect_num_of_args(self):
        # Assemble
        col_names_lst1 = ['id', 'product_type']
        col_names_lst2 = ['product_type']
        expected = TypeError
        
        # Act & Assert
        with self.assertRaises(TypeError):
            reformat_col_names()
        
        with self.assertRaises(TypeError):
            reformat_col_names(col_names_lst1, col_names_lst2)


    # Tests for get_col_names_for_creating()
    def test_get_col_names_for_creating_with_product_types(self):
        # Assemble
        item_type1 = 'sandwich'
        item_type2 = 'cake'
        item_type3 = 'drink'
        expected = 'product_type, name, price'
        
        # Act
        result1 = get_col_names_for_creating(item_type1)
        result2 = get_col_names_for_creating(item_type2)
        result3 = get_col_names_for_creating(item_type3)
        
        # Assert
        self.assertEqual(result1, expected)
        self.assertEqual(result2, expected)
        self.assertEqual(result3, expected)
    
    
    def test_get_col_names_for_creating_with_courier(self):
        # Assemble
        item_type = 'courier'
        expected = 'name, phone'
        
        # Act
        result = get_col_names_for_creating(item_type)
        
        # Assert
        self.assertEqual(result, expected)
    
    
    def test_get_col_names_for_creating_with_order(self):
        # Assemble
        item_type = 'order'
        expected = 'order_number, order_date, order_status, customer_name, customer_address, customer_phone, courier, sandwiches, cakes, drinks'
        
        # Act
        result = get_col_names_for_creating(item_type)
        
        # Assert
        self.assertEqual(result, expected)
    
    
    def test_get_col_names_for_creating_with_incorrect_num_of_args(self):
        # Assemble
        item_type1 = 'sandwich'
        item_type2 = 'cake'
        expected = TypeError
        
        # Act & Assert
        with self.assertRaises(TypeError):
            get_col_names_for_creating()
        
        with self.assertRaises(TypeError):
            get_col_names_for_creating(item_type1, item_type2)
    
    
    def test_get_col_names_for_creating_with_other_data_types(self):
        # Assemble
        item_type1 = ''
        item_type2 = True
        item_type3 = 1
        item_type4 = ['cake']
        expected = 'order_number, order_date, order_status, customer_name, customer_address, customer_phone, courier, sandwiches, cakes, drinks'
        
        # Act
        result1 = get_col_names_for_creating(item_type1)
        result2 = get_col_names_for_creating(item_type2)
        result3 = get_col_names_for_creating(item_type3)
        result4 = get_col_names_for_creating(item_type4)
        
        # Assert
        self.assertEqual(result1, expected)
        self.assertEqual(result2, expected)
        self.assertEqual(result3, expected)
        self.assertEqual(result4, expected)

    
    # Tests for get_name_col_for_item(item_type)
    def test_get_name_col_for_item_with_order(self):
        # Assemble
        item_type = 'order'
        expected = 'order_number'
        
        # Act
        result = get_name_col_for_item(item_type)
        
        # Assert
        self.assertEqual(result, expected)
    
    
    def test_get_name_col_for_item_with_other_item_types(self):
        # Assemble
        item_type1 = 'sandwich'
        item_type2 = 'cake'
        item_type3 = 'drink'
        item_type4 = 'courier'
        expected = 'name'
        
        # Act
        result1 = get_name_col_for_item(item_type1)
        result2 = get_name_col_for_item(item_type2)
        result3 = get_name_col_for_item(item_type3)
        result4 = get_name_col_for_item(item_type4)
        
        # Assert
        self.assertEqual(result1, expected)
        self.assertEqual(result2, expected)
        self.assertEqual(result3, expected)
        self.assertEqual(result4, expected)
    
    
    def test_get_name_col_for_item_with_other_data_types(self):
        # Assemble
        item_type1 = {'name': 'lemon cake'}
        item_type2 = True
        item_type3 = 1
        item_type4 = ['lemon cake']
        item_type5 = ''
        expected = 'order_number'
        
        # Act
        result1 = get_name_col_for_item(item_type1)
        result2 = get_name_col_for_item(item_type2)
        result3 = get_name_col_for_item(item_type3)
        result4 = get_name_col_for_item(item_type4)
        result5 = get_name_col_for_item(item_type5)
        
        # Assert
        self.assertEqual(result1, expected)
        self.assertEqual(result2, expected)
        self.assertEqual(result3, expected)
        self.assertEqual(result4, expected)
        self.assertEqual(result5, expected)
    
    
    def test_get_name_col_for_item_with_incorrect_num_of_args(self):
        # Assemble
        item_type1 = 'sandwich'
        item_type2 = 'cake'
        expected = TypeError
        
        # Act & Assert
        with self.assertRaises(TypeError):
            get_name_col_for_item()
        
        with self.assertRaises(TypeError):
            get_name_col_for_item(item_type1, item_type2)
    
    
    # Tests for str_to_lst(string)
    def test_str_to_lst_with_string(self):
        # Assemble
        string1 = 'order number, order_date'
        string2 = 'price'
        expected1 = ['order number', 'order_date']
        expected2 = ['price']
        
        # Act
        result1 = str_to_lst(string1)
        result2 = str_to_lst(string2)
        
        # Assert
        self.assertEqual(result1, expected1)
        self.assertEqual(result2, expected2)
    
    
    def test_str_to_lst_with_empty_string(self):
        # Assemble
        string = ''
        expected = []
        
        # Act
        result = str_to_lst(string)
        
        # Assert
        self.assertEqual(result, expected)

    
    def test_str_to_lst_with_other_data_types(self):
        # Assemble
        string1 = ['cat', 'dog']
        string2 = False
        string3 = 100
        string4 = {'product': 'chocolate cake'}
        expected = []
        
        # Act
        result1 = str_to_lst(string1)
        result2 = str_to_lst(string2)
        result3 = str_to_lst(string3)
        result4 = str_to_lst(string4)
        
        # Assert
        self.assertEqual(result1, expected)
        self.assertEqual(result2, expected)
        self.assertEqual(result3, expected)
        self.assertEqual(result4, expected)
    
    
    def test_str_to_lst_with_incorrect_num_of_args(self):
        # Assemble
        string1 = 'name, price'
        string2 = 'name, phone'
        expected = TypeError
        
        # Act & Assert
        with self.assertRaises(TypeError):
            str_to_lst()
        
        with self.assertRaises(TypeError):
            str_to_lst(string1, string2)

    
    # Tests for num_lst_to_str(num_lst)
    def test_num_lst_to_str_with_list_of_nums(self):
        # Assemble
        num_lst1 = [1, 2, 3]
        num_lst2 = [1]
        expected1 = '1, 2, 3'
        expected2 = '1'
        
        # Act
        result1 = num_lst_to_str(num_lst1)
        result2 = num_lst_to_str(num_lst2)
        
        # Assert
        self.assertEqual(result1, expected1)
        self.assertEqual(result2, expected2)


    def test_num_lst_to_str_with_empty_list(self):
        # Assemble
        num_lst = []
        expected = ''
        
        # Act
        result = num_lst_to_str(num_lst)
        
        # Assert
        self.assertEqual(result, expected)
    
    
    def test_num_lst_to_str_with_list_of_other_data_types(self):
        # Assemble
        num_lst1 = ['1', '2', '3']
        num_lst2 = ['one', 'two', 'three']
        num_lst3 = [True, False]
        num_lst4 = [[1], [2]]
        num_lst5 = [1.5, 2.6]
        
        expected1 = '1, 2, 3'
        expected2 = 'one, two, three'
        expected3 = 'True, False'
        expected4 = '[1], [2]'
        expected5 = '1.5, 2.6'
        
        # Act
        result1 = num_lst_to_str(num_lst1)
        result2 = num_lst_to_str(num_lst2)
        result3 = num_lst_to_str(num_lst3)
        result4 = num_lst_to_str(num_lst4)
        result5 = num_lst_to_str(num_lst5)
        
        # Assert
        self.assertEqual(result1, expected1)
        self.assertEqual(result2, expected2)
        self.assertEqual(result3, expected3)
        self.assertEqual(result4, expected4)
        self.assertEqual(result5, expected5)
    
    
    def test_num_lst_to_str_with_other_data_types(self):
        # Assemble
        num_lst1 = '1, 2, 3'
        num_lst2 = False
        num_lst3 = {1: 'one'}
        num_lst4 = 1
        num_lst5 = 1.5
        expected = ''
        
        # Act
        result1 = num_lst_to_str(num_lst1)
        result2 = num_lst_to_str(num_lst2)
        result3 = num_lst_to_str(num_lst3)
        result4 = num_lst_to_str(num_lst4)
        result5 = num_lst_to_str(num_lst5)
        
        # Assert
        self.assertEqual(result1, expected)
        self.assertEqual(result2, expected)
        self.assertEqual(result3, expected)
        self.assertEqual(result4, expected)
        self.assertEqual(result5, expected)
    
    
    def test_num_lst_to_str_with_incorrect_num_of_args(self):
        # Assemble
        num_lst1 = [1, 2]
        num_lst2 = [2, 2]
        expected = TypeError
        
        # Act & Assert
        with self.assertRaises(TypeError):
            num_lst_to_str()
        
        with self.assertRaises(TypeError):
            num_lst_to_str(num_lst1, num_lst2)


if __name__ == '__main__':
    unittest.main()