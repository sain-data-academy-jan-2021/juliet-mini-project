### ORDER MENU FUNCTIONALITY ###

from datetime import datetime
import utils


# Renders user-inputted fields as required (used when creating new orders)
def required_field(field_name):
    
    if field_name == 'Customer name':
        o_field = input(f'* {field_name} (or enter 0 to cancel): ')  
    else:
        o_field = input(f'* {field_name}: ')
    
    while o_field == '':
        print(f'This is a required field. Please provide {field_name}.\n')
        o_field = input(f'* {field_name}: ')
        
    return o_field


# Validates user's courier selection against courier list
def validate_courier(couriers_list):
    print('\nAvailable couriers:- ' + ', '.join(couriers_list))
    
    o_courier = input('Preferred courier: ').capitalize()
    while not o_courier in (couriers_list + ['']):
        print(f'\n{o_courier} is unavailable. Please select an available courier or leave blank.')
        o_courier = input('Preferred courier: ').capitalize()
    
    return o_courier


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
def order_confirmation(o_name, o_number, o_date):
    utils.clear_terminal()
    utils.app_title()
    print('-------- JAM\'S ORDER CONFIRMATION --------\n')
    print(f'''Thanks for your order, {o_name}!\n
YOUR ORDER SUMMARY
Order number: {o_number}
Order date: {o_date}
Order status: PREPARING''')


# Creates a new order and adds it to the orders list
def create_new_order(orders_list, couriers_list):
    print('-------- JAM\'S ORDER FORM --------\n')
    print('(* indicates required fields)\n')
    
    o_name = required_field('Customer name')
    if o_name == '0': # Cancels and returns to order menu
        utils.clear_terminal()
        utils.app_title()
    
    else: # Prompts user to complete rest of order form & validates courier selection
        o_address = required_field('Customer address')
        o_phone = required_field('Customer phone')
        o_courier = validate_courier(couriers_list)

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
            }
        )
        
        order_confirmation(o_name, o_number, o_date)
        utils.return_to_menu()


# Updates order status
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


# Pushes out changes requested by user (if any) to the orders list
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


# Updates customer and courier fields for specified order
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
