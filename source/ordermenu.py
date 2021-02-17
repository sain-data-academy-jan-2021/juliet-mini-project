### ORDER MENU FUNCTIONALITY ###

from datetime import datetime
import utils, shared, db


### CREATING NEW ORDERS ###

# Validates user's courier selection against courier list
def validated_courier():
    shared.print_table('courier')
    courier_ids = db.get_single_column_from_db_table('couriers', 'id')
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
            courier_id = input(f'Courier ID (or press Enter to continue): ')


# Validates user's product selection against product lists
def validated_product(db_table, product_type):
    selected_products = []
    shared.print_table(product_type)
    product_ids = db.get_single_column_from_db_table(db_table, 'id')
    
    product_id = input(f'{product_type.capitalize()} ID (or press Enter to skip): ')
    
    while product_id:
        try:
            product_id = int(product_id)
            
            if not product_id in product_ids:
                print(f'Ooops! Please select a valid {product_type.capitalize()} ID or leave blank.\n')
            else:
                selected_products.append(product_id)
            
        except ValueError:
            print(f'Ooops! Please select a valid {product_type.capitalize()} ID or leave blank.\n')
            
        finally:
            product_id = input(f'{product_type.capitalize()} ID (or press Enter to continue): ')
    
    return sorted(selected_products)


# Validates order to check that user has added products to their order!
def empty_order_msg():
    utils.clear_terminal()
    utils.app_title()
    print('We\'re sorry. Your order could not be placed as you didn\'t select any products.')
    utils.return_to_menu()
    

# Generates order id and sets order date & time
def order_autocalc(orders_list):
    try:
        o_id = orders_list[-1].get('order_id', 'JAM-0')
        o_id = 'JAM-' + str(int(o_id[4:]) + 1)
    except IndexError:
        o_id = 'JAM-1'
    
    # Sets order date as current date & time
    o_date = datetime.strftime(datetime.now(), '%d/%m/%Y %H:%M')
    
    return o_id, o_date


# Prints order confirmation message
def order_confirmation(o_name, o_id, o_date, o_sandwiches, o_cakes, o_drinks):
    utils.clear_terminal()
    utils.app_title()
    print('-------- JAM\'S ORDER CONFIRMATION --------\n')
    print(f'''Thanks for your order, {o_name}!\n
YOUR ORDER SUMMARY
Order ID: {o_id}
Order date: {o_date}
Sandwiches: {o_sandwiches}
Cakes: {o_cakes}
Drinks: {o_drinks}
Order status: PREPARING''')


# Reloads/tidies up create order screen in between courier/product selections
def reload_order_screen(section_heading):
    utils.clear_terminal()
    utils.app_title()
    print('\n-------- JAM\'S ORDER FORM --------\n')
    print(f'\n{section_heading}')


# Creates a new order and adds it to the orders list
def create_new_order(orders_list):
    print('\n-------- JAM\'S ORDER FORM --------\n')
    print('(* indicates a required field)\n')
    
    reload_order_screen('CUSTOMER CONTACT DETAILS')
    o_name = shared.required_field('Customer name', True)
    if o_name == '0': # Cancels and returns to order menu
        utils.clear_terminal()
        utils.app_title()
    
    else: # Prompts user to complete rest of order form & validates courier/product selection
        o_address = shared.required_field('Customer address', False)
        o_phone = shared.required_field('Customer phone', False)
        
        try:
            reload_order_screen('PREFFERED COURIER')
            o_courier = validated_courier()
            
            reload_order_screen('SANDWICHES & WRAPS')
            o_sandwiches = validated_product('sandwiches', 'sandwich')
            reload_order_screen('CAKES & PASTRIES')
            o_cakes = validated_product('cakes', 'cake')
            reload_order_screen('HOT & COLD DRINKS')
            o_drinks = validated_product('drinks', 'drink')
        
        except:
            pass
        
        else:
            # Order validation
            if (not o_sandwiches) and (not o_cakes) and (not o_drinks):
                empty_order_msg()
                return

            # Generates order id and sets order date
            o_id, o_date = order_autocalc(orders_list)
            
            # Appends new order to the orders list
            orders_list.append(
                {
                    'order_id': o_id,
                    'order_date': o_date, 
                    'customer_name': o_name, 
                    'customer_address': o_address, 
                    'customer_phone': o_phone,
                    'courier': o_courier, 
                    'order_status': 'PREPARING',
                    'sandwiches': o_sandwiches, 
                    'cakes': o_cakes, 
                    'drinks': o_drinks
                }
            )
            order_confirmation(o_name, o_id, o_date, o_sandwiches, o_cakes, o_drinks)
        
        finally:
            utils.return_to_menu()


### UPDATING ORDER STATUS ### ***DONE!***

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
    order_id = input(f'\nOrder ID to be updated (or enter 0 to cancel): ')
    
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


# UPDATING ORDER DETAILS

# Pushes out changes requested by user (if any) to the orders list
def update_orders_list(o_id, orders_list, order_properties):
    update_count = 0
    for order in orders_list:
        if order.get('order_id') == o_id: # Finds matching order id
            for key, value in order_properties.items():
                if value: # Updates fields if any changes have been requested
                    order[key] = value
                    update_count += 1
            break
        
    if update_count > 0:
        print(f'\nOrder {o_id} has been successfully updated.')
    else:
        print(f'\nYou did not make any changes to order {o_id}.')


# Updates customer and courier fields for specified order
def update_order(orders_list):
    # Gets a list of all order ids
    o_ids = [order.get('order_id') for order in orders_list]
    
    print('-------- JAM\'S ORDER UPDATE FORM --------\n')
    o_id = input('Order ID (or enter 0 to cancel): ').upper()
    
    if o_id == '0': # Cancels and returns user to order menu
        utils.clear_terminal()
        utils.app_title()
        return
    
    elif o_id not in o_ids: # Checks if order id is valid
        print(f'\nOrder {o_id} could not be found. order id is either invalid or it has been deleted from our system.' )

    else: # Prompts user to complete rest of order form
        print('\nComplete the fields below to update your order. Leave fields blank if no changes are required.\n')
        o_name = input('Customer\'s name: ')
        o_address = input('Customer\'s address: ')    
        o_phone = input('Customer\'s phone: ')
        
        try:
            reload_order_screen('PREFFERED COURIER')
            o_courier = validated_courier()
            
            reload_order_screen('SANDWICHES & WRAPS')
            o_sandwiches = validated_product('sandwiches', 'sandwich')
            reload_order_screen('CAKES & PASTRIES')
            o_cakes = validated_product('cakes', 'cake')
            reload_order_screen('HOT & COLD DRINKS')
            o_drinks = validated_product('drinks', 'drink')
        
        except:
            pass
        
        else:
            order_properties = {
                'customer_name': o_name, 
                'customer_address': o_address, 
                'customer_phone': o_phone,
                'courier': o_courier,
                'sandwiches': o_sandwiches, 
                'cakes': o_cakes, 
                'drinks': o_drinks
                }
            
            update_orders_list(o_id, orders_list, order_properties)
        
        finally:
            utils.return_to_menu()
