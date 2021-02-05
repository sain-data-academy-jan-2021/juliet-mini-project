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
    

# Prints tabulated data from product/courier/order list
def print_tabulated_list(item_list, item_type):
    if not item_list:
        print(f'The {item_type} list is currently empty.')
        
    else:
        field_names = list(utils.get_field_names(item_type).values())
        data = [item.values() for item in item_list]
        print(tabulate.tabulate(data, field_names, tablefmt = 'psql', floatfmt = '.2f', showindex = True))


# Prints tabulated data along with a title, then returns user to app menu
def print_item_list(item_list, item_type):
    title = get_item_list_title(item_type)
    print(f'{title.upper()}\n')
    print_tabulated_list(item_list, item_type)
    utils.return_to_menu()


### ADDING NEW ITEMS TO LISTS ###

# Renders user-inputted fields as required
def required_field(field_name, is_first_field):
    
    if is_first_field:
        o_field = input(f'* {field_name} (or enter 0 to cancel): ')  
    else:
        o_field = input(f'* {field_name}: ')
    
    while o_field == '':
        print(f'This is a required field. Please provide {field_name}.\n')
        o_field = input(f'* {field_name}: ')
        
    return o_field

