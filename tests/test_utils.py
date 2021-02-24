# To run this unit test: python -m unittest tests.test_utils 

import unittest
from source.utils import *
# from unittest.mock import patch

class TestUtils(unittest.TestCase):
    
    # def test_my_function(self):
    #     # expected = ...
    #     # result = ... 
    #     self.assertEqual(result, expected)
    
    # def test_another_function(self):
    #     expected = 1
    #     result = another_function()
        
    #     with self.assertRaises(TypeError):
    #         another_function()

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



# Using this means you can run the tests just by running the file in the normal way from the terminal
if __name__ == '__main__':
    unittest.main()