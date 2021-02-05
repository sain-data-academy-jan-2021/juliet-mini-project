### PRODUCT MENU AND COURIER MENU FUNCTIONALITY ###

import utils, shared


### CREATING NEW PRODUCTS & COURIERS ###

# Creates a new product and adds it to the relevant product list
def add_new_product(product_list, product_type):
    product_names = [product.get('name') for product in product_list]
    
    print(f'\n-------- ADD A NEW {product_type.upper()} --------\n')
    new_product = shared.required_field(f'New {product_type} name', True).capitalize()
    
    if new_product == '0': # Cancels and returns to sub-menu
        utils.clear_terminal()
        utils.app_title()
        return
    
    elif not new_product in product_names:
        while True:
            new_price = input('Price: ')
            
            try:
                new_price = float(new_price)
                product_list.append({
                                        'name': new_product,
                                        'price': new_price
                                    })
                print(f'\n{new_product} has just been added to the {product_type} list!')
                break
            
            except ValueError:
                print(f'Ooops! {product_type} price must be a number. Please try again.')
            
    else:
        print(f'\n{new_product} is already on the {product_type} list!')
    
    utils.return_to_menu()


# Creates a new courier and adds it to the courier list
def add_new_courier(courier_list):
    courier_names = [courier.get('name') for courier in courier_list]
    
    print(f'\n-------- ADD A NEW COURIER --------\n')
    new_courier = shared.required_field(f'New courier name', True).capitalize()
    
    if new_courier == '0': # Cancels and returns to sub-menu
        utils.clear_terminal()
        utils.app_title()
        return
    
    elif not new_courier in courier_names:
        new_phone = shared.required_field('Phone', False).capitalize()
        courier_list.append({
                                'name': new_courier,
                                'phone': new_phone
                            })
        print(f'\n{new_courier} has just been added to the courier list!')

    else:
        print(f'\n{new_courier} is already on the courier list!')
    
    utils.return_to_menu()


# Updates an existing item on the product/courier lists
def update_item(list, item_type):
    item_to_update = input(f'Enter name of {item_type} to be updated (or enter 0 to cancel): ').capitalize()
    if item_to_update == '0': # Cancels and returns user to sub-menu
        utils.clear_terminal()
        utils.app_title()
        return
    
    try: # Updates item if it exists on the list
        index_num = list.index(item_to_update)
        updated_name = input(f'Enter new name for {item_type}: ').capitalize()
        list[index_num] = updated_name
        print(f'\n{item_to_update} has been changed to {updated_name} on the {item_type} list.')
    
    except ValueError: # Renders an error message if item is not on the list
        if item_type == 'courier':
            print(f'\n{item_to_update} could not be updated as they aren\'t on the {item_type} list.')
            
        else:
            print(f'\n{item_to_update} could not be updated as it isn\'t on the {item_type} list.')
    
    utils.return_to_menu()


# Removes an existing item from the product/courier lists
def remove_item(list, item_type):
    item_to_remove = input(f'Enter name of {item_type} to be removed (or enter 0 to cancel): ').capitalize()
    if item_to_remove == '0': # Cancels and returns user to sub-menu
        utils.clear_terminal()
        utils.app_title()
        return
    
    try: # Removes item if it exists on the list
        list.remove(item_to_remove)
        print(f'\n{item_to_remove} has been removed from the {item_type} list.')
    
    except ValueError: # Renders an error message if item is not on the list
        if item_type == 'courier':
            print(f'\n{item_to_remove} could not be removed as they aren\'t on the {item_type} list.')
            
        else: 
            print(f'\n{item_to_remove} could not be removed as it isn\'t on the {item_type} list.')
    
    utils.return_to_menu()