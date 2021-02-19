### COURIER MENU FUNCTIONALITY ###

import utils, shared, db


### CREATING NEW COURIERS ###

# Creates a new record in the couriers db table
def add_new_courier(item_type):
    try:
        courier_names = db.get_single_column_from_db_table(item_type, 'name')
    except:
        utils.return_to_menu()
        return
    
    print(f'-------- ADD A NEW COURIER --------\n')
    print('(* indicates a required field)\n')
    new_courier = shared.required_field(f'Courier name', True).capitalize()
    
    if new_courier == '0': # Cancels and returns to sub-menu
        utils.clear_terminal()
        utils.app_title()
        return
    
    elif not new_courier in courier_names:
        new_phone = shared.required_field('Phone', False)
        values = f'\'{new_courier}\', \'{new_phone}\''
        
        try:
            db.create_new_record(item_type, values)
            print(f'\n{new_courier} has been successfully added as a new courier.')
        
        except:
            utils.return_to_menu()
            return
        
    else:
        print(f'\n{new_courier} is already one of our couriers.')
    
    utils.return_to_menu()



### UPDATING EXISTING COURIERS ###

# Updates a record within the couriers db table
def update_courier(item_type):
    print(f'-------- UPDATE AN EXISTING COURIER --------\n')
    try:
        shared.print_table(item_type)
        courier_ids = db.get_single_column_from_db_table(item_type, 'id')
    except:
        utils.return_to_menu()
        return
    
    courier_id = input('\nCourier ID (enter 0 to cancel): ')
    
    try:
        courier_id = int(courier_id)
    except ValueError:
        pass
    
    if courier_id == 0: # Cancels and returns user to sub-menu
        utils.clear_terminal()
        utils.app_title()
        return
    
    # Updates product if it exists within the db table
    elif courier_id in courier_ids:
        courier_name = input('Updated courier name (press Enter to skip): ').capitalize()
        courier_phone = input('Updated phone (press Enter to skip): ')
                
        user_input = {
            'name': courier_name, 
            'phone': courier_phone
            }
        
        try:
            item_name = db.get_name_of_one_item_from_db_table(item_type, courier_id)
            values_to_update = shared.concat_values_to_update(user_input, item_name)
            
            if values_to_update:
                db.update_record_in_db(item_type, courier_id, values_to_update)
                print(f'\nThe courier record for {item_name} has been successfully updated.')
            else:
                print(f'\nYou did not make any changes to the courier record for {item_name}.')
            
        except:
            utils.return_to_menu()
            return
        
    else:
        print(f'\nCourier {courier_id} could not be found as the Courier ID is invalid.')
    
    utils.return_to_menu()

