### UTILITIES ###

from os import system

# Prints app title
def app_title():
    print('''
______________________________________________________________________________________

    888                         d88b               e88~-_              88~\           
    888   /~~~8e  888-~88e-~88e Y88P  d88~\       d888   \   /~~~8e  _888__  e88~~8e  
    888       88b 888  888  888 __/  C888         8888           88b  888   d888  88b 
    888  e88~-888 888  888  888       Y88b        8888      e88~-888  888   8888__888 
|   88P C888  888 888  888  888        888D       Y888   / C888  888  888   Y888    , 
 \__8"   "88_-888 888  888  888      \_88P         "88_-~   "88_-888  888    "88___/ 
______________________________________________________________________________________\n                                                                                  
''')

# Prints a welcome message upon app launch  
def welcome():
    app_title()
    print('Welcome to the Jam\'s Cafe app!\n\n')


# Clears the terminal for aesthetic purposes
def clear_terminal():
    system('clear')


# User input error messages
def invalid_number_error():
    print('Ooops! You\'ve chosen an invalid option. Please try again.\n')

def invalid_input_error():
    print('Ooops! You must enter an option number. Please try again.\n')


# Returns user to the menu they last viewed
def return_to_menu():
    input('\n\nPress Enter key to return to the menu... ')
    clear_terminal()
    app_title()


# Gets the relevant list of dictionary keys/field names for each item type
def get_field_names(item_type):
    if type(item_type) is str:
        if item_type in ['sandwich', 'cake', 'drink']:
            dict_keys = {
                            'name': 'Product', 
                            'price': 'Price'
                        }
        
        elif item_type == 'courier':
            dict_keys = {
                            'name': 'Courier', 
                            'phone': 'Phone Number'
                        }
        
        elif item_type == 'order':
            dict_keys = {
                            'order_number': 'Order No.', 
                            'order_date': 'Order Date', 
                            'customer_name': 'Customer Name', 
                            'customer_address': 'Customer Address', 
                            'customer_phone': 'Customer Phone', 
                            'courier': 'Courier', 
                            'order_status': 'Order Status', 
                            'sandwiches': 'Sandwiches', 
                            'cakes': 'Cakes', 
                            'drinks': 'Drinks'
                        }

    else:
        dict_keys = {}
        
    return dict_keys