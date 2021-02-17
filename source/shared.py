### LIST ACTIONS - PRINT, CREATE, UPDATE AND DELETE ###

import utils, db
import tabulate


### PRINTING TABLES OF ITEMS ###
# Gets custom title for a printed table of products/couriers/orders ***DONE!***
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
    

# Gets data from the database table and prints in terminal ***DONE!***
def print_table(item_type):
    col_names_str = utils.get_col_names_for_printing(item_type) #comma separated string of db column names
    col_names_lst = utils.str_to_lst(col_names_str) #converts the string of col names to a list
    item_data = db.get_multiple_columns_from_db_table(item_type, col_names_str, col_names_lst) #gets data from db and returns a list of dicts
    
    if item_data:
        headers = utils.reformat_col_names(col_names_lst)
        values = [item.values() for item in item_data]
        print(tabulate.tabulate(values, headers, tablefmt = 'psql', floatfmt = '.2f'))
        
    else:
        print('There is no currently no {item_type} data in our database.')


# Prints data from the db table along with a title, then returns user to app menu ***DONE!***
def print_table_with_title(item_type):
    title = get_item_list_title(item_type)
    print(f'{title.upper()}\n')
    print_table(item_type)
    utils.return_to_menu()



### ADDING NEW ITEMS ###

# Renders user-inputted fields as required ***DONE!***
def required_field(field_name, is_first_field):
    
    if is_first_field:
        o_field = input(f'* {field_name} (or enter 0 to cancel): ')  
    else:
        o_field = input(f'* {field_name}: ')
    
    while o_field == '':
        print(f'\nThis is a required field. Please provide {field_name}.\n')
        o_field = input(f'* {field_name}: ')
        
    return o_field



### DELETING ITEMS ###

# Deletes the selected item from the db table ***DONE!***
def delete_item(item_type):
    print(f'-------- DELETE AN EXISTING {item_type.upper()} --------\n')
    try:
        print_table(item_type)
        item_ids = db.get_single_column_from_db_table(item_type, 'id')
        
    except:
        utils.return_to_menu()
        return
    
    # User selects ID of item to be deleted
    item_id = input(f'\n{item_type.capitalize()} ID to be deleted (or enter 0 to cancel): ')
    
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
            item_name = db.get_name_of_one_item_from_db_table(item_type, item_id)
            db.delete_record_from_db(item_type, item_id)
            print(f'\n{item_name} has been deleted from our database.')
            
        except:
            utils.return_to_menu()
            return
    
    else:
        print(f'\n{item_type.capitalize()} ID {item_id} could not be found. {item_type.capitalize()} ID is either invalid or it has already been deleted from our database.' )
    
    utils.return_to_menu()





#-------------BROKEN STUFF------------------------#

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