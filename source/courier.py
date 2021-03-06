### COURIER MENU FUNCTIONALITY ###

# from utils import *
# from shared import *
# from database import *
# from appmenu import display_courier_menu

from source.utils import *
from source.shared import *
from source.database import *
from source.appmenu import display_courier_menu


### CREATING NEW COURIERS ###

# Creates a new record in the couriers db table
def add_new_courier(item_type):
    print(f'-------- ADD A NEW COURIER --------\n')
    try:
        courier_names = get_single_column_from_db_table(item_type, 'name')
    except:
        return_to_menu()
        return
    
    print('(* indicates a required field)\n')
    new_courier = required_field(f'Courier name', True).capitalize()
    
    if new_courier == '0': # Cancels and returns to sub-menu
        clear_terminal()
        app_title()
        return
    
    elif not new_courier in courier_names:
        new_phone = required_field('Phone', False)
        values = f'\'{new_courier}\', \'{new_phone}\''
        
        try:
            create_new_record(item_type, values)
            print(f'\n{new_courier} has been successfully added as a new courier.')
        
        except:
            return_to_menu()
            return
        
    else:
        print(f'\n{new_courier} is already one of our couriers.')
    
    return_to_menu()



### UPDATING EXISTING COURIERS ###

# Updates a record within the couriers db table
def update_courier(item_type):
    print(f'-------- UPDATE A COURIER --------\n')
    try:
        print_table(item_type)
        courier_ids = get_single_column_from_db_table(item_type, 'id')
    except:
        return_to_menu()
        return
    
    courier_id = input('Courier ID (enter 0 to cancel): ')
    
    try:
        courier_id = int(courier_id)
    except ValueError:
        pass
    
    if courier_id == 0: # Cancels and returns user to sub-menu
        clear_terminal()
        app_title()
        return
    
    # Updates product if it exists within the db table
    elif courier_id in courier_ids:
        print('\nComplete the fields below to update courier details. Leave fields blank if no changes are required.\n')
        courier_name = input('Courier name: ').capitalize()
        courier_phone = input('Phone: ')
                
        user_input = {
            'name': courier_name, 
            'phone': courier_phone
            }
        
        try:
            item_name = get_name_of_one_item_from_db_table(item_type, courier_id)
            values_to_update = concat_values_to_update(user_input, item_name)
            
            if values_to_update:
                update_record_in_db(item_type, courier_id, values_to_update)
                print(f'\nThe courier record for {item_name} has been successfully updated.')
            else:
                print(f'\nYou did not make any changes to the courier record for {item_name}.')
            
        except:
            return_to_menu()
            return
        
    else:
        print(f'\nCourier {courier_id} could not be found as the Courier ID is invalid.')
    
    return_to_menu()



### APP MENU ###

# Loads courier menu within the app
def load_courier_menu():
    while True:
        item_type = 'courier'
        menu_choice = display_courier_menu() # Gets user's menu option selection
        clear_terminal()
        app_title()
        
        try:
            menu_choice = int(menu_choice)
            
            if menu_choice == 1:
                print_table_with_title(item_type)
            
            elif menu_choice == 2:
                add_new_courier(item_type)
            
            elif menu_choice == 3:
                update_courier(item_type)
            
            elif menu_choice == 4:
                delete_item(item_type)
            
            elif menu_choice == 5:
                break # Returns to main menu
            
            elif menu_choice == 0:
                exit_app()
            
            else:
                invalid_number_error()
            
        except ValueError:
            invalid_input_error()
