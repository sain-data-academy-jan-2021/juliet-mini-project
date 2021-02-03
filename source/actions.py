### LIST ACTIONS - PRINT, CREATE, UPDATE AND DELETE ###

import utils
import tabulate


### PRINTING LISTS ###
# Gets custom title for a list of products, couriers or headers
def get_item_list_title(item_type):   
    if item_type == 'sandwich':
        header = 'sandwiches & wraps'
        
    elif item_type == 'cake':
        header = 'cakes & pastries'
        
    elif item_type == 'drink':
        header = 'hot & cold drinks'
        
    elif item_type == 'courier':
        header = 'Jam\'s couriers'
        
    elif item_type == 'order':
        header = 'Jam\'s orders'
        
    else:
        header = 'items'
    
    return header
    
    
# Prints all items in a list of products, couriers or orders
def print_item_list(item_list, item_type):
    title = get_item_list_title(item_type)
    print(f'{title.upper()}\n')
    
    if not item_list:
        print(f'The list of {title} is currently empty.')
        
    else:
        field_names = list(utils.get_field_names(item_type).values())
        data = [item.values() for item in item_list]
        print(tabulate.tabulate(data, field_names, tablefmt = 'psql', floatfmt = '.2f'))
    
    utils.return_to_menu()


### ADDING NEW ITEMS TO LISTS ###
# Renders user-inputted fields as required
def required_field(field_name, is_first_field):
    
    if is_first_field == True:
        field = input(f'* {field_name} (or enter 0 to cancel): ')
    else:
        field = input(f'* {field_name}: ')
    
    while field == '':
        print(f'This is a required field. Please provide {field_name}.\n')
        field = input(f'* {field_name}: ')
        
    return field


# Gets specific fields for relevant item type
def get_required_fields(item_type):
    if item_type in ('sandwich', 'cake', 'drink'):
        required_field('Product name', True)
        required_field('Price', False)
        
    elif item_type == 'courier':
        required_field('Courier name', True)
        required_field('Phone', False)
        
    elif item_type == 'order':
        required_field('Customer name', True)
        required_field('Customer address', False)
        required_field('Customer phone', False)
        required_field('Preferred courier', False) #Move to new function for validated fields
        required_field('Sandwiches', False) #Move to new function for validated fields
        required_field('Cakes', False) #Move to new function for validated fields
        required_field('Drinks', False) #Move to new function for validated fields


# Creates a new item dictionary and adds it to the product/courier/order list
def create_new_order(item_list, item_type):
    print('-------- CREATE A NEW {item_type.upper()} --------\n')
    print('(* indicates required fields)\n')
    get_required_fields(item_type)
    