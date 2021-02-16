### LIST ACTIONS - PRINT, CREATE, UPDATE AND DELETE ###

import utils, db
import tabulate


### PRINTING DB TABLES ###
# Gets custom title for a printed table of products/couriers/orders ***DO NOT DELETE!***
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
    

# Prints tabulated data from product/courier/order list ***DO NOT DELETE!***
def print_tabulated_list(item_list, item_type, dict_keys):
    if not item_list:
        print(f'The {item_type} list is currently empty.')
        
    else:
        table_headers = utils.tidy_up_col_names_for_printing(dict_keys)
        data = [item.values() for item in item_list]
        print(tabulate.tabulate(data, table_headers, tablefmt = 'psql', floatfmt = '.2f'))


# Gets data from the database table and prints in terminal ***NEW!***
def print_db_table(item_type):
    db_col_names = utils.get_col_names_for_printing(item_type)
    dict_keys = utils.str_to_lst(db_col_names)
    item_list = db.create_list_from_db_table(item_type, db_col_names, dict_keys)
    
    if item_list:
        print_tabulated_list(item_list, item_type, dict_keys)
        
    else:
        print('There is no currently no {item_type} data in our database.')


# Prints data from the db table along with a title, then returns user to app menu ***NEW!***
def print_db_table_with_title(item_type):
    title = get_item_list_title(item_type)
    print(f'{title.upper()}\n')
    print_db_table(item_type)
    utils.return_to_menu()




#-------------BROKEN STUFF------------------------#
### ADDING NEW ITEMS TO DB TABLES ###

# Renders user-inputted fields as required
def required_field(field_name, is_first_field):
    
    if is_first_field:
        o_field = input(f'* {field_name} (or enter 0 to cancel): ')  
    else:
        o_field = input(f'* {field_name}: ')
    
    while o_field == '':
        print(f'\nThis is a required field. Please provide {field_name}.\n')
        o_field = input(f'* {field_name}: ')
        
    return o_field


### DELETING ITEMS FROM DB TABLES ###

# Deletes the selected item from the db table
def delete_item(db_table, item_type):
    print(f'\n-------- DELETE AN EXISTING {item_type.upper()} --------\n')
    try:
        print_db_table(item_type)
        item_ids = db.get_field_from_db_table(db_table, 'id')
        
    except:
        utils.return_to_menu()
        return
    
    # User selects ID of item to be deleted
    item_id = input(f'\n{item_type.capitalize()} ID (or enter 0 to cancel): ')
    
    try:
        item_id = int(item_id)
    except ValueError:
        pass
    
    if item_id == 0: # Cancels and returns user to app menu
        utils.clear_terminal()
        utils.app_title()
        return
    
    elif item_id in item_ids: # Checks if item id is valid then deletes item
        try:
            item_name = db.get_item_name_from_db_table(db_table, item_id)
            db.delete_record_from_db(db_table, item_id)
            print(f'\n{item_name} has been deleted from our database.')
            
        except:
            utils.return_to_menu()
            return
    
    else:
        print(f'\n{item_type.capitalize()} {item_id} could not be found. {item_type.capitalize()} ID is either invalid or it has been deleted from our database.' )
    
    utils.return_to_menu()






### UPDATING ITEMS ON LISTS ###

# Pushes out changes requested by user (if any) to the product/courier list
def update_item_list(item_id, item_list, item_type, item_properties):
    update_count = 0
    
    for key, value in item_properties.items():
        if value: # Updates fields if any changes have been requested
            for item in item_list:
                if item['id'] == item_id:
                    item[key] = value
                    update_count += 1
                    item_name = item['name']
                    break
        
    if update_count > 0:
        print(f'\n{item_name} has been successfully updated.')
    else:
        print(f'\nYou did not make any changes to {item_type.capitalize()} {item_id}.')