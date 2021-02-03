### PRODUCT MENU AND COURIER MENU FUNCTIONALITY ###

import utils


# Adds a new item to the product/courier lists
def add_new_item(list, item_type):
    new_item = input(f'Enter name of {item_type} to be added (or enter 0 to cancel): ').capitalize()
    if new_item == '0': # Cancels and returns to sub-menu
        utils.clear_terminal()
        utils.app_title()
        return
    
    elif not new_item in list:
        list.append(new_item)
        print(f'\n{new_item} has just been added to the {item_type} list!')
        
    else:
        print(f'{new_item} is already on the {item_type} list!')
    
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