# To run ALL unit tests: python -m unittest discover .
# To run this test suite: python -m unittest tests.test_appmenu

import unittest
from source.appmenu import get_option

class TestAppMenu(unittest.TestCase):

    # Tests for get_option()

    # Common case: user enters a number
    def test_get_option_with_number_input(self):
        # Assemble
        def mock_input(msg):
            return '2'
        
        expected = '2'
        
        # Act
        actual = get_option(mock_input)
        
        # Assert
        assert actual == expected


    # Edge case: user enters a word
    def test_get_option_with_word_input(self):
        # Assemble
        def mock_input(msg):
            return 'two'
        
        expected = 'two'
        
        # Act
        actual = get_option(mock_input)
        
        # Assert
        assert actual == expected


    # Edge case: user enters nothing
    def test_get_option_with_no_input(self):
        # Assemble
        def mock_input(msg):
            return ''
        
        expected = ''
        
        # Act
        actual = get_option(mock_input)
        
        # Assert
        assert actual == expected


    # Corner case: user enters a Boolean
    def test_get_option_with_bool_input(self):
        # Assemble
        def mock_input(msg):
            return 'True'
        
        expected = 'True'
        
        # Act
        actual = get_option(mock_input)
        
        # Assert
        assert actual == expected


    # Corner case: user enters a non-alpha-numeric character
    def test_get_option_with_hyphen_input(self):
        # Assemble
        def mock_input(msg):
            return '-'
        
        expected = '-'
        
        # Act
        actual = get_option(mock_input)
        
        # Assert
        assert actual == expected

if __name__ == '__main__':
    unittest.main()
