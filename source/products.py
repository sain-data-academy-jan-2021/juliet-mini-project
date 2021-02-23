### PRODUCT MENU FUNCTIONALITY ###

import utils, shared, db


### CREATING NEW PRODUCTS ###

# Creates a new record in the products db table
def add_new_product(item_type):
    print(f'-------- ADD A NEW {item_type.upper()} --------\n')
    try:
        product_names = db.get_single_column_from_db_table(item_type, 'name')
        
    except:
        utils.return_to_menu()
        return
    
    print('(* indicates a required field)\n')
    new_product = shared.required_field(f'{item_type.capitalize()} name', True).capitalize()
    
    if new_product == '0': # Cancels and returns to sub-menu
        utils.clear_terminal()
        utils.app_title()
        return
    
    elif not new_product in product_names:
        while True:
            new_price = shared.required_field('Price', False)
            
            try:
                new_price = round(float(new_price), 2)
                values = f'\'{item_type}\', \'{new_product}\', {new_price}'
                
                try:
                    db.create_new_record(item_type, values)
                    print(f'\n{new_product} has successfully been added to our {item_type} range.')
                    break
                
                except:
                    return
                
            except ValueError:
                print(f'\nOoops! Price must be a number. Please try again.\n')
            
    else:
        print(f'\n{new_product} is already part of our {item_type} range.')
    
    utils.return_to_menu()



### UPDATING EXISTING PRODUCTS ###

# Updates a record within the products db table
def update_product(item_type):
    print(f'-------- UPDATE A {item_type.upper()} --------\n')
    try:
        shared.print_table(item_type)
        product_ids = db.get_single_column_from_db_table(item_type, 'id')
    except:
        utils.return_to_menu()
        return
    
    product_id = input(f'{item_type.capitalize()} ID (enter 0 to cancel): ')
    
    try:
        product_id = int(product_id)
    except ValueError:
        pass
    
    if product_id == 0: # Cancels and returns user to sub-menu
        utils.clear_terminal()
        utils.app_title()
        return
    
    # Updates product if it exists within the db table
    elif product_id in product_ids:
        print('\nComplete the fields below to update product details. Leave fields blank if no changes are required.\n')
        product_name = input('Name: ').capitalize()
        product_price = input('Price: ')
        
        user_input = {
            'name': product_name, 
            'price': product_price
            }
        
        try:
            if product_price:
                product_price = round(float(product_price), 2)
            
        except ValueError:
            print('\nThe selected product could not be updated as Price must be a number.')
            utils.return_to_menu()
            return
            
        try:
            item_name = db.get_name_of_one_item_from_db_table(item_type, product_id)
            values_to_update = shared.concat_values_to_update(user_input, item_name)
            
            if values_to_update:
                db.update_record_in_db(item_type, product_id, values_to_update)
                print(f'\nThe product details for {item_name} have been successfully updated.')
            else:
                print(f'\nYou did not make any changes to the product details for {item_name}.')
            
        except:
            utils.return_to_menu()
            return
    
    else:
        print(f'\n{item_type.capitalize()} {product_id} could not be found as the {item_type.capitalize()} ID is invalid.')
    
    utils.return_to_menu()
