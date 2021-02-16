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


# Exits the app with a goodbye message
def exit_app():
    clear_terminal()
    app_title()
    print('Thanks for using our app, see you again soon!\n\n')
    exit()


# # Gets the relevant list of dictionary keys/field names for each item type
# def get_field_names(item_type):
#     if type(item_type) is str:
#         if item_type in ['sandwich', 'cake', 'drink']:
#             dict_keys = {
#                             'id': 'ID',
#                             'product_type': 'Product Type',
#                             'name': 'Product', 
#                             'price': 'Price'
#                         }
        
#         elif item_type == 'courier':
#             dict_keys = {
                            
#                             'id': 'ID',
#                             'name': 'Courier', 
#                             'phone': 'Phone Number'
#                         }
        
#         elif item_type == 'order':
#             dict_keys = {
#                             'order_id': 'Order ID', 
#                             'order_date': 'Order Date', 
#                             'customer_name': 'Customer Name', 
#                             'customer_address': 'Customer Address', 
#                             'customer_phone': 'Customer Phone', 
#                             'courier': 'Courier', 
#                             'order_status': 'Order Status', 
#                             'sandwiches': 'Sandwiches', 
#                             'cakes': 'Cakes', 
#                             'drinks': 'Drinks'
#                         }

#     else:
#         dict_keys = {}
        
#     return dict_keys


# Returns the relevant list of column names in the db table, used when printing tables ***GOOD TO GO!***
def get_col_names_for_printing(item_type):
    if item_type in ('sandwich', 'cake', 'drink'):
        col_names = 'id, name, price'
    
    elif item_type == 'courier':
        col_names = 'id, name, phone'
    
    else:
        col_names = 'id, order_number, order_date, order_status, courier, customer_name, customer_phone, customer_address, sandwiches, cakes, drinks'
    
    return col_names


# Cleans dictionary keys (same as db table column headers) ready to be used in printed tables
def tidy_up_col_names_for_printing(dict_keys):
    col_headers = []
    
    if type(dict_keys) is list:
        for i in range(len(dict_keys)):
            col_headers.append(dict_keys[i].replace('_', ' ').title())
    
    return col_headers


# Returns the relevant list of column names in the db table, used when creating new items ***NEW!***
def get_col_names_for_creating(db_table):
    if db_table in ['sandwiches', 'cakes', 'drinks']:
        col_names = 'name, price'
    
    elif db_table == 'couriers':
        col_names = 'name, phone'
    
    else:
        col_names = 'order_id, order_date, customer_name, customer_address, customer_phone, courier, order_status, sandwiches, cakes, drinks'
    
    return col_names


# Converts comma-separated string to a list ***GOOD TO GO!***
def str_to_lst(string):
    if type(string) is str and string:
        str_list = string.split(', ')
        return str_list
    
    else:
        return []


# Returns the relevant 'name' column for a specific table
def get_name_col_for_item(item_type):
    if item_type in ['sandwich', 'cake', 'drink', 'courier']:
        name_col = 'name'
    
    else:
        name_col = 'order_number'
    
    return name_col


