### ORDER MENU FUNCTIONALITY ###

from datetime import datetime
import utils, shared, db
from appmenu import display_order_menu


### CREATING NEW ORDERS ###

# Validates user's courier selection against couriers db table
def validated_courier():
    shared.print_table('courier')
    courier_ids = db.get_single_column_from_db_table('courier', 'id')
    courier_id = input(f'Courier ID (or press Enter to skip): ')
    
    while courier_id:
        try:
            courier_id = int(courier_id)
            
            if not courier_id in courier_ids:
                print(f'Ooops! Please select a valid Courier ID or leave blank.\n')
            else:
                return courier_id
            
        except ValueError:
            print(f'Ooops! Please select a valid Courier ID or leave blank.\n')
            courier_id = input(f'Courier ID (or press Enter to skip): ')

    if not courier_id:
        return 'NULL'


# Validates user's product selection against products db table
def validated_product(product_type, state = 'create'):
    selected_products = []
    shared.print_table(product_type)
    product_ids = db.get_single_column_from_db_table(product_type, 'id')
    
    if state == 'create':
        product_id = input(f'{product_type.capitalize()} ID (or press Enter to skip): ')
    else:
        print('Leave field blank if no changes are required. Enter 0 to clear your previous selection.\n')
        product_id = input(f'{product_type.capitalize()} ID: ')
    
    if state == 'create' and product_id == '':
        return 'NULL'
    elif product_id == '':
        return ''
    
    while product_id:
        try:
            product_id = int(product_id)
            
            if state != 'create' and product_id == 0: # Enables previous product selections to be cleared
                return '0'
            
            elif not product_id in product_ids:
                print(f'Ooops! Please select a valid {product_type.capitalize()} ID or leave blank.\n')
            else:
                selected_products.append(product_id)
            
        except ValueError:
            print(f'Ooops! Please select a valid {product_type.capitalize()} ID or leave blank.\n')

        product_id = input(f'{product_type.capitalize()} ID (or press Enter to continue): ')
    
    return utils.num_lst_to_str(sorted(selected_products))


# Validates order to check that user has added products to their order
def empty_order_msg():
    utils.clear_terminal()
    utils.app_title()
    print('We\'re sorry. Your order could not be placed as you didn\'t select any products.')
    utils.return_to_menu()
    

# Generates order id and sets order date & time
def order_autocalc():
    try:
        order_number = db.get_highest_item_id_from_db_table('order') + 1
        order_number = 'JAM-' + str(order_number)
        
    except TypeError:
        order_number = 'JAM-1'
        
    # Sets order date as current date & time
    order_date = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
    
    return order_number, order_date


# Prints order confirmation message
def order_confirmation(order_name, order_number, order_date, order_courier, order_sandwiches, order_cakes, order_drinks):
    utils.clear_terminal()
    utils.app_title()
    print('-------- JAM\'S ORDER CONFIRMATION --------\n')
    print(f'''Thanks for your order, {order_name}!\n
YOUR ORDER SUMMARY
Order Number: {order_number}
Order date: {order_date}
Courier: {order_courier}
Sandwiches: {order_sandwiches}
Cakes: {order_cakes}
Drinks: {order_drinks}
Order status: PREPARING''')


# Reloads/tidies up create order screen in between courier/product selections
def load_order_screen(section_heading, state = 'create'):
    utils.clear_terminal()
    utils.app_title()
    
    if state == 'create':
        print('-------- PLACE A NEW ORDER --------\n')
        
    else:
        print('-------- UPDATE ORDER DETAILS --------\n')
        print('Complete the fields below to update your order details. Leave fields blank if no changes are required.\n')
        
    print(f'{section_heading}')
    print('(* indicates a required field)\n')


# Creates a new order and adds it to the orders list
def create_new_order():
    load_order_screen('CUSTOMER CONTACT DETAILS')
    order_name = shared.required_field('Customer name', True)
    if order_name == '0': # Cancels and returns to order menu
        utils.clear_terminal()
        utils.app_title()
    
    else: # Prompts user to complete rest of order form & validates courier/product selection
        order_phone = shared.required_field('Customer phone', False)
        order_address = shared.required_field('Customer address', False)
        
        try:
            load_order_screen('PREFFERED COURIER')
            order_courier = validated_courier()
            load_order_screen('SANDWICHES & WRAPS')
            order_sandwiches = validated_product('sandwich')
            load_order_screen('CAKES & PASTRIES')
            order_cakes = validated_product('cake')
            load_order_screen('HOT & COLD DRINKS')
            order_drinks = validated_product('drink')
            
            order_number, order_date = order_autocalc()
        
            # Order validation
            if (not order_sandwiches) and (not order_cakes) and (not order_drinks):
                empty_order_msg()
                return

            # Concatenates order data for use as SQL query to update the db
            order_data = f'\'{order_number}\', \'{order_date}\', \'PREPARING\', \'{order_name}\', \'{order_address}\', \'{order_phone}\', {order_courier}, \'{order_sandwiches}\', \'{order_cakes}\', \'{order_drinks}\''
            order_data = order_data.replace('\'NULL\'', 'NULL')
            db.create_new_record('order', order_data)
            order_confirmation(order_name, order_number, order_date, order_courier, order_sandwiches, order_cakes, order_drinks)
            
        except:
            print('Unfortunately your order cannot be placed at this time. Please call us to place an order.')
        
        utils.return_to_menu()



