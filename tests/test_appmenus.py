from source.appmenus import get_option

# To run this unit test: HOLBMAC1004:miniproject juliet.hartwell$ python -m unittest tests.test_appmenus

### TEST CASES FOR get_option()

# Common case: user enters a number
def test_get_option_with_number_input():
    # Assemble
    def mock_input(msg):
        return '2'
    
    expected = '2'
    
    # Actual
    actual = get_option(mock_input)
    
    # Assert
    assert actual == expected
    print('Passed test_get_option_with_number_input')

test_get_option_with_number_input()

# Edge case: user enters a word
def test_get_option_with_word_input():
    # Assemble
    def mock_input(msg):
        return 'two'
    
    expected = 'two'
    
    # Actual
    actual = get_option(mock_input)
    
    # Assert
    assert actual == expected
    print('Passed test_get_option_with_word_input')

test_get_option_with_word_input()

# Edge case: user enters nothing
def test_get_option_with_no_input():
    # Assemble
    def mock_input(msg):
        return ''
    
    expected = ''
    
    # Actual
    actual = get_option(mock_input)
    
    # Assert
    assert actual == expected
    print('Passed test_get_option_with_no_input')

test_get_option_with_no_input()

# Corner case: user enters a Boolean
def test_get_option_with_bool_input():
    # Assemble
    def mock_input(msg):
        return 'True'
    
    expected = 'True'
    
    # Actual
    actual = get_option(mock_input)
    
    # Assert
    assert actual == expected
    print('Passed test_get_option_with_bool_input')

test_get_option_with_bool_input()

# Corner case: user enters a non-alpha-numeric character
def test_get_option_with_hyphen_input():
    # Assemble
    def mock_input(msg):
        return '-'
    
    expected = '-'
    
    # Actual
    actual = get_option(mock_input)
    
    # Assert
    assert actual == expected
    print('Passed test_get_option_with_hyphen_input')

test_get_option_with_hyphen_input()
