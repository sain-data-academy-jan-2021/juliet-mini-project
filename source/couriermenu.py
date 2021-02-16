### COURIER MENU FUNCTIONALITY ###

import utils, shared, db


### CREATING NEW COURIERS ###

# Creates a new courier and adds it to the courier list
def add_new_courier(db_table):
    # Gets a list of all courier names
    try:
        courier_names = db.get_field_from_db_table(db_table, 'name')
    except:
        utils.return_to_menu()
        return
    
    print(f'\n-------- ADD A NEW COURIER --------\n')
    print('(* indicates a required field)\n')
    new_courier = shared.required_field(f'Courier name', True).capitalize()
    
    if new_courier == '0': # Cancels and returns to sub-menu
        utils.clear_terminal()
        utils.app_title()
        return
    
    elif not new_courier in courier_names:
        new_phone = shared.required_field('Phone', False).capitalize()
        values = f'\'{new_courier}\', \'{new_phone}\''
        
        try:
            db.create_new_record(db_table, values)
        
        except:
            utils.return_to_menu()
            return            
        
        else:
            utils.clear_terminal()
            utils.app_title()
            name_col = get_name_col_for_item(db_table)
            print(f'\n{new_courier} has been set up as a new courier!')

    else:
        print(f'\n{new_courier} is already one of our couriers!')
    
    utils.return_to_menu()


# ---------------------- BROKEN STUFF ---------------------------------------- #

### UPDATING EXISTING COURIERS ###

# Updates an existing person on the courier list
def update_courier(courier_list):
    print(f'\n-------- UPDATE AN EXISTING COURIER --------\n')
    shared.print_tabulated_list(courier_list, 'courier')
    courier_ids = [courier.get('id') for courier in courier_list]
    courier_id = input('\nCourier ID (or enter 0 to cancel): ')
    
    try:
        courier_id = int(courier_id)
    except ValueError:
        pass
    
    if courier_id == 0: # Cancels and returns user to sub-menu
        utils.clear_terminal()
        utils.app_title()
        return
    
    # Updates product if it exists on the list
    elif courier_id in courier_ids:
        courier_name = input('Name: ')
        courier_phone = input('Phone: ')
                
        courier_properties = {
            'name': courier_name, 
            'phone': courier_phone
            }
        
        shared.update_item_list(courier_id, courier_list, 'courier', courier_properties)
    
    else:
        print(f'\nCourier {courier_id} could not be found as the Courier ID is invalid.')
    
    utils.return_to_menu()
