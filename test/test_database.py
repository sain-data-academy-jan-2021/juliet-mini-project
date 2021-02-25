# To run ALL unit tests: python -m unittest discover .
# To run this test suite: python -m unittest test.test_database

import unittest
from unittest.mock import patch
from source.database import *

class TestDatabase(unittest.TestCase):
    
    # Tests for get_db_table_name(item_type)
    def test_get_db_table_name_with_product_types(self):
        # Assemble
        item_type1 = 'sandwich'
        item_type2 = 'cake'
        item_type3 = 'drink'
        expected = 'products'
        
        # Act
        result1 = get_db_table_name(item_type1)
        result2 = get_db_table_name(item_type2)
        result3 = get_db_table_name(item_type3)
        
        # Assert
        self.assertEqual(result1, expected)
        self.assertEqual(result2, expected)
        self.assertEqual(result3, expected)
    
    
    def test_get_db_table_name_with_courier(self):
        # Assemble
        item_type = 'courier'
        expected = 'couriers'
        
        # Act
        result = get_db_table_name(item_type)
        
        # Assert
        self.assertEqual(result, expected)
    
    
    def test_get_db_table_name_with_order(self):
        # Assemble
        item_type = 'order'
        expected = 'orders'
        
        # Act
        result = get_db_table_name(item_type)
        
        # Assert
        self.assertEqual(result, expected)
    
    
    def test_get_db_table_name_with_incorrect_num_of_args(self):
        # Assemble
        item_type1 = 'sandwich'
        item_type2 = 'cake'
        expected = TypeError
        
        # Act & Assert
        with self.assertRaises(TypeError):
            get_db_table_name()
        
        with self.assertRaises(TypeError):
            get_db_table_name(item_type1, item_type2)
    
    
    def test_get_db_table_name_with_other_data_types(self):
        # Assemble
        item_type1 = ''
        item_type2 = True
        item_type3 = 1
        item_type4 = ['cake']
        expected = 'orders'
        
        # Act
        result1 = get_db_table_name(item_type1)
        result2 = get_db_table_name(item_type2)
        result3 = get_db_table_name(item_type3)
        result4 = get_db_table_name(item_type4)
        
        # Assert
        self.assertEqual(result1, expected)
        self.assertEqual(result2, expected)
        self.assertEqual(result3, expected)
        self.assertEqual(result4, expected)
    
    

if __name__ == '__main__':
    unittest.main()