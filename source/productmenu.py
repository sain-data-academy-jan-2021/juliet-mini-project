### PRODUCT MENU FUNCTIONALITY ###

import utils, shared, db


### CREATING NEW PRODUCTS ###

# Creates a new product and adds it to the relevant product list
def add_new_product(item_type):
    # Gets a list of all product names (for the type)
    try:
        product_names = db.get_single_column_from_db_table(item_type, 'name')
        
    except:
        utils.return_to_menu()
        return
    
    print(f'-------- ADD A NEW {item_type.upper()} --------\n')
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



# ---------------------- BROKEN STUFF ---------------------------------------- #

### UPDATING EXISTING PRODUCTS ###

# Updates an existing item on the product list
def update_product(product_list, product_type):
    print(f'\n-------- UPDATE AN EXISTING {product_type.upper()} --------\n')
    shared.print_tabulated_list(product_list, product_type)
    product_ids = [product.get('id') for product in product_list]
    product_id = input(f'\n{product_type.capitalize()} ID (or enter 0 to cancel): ')
    
    try:
        product_id = int(product_id)
    except ValueError:
        pass
    
    if product_id == 0: # Cancels and returns user to sub-menu
        utils.clear_terminal()
        utils.app_title()
        return
    
    elif product_id in product_ids: # Updates product if it exists on the list
        product_name = input('Name: ')
        product_price = input('Price: ')
        
        try:
            if product_price:
                product_price = round(float(product_price), 2)
                
            product_properties = {
                'name': product_name, 
                'price': product_price
                }
        
            shared.update_item_list(product_id, product_list, product_type, product_properties)
        
        except ValueError:
            print(f'\n{product_type.capitalize()} {product_id} could not be updated as Price must be a number.')
    
    else:
        print(f'\n{product_type.capitalize()} {product_id} could not be found as the {product_type.capitalize()} ID is invalid.')
    
    utils.return_to_menu()
