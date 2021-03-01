### RUNS JAM'S CAFE APP ###
# Jam's Cafe app v2.95

# from utils import *
# from appmenu import display_main_menu
# from courier import load_courier_menu
# from order import load_order_menu
# from product import load_product_type_menu

from source.utils import *
from source.appmenu import display_main_menu
from source.courier import load_courier_menu
from source.order import load_order_menu
from source.product import load_product_type_menu


welcome()

while True: # Reloads the app menu
    menu_choice = display_main_menu() # Gets user's menu option selection
    clear_terminal()
    app_title()
    
    try: # Processes user's main menu selection
        menu_choice = int(menu_choice)
        
        if menu_choice == 1:
            load_product_type_menu()
                
        elif menu_choice == 2:
            load_courier_menu()
        
        elif menu_choice == 3:
            load_order_menu()
        
        elif menu_choice == 0:
            exit_app()
            
        else:
            invalid_number_error()
    
    except ValueError:
        invalid_input_error()
