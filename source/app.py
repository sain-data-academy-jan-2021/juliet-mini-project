### RUNS JAM'S CAFE APP ###
# Jam's Cafe app v2.91

# Updates in this version:
# Product data combined into one db table
# Order data migrated to new database table


import utils, data, appmenus, ordermenu, couriermenu, productmenu, shared, db


### PRODUCT MENU NAVIGATION ###
reload_product_menu = True # Condition on while loop that reloads product menu

# Loads product menus after user selects product type
def product_menu(product_type):
    global reload_product_menu
    
    while True: # Reloads product menu(s)
        product_menu_choice = appmenus.product_menu(product_type) # Gets user's product menu selection
        utils.clear_terminal()
        utils.app_title()
        
        try:
            product_menu_choice = int(product_menu_choice)
            
            if product_menu_choice == 1:
                shared.print_table_with_title(product_type)

            elif product_menu_choice == 2:
                productmenu.add_new_product(product_type)
            
            elif product_menu_choice == 3:
                # productmenu.update_product(product_list, product_type)
                pass #***Need to fix!***
            
            elif product_menu_choice == 4:
                shared.delete_item(product_type)
            
            elif product_menu_choice == 5:
                break # Returns to product type menu
            
            elif product_menu_choice == 6:
                reload_product_menu = False
                break # Returns to main menu
        
            elif product_menu_choice == 0:
                utils.exit_app()
                
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
                            product_menu('sandwich') # Loads sandwich menu
                            
                        elif product_type_choice == 2:
                            product_menu('cake') # Loads cake menu
                        
                        elif product_type_choice == 3:
                            product_menu('drink') # Loads drink menu
                        
                        elif product_type_choice == 4:
                            break # Returns to main menu
                    
                        elif product_type_choice == 0:
                            utils.exit_app()
                            
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
                            shared.print_table_with_title(item_type)
                        
                        elif courier_menu_choice == 2:
                            couriermenu.add_new_courier(item_type)
                        
                        elif courier_menu_choice == 3:
                            # couriermenu.update_courier(couriers)
                            pass #***Need to fix!***
                        
                        elif courier_menu_choice == 4:
                            shared.delete_item(item_type)
                        
                        elif courier_menu_choice == 5:
                            break # Returns to main menu
                        
                        elif courier_menu_choice == 0:
                            utils.exit_app()
                        
                        else:
                            utils.invalid_number_error()
                        
                    except ValueError:
                        utils.invalid_input_error()
            
            elif main_choice == 3: # Launches the order menu
                while True: # Reloads order menu
                    item_type = 'order'
                    order_menu_choice = appmenus.order_menu() # Gets user's order menu selection
                    utils.clear_terminal()
                    utils.app_title()
                    
                    try:
                        order_menu_choice = int(order_menu_choice)
                        
                        if order_menu_choice == 1:
                            shared.print_table_with_title('order')
                        
                        elif order_menu_choice == 2:
                            # ordermenu.create_new_order(orders)
                            pass #***Need to fix!***
                        
                        elif order_menu_choice == 3:
                            ordermenu.update_order_status()
                        
                        elif order_menu_choice == 4:
                            # ordermenu.update_order(orders)
                            pass #***Need to fix!***
                        
                        elif order_menu_choice == 5:
                            shared.delete_item('order')
                        
                        elif order_menu_choice == 6:
                            break # Returns to main menu
                        
                        elif order_menu_choice == 0:
                            utils.exit_app()
                            
                        else:
                            utils.invalid_number_error()
                    
                    except ValueError:
                        utils.invalid_input_error()
            
            elif main_choice == 0:
                utils.exit_app()
                
            else:
                utils.invalid_number_error()
        
        except ValueError:
            utils.invalid_input_error()


### RUNNING THE APP ###
def run_app():
    utils.welcome()
    navigate_menu()

run_app()
