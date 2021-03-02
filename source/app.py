### RUNS JAM'S CAFE APP ###
# Jam's Cafe app v2.95

import utils, appmenu, courier, order, product

utils.welcome()

while True: # Reloads the app menu
    menu_choice = appmenu.display_main_menu() # Gets user's menu option selection
    utils.clear_terminal()
    utils.app_title()
    
    try: # Processes user's main menu selection
        menu_choice = int(menu_choice)
        
        if menu_choice == 1:
            product.load_product_type_menu()
                
        elif menu_choice == 2:
            courier.load_courier_menu()
        
        elif menu_choice == 3:
            order.load_order_menu()
        
        elif menu_choice == 0:
            utils.exit_app()
            
        else:
            utils.invalid_number_error()
    
    except ValueError:
        utils.invalid_input_error()