### UPDATING ORDER STATUS ###

def update_order_status():
    statuses = ['PREPARING', 'READY', 'OUT FOR DELIVERY', 'DELIVERED', 'COMPLETED', 'CANCELLED', 'DELAYED', 'REJECTED']
    print(f'-------- UPDATE ORDER STATUS --------\n')
    
    try:
        shared.print_table('order')
        order_ids = db.get_single_column_from_db_table('order', 'id')
        
    except:
        utils.return_to_menu()
        return
    
    # User selects ID of item to be updated
    order_id = input(f'Order ID to be updated (or enter 0 to cancel): ')
    
    try:
        order_id = int(order_id)
    except ValueError:
        pass
    
    if order_id == 0: # Cancels and returns user to order menu
        utils.clear_terminal()
        utils.app_title()
        return

    elif order_id in order_ids: # Checks if order id is valid then updates status       
        print('\nStatuses:- ' + ', '.join(statuses))
        new_status = input('New order status: ').upper()
        
        # Checks that inputted status is valid
        while not new_status in statuses:
            print(f'\n{new_status} is not a valid status.')
            new_status = input('Enter new order status: ').upper()
                
        try:
            order_number = db.get_name_of_one_item_from_db_table('order', order_id)
            new_values = f'order_status = \'{new_status}\''
            db.update_record_in_db('order', order_id, new_values)
            print(f'\nThe order status of {order_number} has been updated to {new_status}.')
            
        except:
            utils.return_to_menu()
            return
    
    else:
        print(f'\nOrder ID {order_id} could not be found. Order ID is either invalid or it has been deleted from our database.' )
    
    utils.return_to_menu()



### UPDATING ORDER DETAILS ###

# Updates customer and courier fields for specified order
def update_order(item_type):
    print('-------- UPDATE ORDER DETAILS --------\n')
    try:
        shared.print_table(item_type)
        order_ids = db.get_single_column_from_db_table(item_type, 'id')
    except:
        utils.return_to_menu()
        return
    
    order_id = input('Order ID (or enter 0 to cancel): ')
    
    try:
        order_id = int(order_id)
    except ValueError:
        pass
    
    if order_id == 0: # Cancels and returns user to order menu
        utils.clear_terminal()
        utils.app_title()
        return
    
    elif order_id in order_ids:
        load_order_screen('CUSTOMER CONTACT DETAILS', 'update')
        order_name = input('Customer\'s name: ')
        order_address = input('Customer\'s address: ')
        order_phone = input('Customer\'s phone: ')
        
        try:
            load_order_screen('PREFFERED COURIER', 'update')
            order_courier = validated_courier()
            load_order_screen('SANDWICHES & WRAPS', 'update')
            order_sandwiches = validated_product('sandwich', 'update')
            load_order_screen('CAKES & PASTRIES', 'update')
            order_cakes = validated_product('cake', 'update')
            load_order_screen('HOT & COLD DRINKS', 'update')
            order_drinks = validated_product('drink', 'update')
            
            user_input = {
                'customer_name': order_name, 
                'customer_phone': order_phone,
                'customer_address': order_address, 
                'courier': order_courier,
                'sandwiches': order_sandwiches, 
                'cakes': order_cakes, 
                'drinks': order_drinks
                }
                        
            order_number = db.get_name_of_one_item_from_db_table(item_type, order_id)
            values_to_update = shared.concat_values_to_update(user_input, order_number)
            
            if values_to_update:
                db.update_record_in_db(item_type, order_id, values_to_update)
                print(f'\nOrder {order_number} has been successfully updated.')
            
            else:
                print(f'\nYou did not make any changes to order {order_number}.')
            
        except:
            print('Unfortunately your order cannot be updated at this time. Please call us to amend your order.')
        
    else:
        print(f'\nOrder {order_id} could not be found. Order ID is either invalid or it has been deleted from our system.' )
    
    utils.return_to_menu()



### APP MENU ###

# Loads order menu within the app
def load_order_menu():
    while True:
        item_type = 'order'
        menu_choice = display_order_menu() # Gets user's menu option selection
        utils.clear_terminal()
        utils.app_title()
        
        try:
            menu_choice = int(menu_choice)
            
            if menu_choice == 1:
                shared.print_table_with_title(item_type)
            
            elif menu_choice == 2:
                create_new_order()
            
            elif menu_choice == 3:
                update_order_status()
            
            elif menu_choice == 4:
                update_order(item_type)
            
            elif menu_choice == 5:
                shared.delete_item(item_type)
            
            elif menu_choice == 6:
                break # Returns to main menu
            
            elif menu_choice == 0:
                utils.exit_app()
                
            else:
                utils.invalid_number_error()
        
        except ValueError:
            utils.invalid_input_error()
