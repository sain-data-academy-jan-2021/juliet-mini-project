### ORDER MENU FUNCTIONALITY ###

from datetime import datetime
import utils, shared


### CREATING NEW ORDERS ###

# Validates user's courier selection against courier list
def validated_courier(courier_list):
    shared.print_tabulated_list(courier_list, 'courier')
    max_courier_id = len(courier_list) - 1
    
    while True:
        courier_id = input(f'Courier ID (or press Enter to skip): ')
        if not courier_id:
            return ''
        
        try:
            courier_id = int(courier_id)
            if courier_id > max_courier_id:
                print(f'Ooops! Please select a valid Courier ID or leave blank.\n')
            else:
                return courier_id
            
        except ValueError:
            print(f'Ooops! Please select a valid Courier ID or leave blank.\n')


# Validates user's product selection against product lists
def validated_product(product_list, product_type):
    selected_products = []
    shared.print_tabulated_list(product_list, product_type)
    max_product_id = len(product_list) - 1
    product_id = input(f'{product_type.capitalize()} ID (or press Enter to skip): ')
    
    while product_id:
        try:
            product_id = int(product_id)
            
            if product_id > max_product_id:
                print(f'Ooops! Please select a valid {product_type.capitalize()} ID or leave blank.\n')
            else:
                selected_products.append(product_id)
            
        except ValueError:
            print(f'Ooops! Please select a valid {product_type.capitalize()} ID or leave blank.\n')
            
        finally:
            product_id = input(f'{product_type.capitalize()} ID (or press Enter to continue): ')
    
    return sorted(selected_products)


# Validates order to check that user has added products to their order!
def order_validation():
    utils.clear_terminal()
    utils.app_title()
    print('We\'re sorry. Your order could not be placed as you didn\'t select any products.')
    utils.return_to_menu()
    

# Generates order number and sets order date & time
def order_autocalc(orders_list):
    try:
        o_number = orders_list[-1].get('order_number', 'JAM-0')
        o_number = 'JAM-' + str(int(o_number[4:]) + 1)
    except IndexError:
        o_number = 'JAM-1'
    
    # Sets order date as current date & time
    o_date = datetime.strftime(datetime.now(), '%d/%m/%Y %H:%M')
    
    return o_number, o_date


