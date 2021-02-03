### RUNS JAM'S CAFE APP ###
# Jam's Cafe app v0.9

# Updates in this version:
# Menu functionality split into separate modules
# Large, complex functions broken down into smaller components

import utils, data, appmenus, ordermenu, pcmenus, actions
from datetime import datetime


### IMPORTING APP DATA ###
# Gets app data from .csv files and stores as lists of dictionaries whilst app is running
sandwiches = data.get_data_from_csv('./source/data/sandwiches.csv')
cakes = data.get_data_from_csv('./source/data/cakes.csv')
drinks = data.get_data_from_csv('./source/data/drinks.csv')
couriers = data.get_data_from_csv('./source/data/couriers.csv')
orders = data.get_data_from_csv('./source/data/orders.csv')

# Reformats product data in orders list
orders = data.products_str_to_lst(orders)


### SAVING DATA AND EXITING THE APP ###
# Writes app data to .txt files and exits the app
def exit_app():
    global orders
    # Reformats product data in orders list
    orders = data.products_lst_to_str(orders)
    
    data.write_data_to_csv('./source/data/sandwiches.csv', sandwiches, 'sandwich')
    data.write_data_to_csv('./source/data/cakes.csv', cakes, 'cake')
    data.write_data_to_csv('./source/data/drinks.csv', drinks, 'drink')
    data.write_data_to_csv('./source/data/couriers.csv', couriers, 'courier')
    data.write_data_to_csv('./source/data/orders.csv', orders, 'order')
    
    utils.clear_terminal()
    utils.app_title()
    print('Thanks for using our app, see you again soon!\n')
    exit()


### PRODUCT MENU NAVIGATION ###
reload_product_menu = True # Condition on while loop that reloads product menu

# Loads product menus after user selects product type
def product_menu(item_list, item_type):
    global reload_product_menu
    
    while True: # Reloads product menu(s)
        product_menu_choice = appmenus.product_menu(item_type) # Gets user's product menu selection
        utils.clear_terminal()
        utils.app_title()
        try:
            product_menu_choice = int(product_menu_choice)
            if product_menu_choice == 1:
                actions.print_item_list(item_list, item_type)

            elif product_menu_choice == 2:
                pcmenus.add_new_item(item_list, item_type)
            
            elif product_menu_choice == 3:
                pcmenus.update_item(item_list, item_type)
            
            elif product_menu_choice == 4:
                pcmenus.remove_item(item_list, item_type)
            
            elif product_menu_choice == 5:
                break # Returns to product type menu
            
            elif product_menu_choice == 6:
                reload_product_menu = False
                break # Returns to main menu
        
            elif product_menu_choice == 0:
                exit_app()
                
            else:
                utils.invalid_number_error()
        except ValueError:
            utils.invalid_input_error()


### MAIN MENU NAVIGATION ###
# Enables user to navigate through the app's menu and make changes
def navigate_menu():
    global reload_product_menu
    
    while True: # Reloads the app menu
        main_choice = appmenus.display_main_menu() # Gets user's main menu selection
        utils.clear_terminal()
        utils.app_title()
        
        try: # Processes user's main menu selection
            main_choice = int(main_choice)
            
            if main_choice == 1: # Launches the product type menu
                reload_product_menu = True
                
                while reload_product_menu == True: # Reloads product menu
                    product_type_choice = appmenus.product_type_menu() # Gets user's product type menu selection
                    utils.clear_terminal()
                    utils.app_title()
                    
                    try:
                        product_type_choice = int(product_type_choice)
                        
                        if product_type_choice == 1:
                            product_menu(sandwiches, 'sandwich') # Loads sandwich menu
                            
                        elif product_type_choice == 2:
                            product_menu(cakes, 'cake') # Loads cake menu
                        
                        elif product_type_choice == 3:
                            product_menu(drinks, 'drink') # Loads drink menu
                        
                        elif product_type_choice == 4:
                            break # Returns to main menu
                    
                        elif product_type_choice == 0:
                            exit_app()
                            
                        else:
                            utils.invalid_number_error()

                    except ValueError:
                        utils.invalid_input_error()
                    
            elif main_choice == 2: # Launches the courier menu
                while True: # Reloads courier menu
                    item_type = 'courier'
                    courier_menu_choice = appmenus.courier_menu() # Gets user's courier menu selection
                    utils.clear_terminal()
                    utils.app_title()
                    
                    try:
                        courier_menu_choice = int(courier_menu_choice)
                        
                        if courier_menu_choice == 1:
                            actions.print_item_list(couriers, 'courier')
                        
                        elif courier_menu_choice == 2:
                            pcmenus.add_new_item(couriers, item_type)
                        
                        elif courier_menu_choice == 3:
                            pcmenus.update_item(couriers, item_type)
                        
                        elif courier_menu_choice == 4:
                            pcmenus.remove_item(couriers, item_type)
                        
                        elif courier_menu_choice == 5:
                            break # Returns to main menu
                        
                        elif courier_menu_choice == 0:
                            exit_app()
                        
                        else:
                            utils.invalid_number_error()
                        
                    except ValueError:
                        utils.invalid_input_error()
            
            elif main_choice == 3: # Launches the order menu
                while True: # Reloads order menu
                    order_menu_choice = appmenus.order_menu() # Gets user's order menu selection
                    utils.clear_terminal()
                    utils.app_title()
                    
                    try:
                        order_menu_choice = int(order_menu_choice)
                        
                        if order_menu_choice == 1:
                            actions.print_item_list(orders, 'order')
                        
                        elif order_menu_choice == 2:
                            ordermenu.create_new_order(orders, couriers)
                        
                        elif order_menu_choice == 3:
                            ordermenu.update_status(orders)
                        
                        elif order_menu_choice == 4:
                            ordermenu.update_order(orders, couriers)
                        
                        elif order_menu_choice == 5:
                            ordermenu.delete_order(orders)
                        
                        elif order_menu_choice == 6:
                            break # Returns to main menu
                        
                        elif order_menu_choice == 0:
                            exit_app()
                            
                        else:
                            utils.invalid_number_error()
                    
                    except ValueError:
                        utils.invalid_input_error()
            
            elif main_choice == 0:
                exit_app()
                
            else:
                utils.invalid_number_error()
        
        except ValueError:
            utils.invalid_input_error()


### RUNNING THE APP ###
def run_app():
    utils.welcome()
    navigate_menu()

run_app()