# Prints order confirmation message
def order_confirmation(o_name, o_number, o_date, o_sandwiches, o_cakes, o_drinks):
    utils.clear_terminal()
    utils.app_title()
    print('-------- JAM\'S ORDER CONFIRMATION --------\n')
    print(f'''Thanks for your order, {o_name}!\n
YOUR ORDER SUMMARY
Order number: {o_number}
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
def create_new_order(orders_list, couriers_list, sandwich_list, cake_list, drink_list):
    print('\n-------- JAM\'S ORDER FORM --------\n')
    print('(* indicates required fields)\n')
    
    reload_order_screen('CUSTOMER CONTACT DETAILS')
    o_name = shared.required_field('Customer name', True)
    if o_name == '0': # Cancels and returns to order menu
        utils.clear_terminal()
        utils.app_title()
    
    else: # Prompts user to complete rest of order form & validates courier/product selection
        o_address = shared.required_field('Customer address', False)
        o_phone = shared.required_field('Customer phone', False)
        
        reload_order_screen('PREFFERED COURIER')
        o_courier = validated_courier(couriers_list)
        
        reload_order_screen('SANDWICHES & WRAPS')
        o_sandwiches = validated_product(sandwich_list, 'sandwich')
        reload_order_screen('CAKES & PASTRIES')
        o_cakes = validated_product(cake_list, 'cake')
        reload_order_screen('HOT & COLD DRINKS')
        o_drinks = validated_product(drink_list, 'drink')
        
        if (not o_sandwiches) and (not o_cakes) and (not o_drinks):
            order_validation()
            return

        # Generates order number and sets order date
        o_number, o_date = order_autocalc(orders_list)
        
        # Appends new order to the orders list
        orders_list.append(
            {
                'order_number': o_number,
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
        order_confirmation(o_name, o_number, o_date, o_sandwiches, o_cakes, o_drinks)
        utils.return_to_menu()


### UPDATING ORDER STATUS ###

def update_status(orders_list):
    # Gets a list of all order numbers
    o_numbers = [order.get('order_number') for order in orders_list]
    statuses = ['PREPARING', 'READY', 'OUT FOR DELIVERY', 'DELIVERED', 'COMPLETED', 'CANCELLED', 'DELAYED', 'REJECTED']
    
    o_number = input('Enter order number to be updated (or enter 0 to cancel): ').upper()
    if o_number == '0': # Cancels and returns user to order menu
        utils.clear_terminal()
        utils.app_title()
        return
    
    elif o_number not in o_numbers: # Checks if order number is valid
        print(f'\nOrder {o_number} could not be found. Order number is either invalid or it has been deleted from our system.' )
    
    else: # Updates order status
        print('\nStatuses:- ' + ', '.join(statuses))
        o_status = input('Enter new order status: ').upper()
        
        # Checks that inputted status is valid
        while not o_status in statuses:
            print(f'\n{o_status} is not a valid status.')
            o_status = input('Enter new order status: ').upper()
            
        for order in orders_list:
            if order.get('order_number') == o_number:
                order['order_status'] = o_status
                print(f'\nThe order status of {o_number} has been updated to {o_status}.')
                break
    
    utils.return_to_menu()


# Pushes out changes requested by user (if any) to the orders list #BROKEN!
def update_orders_list(o_number, orders_list, order_properties):
    update_count = 0
    for order in orders_list:
        if order.get('order_number') == o_number: # Finds matching order number
            for key, value in order_properties.items():
                if value != '': # Updates fields if any changes have been requested
                    order[key] = value
                    update_count += 1
            break
        
    if update_count > 0:
        print(f'\nOrder {o_number} has been successfully updated.')
    else:
        print(f'\nYou did not make any changes to order {o_number}.')


# Updates customer and courier fields for specified order #BROKEN!
def update_order(orders_list, couriers_list):
    # Gets a list of all order numbers
    o_numbers = [order.get('order_number') for order in orders_list]
    
    print('-------- JAM\'S ORDER UPDATE FORM --------\n')
    o_number = input('Enter reference number of order to be updated (or enter 0 to cancel): ').upper()
    
    if o_number == '0': # Cancels and returns user to order menu
        utils.clear_terminal()
        utils.app_title()
        return
    
    elif o_number not in o_numbers: # Checks if order number is valid
        print(f'\nOrder {o_number} could not be found. Order number is either invalid or it has been deleted from our system.' )

    else: # Prompts user to complete rest of order form
        print('\nComplete the fields below to update your order. Leave fields blank if no changes are required.\n')
        o_name = input('Customer\'s name: ')
        o_address = input('Customer\'s address: ')    
        o_phone = input('Customer\'s phone: ')
        o_courier = validate_courier(couriers_list)
        
        order_properties = {
            'customer_name': o_name, 
            'customer_address': o_address, 
            'customer_phone': o_phone,
            'courier': o_courier
            }
        
        update_orders_list(o_number, orders_list, order_properties)
        
    utils.return_to_menu()


# Deletes an order from the orders list
def delete_order(orders_list):
    # Gets a list of all order numbers
    o_numbers = [order.get('order_number') for order in orders_list]
    
    o_number = input('Enter order number to be deleted (or enter 0 to cancel): ').upper()
    if o_number == '0': # Cancels and returns user to order menu
        utils.clear_terminal()
        utils.app_title()
        return
    
    elif o_number not in o_numbers: # Checks if order number is valid
        print(f'\nOrder {o_number} could not be found. Order number is either invalid or it has been deleted from our system.' )
    
    else: # Deletes order
        for order in orders_list:
            if order.get('order_number') == o_number:
                orders_list.remove(order)
                print(f'\nOrder {o_number} has been deleted.')
                break
    
    utils.return_to_menu()
